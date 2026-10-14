# ==============================================================================
#               H A C K E R   T R A D E R   A S S I S T A N T
# ==============================================================================
# Brand: HACKER VIP TRADING BOT
# Version: 1.1 Stable Crash-Free Edition
# ==============================================================================

import os
import json
import logging
import time
import telebot
from telebot import types

# --- LOGGING CONFIGURATION ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger("HACKER_ASSISTANT_BOT")

# --- CREDENTIALS ---
BOT_TOKEN = "8854893422:AAET-ureA2Nqx_-133Dh4YknUnOFIx5QVsw"
SUPPORT_USERNAME = "HACKERRR_OFFICIAL"
QUOTEX_LINK = "https://broker-qx.pro/?lid=2382183"
ADMIN_ID = 6810437899

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown', threaded=True, num_threads=16)

user_states = {}
user_data = {}
DB_FILE = "traders_db.json"

def load_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_db(db):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(db, f, indent=4)
    except Exception:
        pass

db = load_db()

# --- KEYBOARDS ---

def main_menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🚀 VIP JOINING PROCESS", callback_data="vip_process"),
        types.InlineKeyboardButton("📈 HOW TO CREATE QUOTEX NEW ACCOUNT", callback_data="create_acc"),
        types.InlineKeyboardButton("🗑️ HOW TO DELETE QUOTEX OLD ACCOUNT", callback_data="delete_acc"),
        types.InlineKeyboardButton("👑 OUR VIP GROUPS PICS", callback_data="vip_pics"),
        types.InlineKeyboardButton("📩 SEND TRADER ID HERE", callback_data="send_id"),
        types.InlineKeyboardButton("❓ ANY QUESTION DM US", url=f"https://t.me/{SUPPORT_USERNAME}")
    )
    return markup

def back_menu_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("◀️ BACK TO MENU", callback_data="back_home"))
    return markup

# --- COMMAND HANDLERS ---

@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_states[user_id] = None

    welcome_msg = (
        f"👋 **Hello Dear {name} TRADER**\n\n"
        f"🤖 **Welcome to HACKER ASSISTANT BOT**, Can I help you?\n\n"
        f"🔥 **HACKER TRADER thanks for contacting!**\n"
        f"✅ Free signals group link:\n`https://t.me/Hacker_official_804`\n\n"
        f"💬 Join now for free signals everyday\n\n"
        f"🛡️ If any problem smsg me: @{SUPPORT_USERNAME}"
    )
    
    bot.send_message(message.chat.id, welcome_msg, reply_markup=main_menu_markup())

# --- CALLBACK QUERY HANDLERS ---

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    user_id = call.from_user.id
    data = call.data

    if data == "back_home":
        user_states[user_id] = None
        try:
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="🤖 **Main Menu - Select an option below:**",
                reply_markup=main_menu_markup()
            )
        except Exception:
            bot.send_message(call.message.chat.id, "🤖 **Main Menu:**", reply_markup=main_menu_markup())

    elif data == "vip_process":
        text = (
            "📌 **VIP JOINING PROCESS**\n\n"
            "Make 30$ Deposit get access in Our All VIPs Groups\n\n"
            f"1️⃣ **Create New Account With This Link:**\n{QUOTEX_LINK}\n\n"
            "2️⃣ **After Creating Account Send Your Trader By Clicking Below Button**"
        )
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("📩 SEND TRADER ID HERE", callback_data="send_id"),
            types.InlineKeyboardButton("◀️ BACK", callback_data="back_home")
        )
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, disable_web_page_preview=True)
        except Exception:
            pass

    elif data == "create_acc":
        text = (
            "📈 **How to Create a New Quotex Account:**\n\n"
            f"1️⃣ Click on my link:\n{QUOTEX_LINK}\n"
            "2️⃣ Select, put new email and strong password.\n"
            "3️⃣ Accept terms & conditions.\n"
            "4️⃣ Click on registration - account registration successful.\n"
            "5️⃣ Check your email - you received a link for verification - verify your email.\n"
            "6️⃣ Then go to your profile and verify with documents (Identity card).\n\n"
            "✅ **Done! Your account is ready to deposit.**"
        )
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=back_menu_markup(), disable_web_page_preview=True)
        except Exception:
            pass

    elif data == "delete_acc":
        text = (
            "🗑️ **How To Delete Your Old Quotex Account:**\n\n"
            "1️⃣ Go to profile option.\n"
            "2️⃣ Scroll down and select delete account.\n"
            "3️⃣ Check your email - you will receive a link for deleting the account.\n"
            "4️⃣ Click on the link you received on email - account is deleted successfully.\n\n"
            "💡 **Now you can register a fresh account using our affiliate link.**"
        )
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=back_menu_markup())
        except Exception:
            pass

    elif data == "vip_pics":
        text = (
            "👑 **OUR VIP FUTURE SIGNALS GROUP**\n\n"
            "We Provide Daily 100% High Accurate Quotex Future Signals 🚀\n\n"
            f"🔗 Join Our VIP: @{SUPPORT_USERNAME}"
        )
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔥 JOIN NOW OUR VIP", url=QUOTEX_LINK))
        markup.add(types.InlineKeyboardButton("◀️ BACK", callback_data="back_home"))
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup, disable_web_page_preview=True)
        except Exception:
            pass

    elif data == "send_id":
        user_states[user_id] = 'awaiting_trader_id'
        text = "📝 **Please Send Your Trader Id Here:**\n*(Type your ID in chat and send)*"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("❌ CANCEL", callback_data="back_home"))
        try:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=markup)
        except Exception:
            pass

# --- TEXT HANDLER FOR TRADER ID ---

@bot.message_handler(func=lambda m: user_states.get(m.from_user.id) == 'awaiting_trader_id')
def receive_trader_id(message):
    user_id = message.from_user.id
    trader_id_text = message.text.strip()
    user_states[user_id] = None

    db[str(user_id)] = {
        "username": message.from_user.username,
        "name": message.from_user.first_name,
        "trader_id": trader_id_text
    }
    save_db(db)

    bot.send_message(
        message.chat.id,
        f"✅ **Thank you!** Your Trader ID `{trader_id_text}` has been successfully received.\nOur team will verify and contact you soon.",
        reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🏠 MAIN MENU", callback_data="back_home"))
    )

    try:
        bot.send_message(
            ADMIN_ID,
            f"🔔 **NEW TRADER ID RECEIVED!**\n\n"
            f"👤 User: {message.from_user.first_name} (@{message.from_user.username})\n"
            f"🆔 User ID: `{user_id}`\n"
            f"🔑 Trader ID: `{trader_id_text}`"
        )
    except Exception:
        pass

if __name__ == "__main__":
    logger.info("Hacker Trader Assistant Bot is starting...")
    while True:
        try:
            bot.remove_webhook()
            bot.infinity_polling(skip_pending=True, timeout=20, long_polling_timeout=20)
        except Exception as e:
            logger.error(f"Bot crashed with error: {e}. Restarting in 5 seconds...")
            time.sleep(5)
