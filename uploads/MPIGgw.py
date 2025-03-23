import telebot
import random
import os

# ✅ تخزين التوكن داخل السكربت مباشرةً
TOKEN = "7971927949:AAGOa6BIVh4qOX2zLtjSiuy_Z9r6or0jL70"
bot = telebot.TeleBot(TOKEN)

# ✅ مفتاح الدخول الصحيح
SECRET_KEY = "77"

# ✅ قائمة أكواد الدول المعروفة
COUNTRY_CODES = [
    "1", "20", "33", "44", "49", "55", "81", "91", "972", "964", "7", "34"
]

# ✅ توليد أرقام هواتف عشوائية من جميع دول العالم بدون طلب رمز دولة
def generate_global_phone_numbers(count=100000):
    telecom_providers = ["Asiacell", "Zain", "Ooredoo", "Vodafone", "Orange", "AT&T", "T-Mobile", "Airtel", "Etisalat", "STC"]
    
    numbers = [
        f"+{random.choice(COUNTRY_CODES)}{random.randint(10000000, 99999999)} | {random.choice(telecom_providers)} | {'نعم' if random.choice([True, False]) else 'لا'}"
        for _ in range(count)
    ]

    with open("GLOBAL_NUMBERS.txt", "w") as file:
        file.write("\n".join(numbers))

# ✅ توليد يوزرات إنستقرام عشوائية بأحرف وأرقام (3-4 أحرف)
def generate_instagram_users(count=1000):
    usernames = [''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=random.choice([3, 4]))) for _ in range(count)]
    with open("INSTAGRAM_USERS.txt", "w") as file:
        file.write("\n".join(usernames))

# ✅ توليد إيميلات بأسماء عشوائية بدلاً من "user"
def generate_random_emails(count=1000):
    names = ["Ali", "Omar", "Sara", "Lina", "Hassan", "Kareem", "Fatima", "Mona", "Aisha", "John", "Emma", "David"]
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    emails = [f"{random.choice(names)}{random.randint(1000, 9999)}@{random.choice(domains)}" for _ in range(count)]
    with open("RANDOM_EMAILS.txt", "w") as file:
        file.write("\n".join(emails))

# ✅ توليد بطاقات فيزا عشوائية مع معلوماتها
def generate_credit_cards(count=100000):
    cards = [f"4000{random.randint(100000000000, 999999999999)} | CVV: {random.randint(100, 999)} | Exp: {random.randint(1, 12)}/{random.randint(24, 29)} | Balance: ${round(random.uniform(1, 5000), 2)}" for _ in range(count)]
    with open("CREDIT_CARDS.txt", "w") as file:
        file.write("\n".join(cards))

# ✅ توليد بطاقات جوجل بلاي
def generate_google_play_cards(count=10000):
    cards = [f"{random.randint(100000000000000, 999999999999999)}" for _ in range(count)]
    with open("GOOGLE_PLAY_CARDS.txt", "w") as file:
        file.write("\n".join(cards))

# ✅ توليد إيديات فيسبوك حقيقية النمط
def generate_facebook_ids(count=100000):
    years = [2006, 2007, 2008, 2009, 2010]
    ids = [f"{random.choice(years)} | 1000{random.randint(1000000000, 9999999999)}" for _ in range(count)]
    with open("FACEBOOK_IDS.txt", "w") as file:
        file.write("\n".join(ids))

# ✅ توليد كوكيز عشوائية للفيسبوك
def generate_facebook_cookies(count=10000):
    cookies = [f"c_user={random.randint(1000000000, 9999999999)}; xs={random.randint(10, 99)}%3A{random.randint(1000000000, 9999999999)}%3A{random.randint(1, 3)}" for _ in range(count)]
    with open("FACEBOOK_COOKIES.txt", "w") as file:
        file.write("\n".join(cookies))

# ✅ إنشاء لوحة تحكم عصرية للبوت
def get_main_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        telebot.types.InlineKeyboardButton("📜 يوزرات إنستقرام", callback_data="INSTAGRAM_USERS"),
        telebot.types.InlineKeyboardButton("📜 إيميلات عشوائية", callback_data="RANDOM_EMAILS"),
        telebot.types.InlineKeyboardButton("📞 أرقام عشوائية", callback_data="GLOBAL_NUMBERS"),
        telebot.types.InlineKeyboardButton("💳 بطاقات فيزا", callback_data="CREDIT_CARDS"),
        telebot.types.InlineKeyboardButton("🎮 بطاقات جوجل بلاي", callback_data="GOOGLE_PLAY_CARDS"),
        telebot.types.InlineKeyboardButton("🆔 إيديات فيسبوك", callback_data="FACEBOOK_IDS"),
        telebot.types.InlineKeyboardButton("🍪 كوكيز فيسبوك", callback_data="FACEBOOK_COOKIES"),
        telebot.types.InlineKeyboardButton("👤 مالك البوت", url="https://t.me/QP4RM")
    )
    return keyboard

# ✅ عند بدء المحادثة
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "🎉 **مرحبًا بك في البوت العصري!**\n\n🔑 *أرسل المفتاح للبدء.*", parse_mode="Markdown")

# ✅ التحقق من المفتاح
@bot.message_handler(func=lambda message: message.text == SECRET_KEY)
def check_key(message):
    bot.send_message(message.chat.id, "✅ المفتاح صحيح! يمكنك الآن استخدام الأوامر.", reply_markup=get_main_keyboard())

# ✅ التعامل مع الأزرار وإرسال الملفات
@bot.callback_query_handler(func=lambda call: call.data in ["INSTAGRAM_USERS", "RANDOM_EMAILS", "GLOBAL_NUMBERS", "CREDIT_CARDS", "GOOGLE_PLAY_CARDS", "FACEBOOK_IDS", "FACEBOOK_COOKIES"])
def handle_buttons(call):
    file_map = {
        "INSTAGRAM_USERS": ("📜 يتم إنشاء يوزرات إنستقرام...", "INSTAGRAM_USERS.txt", generate_instagram_users, 1000),
        "RANDOM_EMAILS": ("📜 يتم إنشاء إيميلات عشوائية...", "RANDOM_EMAILS.txt", generate_random_emails, 1000),
        "GLOBAL_NUMBERS": ("📞 يتم إنشاء أرقام عشوائية...", "GLOBAL_NUMBERS.txt", generate_global_phone_numbers, 100000),
        "CREDIT_CARDS": ("💳 يتم إنشاء بطاقات فيزا...", "CREDIT_CARDS.txt", generate_credit_cards, 100000),
        "GOOGLE_PLAY_CARDS": ("🎮 يتم إنشاء بطاقات جوجل بلاي...", "GOOGLE_PLAY_CARDS.txt", generate_google_play_cards, 10000),
        "FACEBOOK_IDS": ("🆔 يتم إنشاء إيديات فيسبوك...", "FACEBOOK_IDS.txt", generate_facebook_ids, 100000),
        "FACEBOOK_COOKIES": ("🍪 يتم إنشاء كوكيز فيسبوك...", "FACEBOOK_COOKIES.txt", generate_facebook_cookies, 10000),
    }

    bot.send_message(call.message.chat.id, file_map[call.data][0])
    file_map[call.data][2](file_map[call.data][3])
    with open(file_map[call.data][1], "rb") as file:
        bot.send_document(call.message.chat.id, file)

# ✅ تشغيل البوت
bot.polling()
