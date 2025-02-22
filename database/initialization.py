from tortoise import Tortoise

from tgbot.config import load_config

config = load_config('.env')


models = [
    # 'tgbot.models.product'
]
TORTOISE_ORM = {
    'connections': {
        'default': config.db.construct_url()
    },
    'apps': {
        'models': {
            'models': models + ['aerich.models'],
            'default_connection': 'default',
        }
    }
}


async def db_init():
    await Tortoise.init(db_url=config.db.construct_url(), modules={'models': models})
    await Tortoise.generate_schemas()


async def db_shutdown():
    await Tortoise.close_connections()
