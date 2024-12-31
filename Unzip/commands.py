from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import Config

active_tasks = {}

# Function to check if a user is subscribed to all required channels
async def is_subscribed_to_all(client, user_id):
    for channel_id in config.FORCE_SUB_CHANNELS:
        try:
            member = await client.get_chat_member(chat_id=int(channel_id), user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False, channel_id
        except Exception:
            return False, channel_id
    return True, None

@Client.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    is_subscribed, unsubscribed_channel = await is_subscribed_to_all(client, user_id)
    
    if not is_subscribed:
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Join Channel", url=f"https://t.me/c/{unsubscribed_channel.replace('-100', '')}")],
                [InlineKeyboardButton("Retry", callback_data="check_subscription")]
            ]
        )
        await message.reply(
            "❌ You must join all required channels to use this bot.",
            reply_markup=reply_markup
        )
        return

    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Update Channel", url="https://t.me/JN2FLIX")],
            [InlineKeyboardButton("MORE BOTS", url="https://t.me/ROCKERSBACKUP")],
        ]
    )
    start_message = (
        "Hello!\n\n"
        "Send me a ZIP file, and I'll unzip it for you."
    )
    await message.reply(start_message, reply_markup=reply_markup)

@Client.on_callback_query(filters.regex("check_subscription"))
async def check_subscription(client, callback_query):
    user_id = callback_query.from_user.id
    is_subscribed, unsubscribed_channel = await is_subscribed_to_all(client, user_id)

    if not is_subscribed:
        await callback_query.answer("❌ You are not subscribed to all required channels!", show_alert=True)
    else:
        await callback_query.message.delete()
        await callback_query.message.reply(
            "✅ Thank you for subscribing! You can now use the bot."
        )

@Client.on_message(filters.command("help"))
async def help_command(client, message):
    user_id = message.from_user.id
    is_subscribed, unsubscribed_channel = await is_subscribed_to_all(client, user_id)
    
    if not is_subscribed:
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Join Channel", url=f"https://t.me/c/{unsubscribed_channel.replace('-100', '')}")],
                [InlineKeyboardButton("Retry", callback_data="check_subscription")]
            ]
        )
        await message.reply(
            "❌ You must join all required channels to use this bot.",
            reply_markup=reply_markup
        )
        return

    help_message = (
        "Here are the commands you can use:\n\n"
        "/start - Start the bot and get the welcome message\n"
        "/help - Get help on how to use the bot\n\n"
        "To unzip a file, simply send me a ZIP file and I will extract its contents and send them back to you.\n\n"
        "©️ Channel : @JN2FLIX"
    )
    await message.reply(help_message)

@Client.on_callback_query(filters.regex("cancel_unzip"))
async def cancel_callback(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id in active_tasks:
        task = active_tasks[user_id]
        task.cancel()
        await callback_query.answer("⛔ Unzipping has been cancelled.", show_alert=True)
    else:
        await callback_query.answer("⚠️ No ongoing unzip operation.", show_alert=True)
