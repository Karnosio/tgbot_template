from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter

router = Router()
router.message.filter(AdminFilter())


@router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply('echo handler')
