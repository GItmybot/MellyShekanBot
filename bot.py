import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database import init_db, add_user
from config import BOT_TOKEN


# =========================
# تنظیمات بات
# =========================

TOKEN = BOT_TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


# =========================
# منوی اصلی
# =========================

def main_menu():
    builder = ReplyKeyboardBuilder()

    builder.button(text="🛒 خرید کانفیگ")
    builder.button(text="📦 سرویس‌های من")
    builder.button(text="👤 حساب کاربری")
    builder.button(text="🎁 دعوت دوستان")
    builder.button(text="🎟 کد تخفیف")
    builder.button(text="🆘 پشتیبانی")

    builder.adjust(2, 2, 2)

    return builder.as_markup(
        resize_keyboard=True
    )


# =========================
# شروع بات
# =========================

@dp.message(CommandStart())
async def start(message: Message):

    user = message.from_user

    add_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name
    )

    await message.answer(
        f"👋 سلام {user.first_name} عزیز!\n\n"
        "🌐 به ربات رسمی Melly Shekan خوش آمدید.\n\n"
        "🚀 فروش کانفیگ V2Ray\n"
        "⚡ سریع، پایدار و حرفه‌ای\n\n"
        "👇 از منوی زیر انتخاب کنید:",
        reply_markup=main_menu()
    )


# =========================
# خرید کانفیگ
# =========================

@dp.message(lambda message: message.text == "🛒 خرید کانفیگ")
async def buy_config(message: Message):

    await message.answer(
        "🛒 بخش خرید کانفیگ\n\n"
        "💎 سرویس VIP\n"
        "🎮 سرویس Gaming\n\n"
        "به‌زودی انتخاب پلن‌ها فعال می‌شود."
    )


# =========================
# سرویس‌های من
# =========================

@dp.message(lambda message: message.text == "📦 سرویس‌های من")
async def my_services(message: Message):

    await message.answer(
        "📦 سرویس‌های شما\n\n"
        "هنوز سرویسی برای نمایش وجود ندارد."
    )


# =========================
# حساب کاربری
# =========================

@dp.message(lambda message: message.text == "👤 حساب کاربری")
async def account(message: Message):

    user = message.from_user

    await message.answer(
        "👤 اطلاعات حساب شما\n\n"
        f"🆔 شناسه کاربری: {user.id}\n"
        f"👤 نام: {user.first_name}\n"
        f"🔗 نام کاربری: @{user.username if user.username else 'ندارد'}"
    )


# =========================
# دعوت دوستان
# =========================

@dp.message(lambda message: message.text == "🎁 دعوت دوستان")
async def referrals(message: Message):

    bot_info = await bot.get_me()

    referral_link = (
        f"https://t.me/{bot_info.username}"
        f"?start=ref_{message.from_user.id}"
    )

    await message.answer(
        "🎁 سیستم دعوت دوستان\n\n"
        "👥 با دعوت ۱۰ نفر از دوستان خود:\n"
        "🎁 ۱۰ گیگ اینترنت رایگان دریافت کنید.\n"
        "⏳ مدت اعتبار: ۲۰ روز\n\n"
        "🔗 لینک دعوت اختصاصی شما:\n"
        f"{referral_link}"
    )


# =========================
# کد تخفیف
# =========================

@dp.message(lambda message: message.text == "🎟 کد تخفیف")
async def discount(message: Message):

    await message.answer(
        "🎟 کد تخفیف\n\n"
        "کد تخفیف خود را ارسال کنید تا بررسی شود."
    )


# =========================
# پشتیبانی
# =========================

@dp.message(lambda message: message.text == "🆘 پشتیبانی")
async def support(message: Message):

    await message.answer(
        "🆘 پشتیبانی Melly Shekan\n\n"
        "📩 ارتباط با پشتیبانی:\n"
        "@Mellyshekan_support"
    )


# =========================
# اجرای بات
# =========================

async def main():

    init_db()

    print("Melly Shekan Bot Started ✅")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
