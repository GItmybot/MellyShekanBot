# MellyShekanBotimport asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# توکن بات را اینجا بعداً امن‌تر می‌کنیم
TOKEN = "8992822551:AAHkhv_myuoQg2rVFGhU5OUo-ycmDLjzEzE"


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 سلام به Melly Shekan خوش آمدید 🌐\n\n"
        "🚀 فروش کانفیگ V2Ray\n"
        "برای مشاهده خدمات از منو استفاده کنید."
    )


@dp.message()
async def echo(message: Message):
    await message.answer(
        "✅ پیام شما دریافت شد.\n"
        "به زودی امکانات فروش فعال می‌شود 💎"
    )


async def main():
    print("Melly Shekan Bot Started ✅")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
