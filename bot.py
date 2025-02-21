import asyncio

import betterlogging as logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder

# from models.initialization import db_init, db_shutdown
from tgbot.config import load_config, Config
from tgbot.handlers import routers_list
from tgbot.middlewares.middleware_factory import MiddlewareFactory
from tgbot.services import broadcaster

logging.basic_colorized_config(level=logging.INFO)
logger = logging.getLogger(__name__)


async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, 'Bot started !')


def register_global_middlewares(dp: Dispatcher, config: Config):
    """
    Register global middlewares for the given dispatcher.
    Global middlewares here are the ones that are applied to all the handlers (you specify the type of update)

    :param dp: The dispatcher instance.
    :type dp: Dispatcher
    :param config: The configuration object from the loaded configuration.
    :return: None
    """
    middleware_types = [
        MiddlewareFactory(config, 'config'),
    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)


def get_storage(config):
    """
    Return storage based on the provided configuration.

    Args:
        config (Config): The configuration object.

    Returns:
        Storage: The storage object based on the configuration.

    """
    if config.tg_bot.use_redis:
        return RedisStorage.from_url(
            config.redis.dsn(),
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )
    else:
        return MemoryStorage()


async def main():
    config = load_config('.env')
    storage = get_storage(config)

    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=config.tg_bot.token, default=default)
    dp = Dispatcher(storage=storage)

    dp.include_routers(*routers_list)

    register_global_middlewares(dp, config)

    await on_startup(bot, config.tg_bot.admin_ids)

    # await db_init()

    logger.info('Starting bot :)')

    await dp.start_polling(bot)

    # await db_shutdown()

    logging.info('Bot stopped :(')


if __name__ == '__main__':
    try:
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped :(')
