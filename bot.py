import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database import init_db, add_user


# =========================
# تنظیمات بات
# =========================

TOKEN = "YOUR_TOKEN"
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
# پاسخ به دکمه‌ها
# =========================

@dp.message()
async def menu_handler(message: Message):

    text = message.text

    if text == "🛒 خرید کانفیگ":
        await message.answer(
            "🛒 بخش خرید کانفیگ\n\n"
            "💎 لطفاً نوع سرویس خود را انتخاب کنید."
        )

    elif text == "📦 سرویس‌های من":
        await message.answer(
            "📦 سرویس‌های شما\n\n"
            "هنوز سرویسی برای نمایش وجود ندارد."
        )

    elif text == "👤 حساب کاربری":
        await message.answer(
            f"👤 اطلاعات حساب شما\n\n"
            f"🆔 شناسه کاربری: {message.from_user.id}\n"
            f"👤 نام: {message.from_user.first_name}"
        )

    elif text == "🎁 دعوت دوستان":
        await message.answer(
            "🎁 سیستم دعوت دوستان\n\n"
            "👥 با دعوت ۱۰ نفر از دوستان خود:\n"
            "🎁 ۱۰ گیگ اینترنت رایگان\n"
            "⏳ به مدت ۲۰ روز دریافت کنید."
        )

    elif text == "🎟 کد تخفیف":
        await message.answer(
            "🎟 کد تخفیف\n\n"
            "اگر کد تخفیف دارید، آن را ارسال کنید."
        )

    elif text == "🆘 پشتیبانی":
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
