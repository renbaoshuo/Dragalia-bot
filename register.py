import botSession
from mdFunctions import *
from mdMessage import process_msg
from mdComic import life, sync_life
from telegram.ext import MessageHandler, CommandHandler, Filters


def register_handlers():
    dp = botSession.dp

    dp.add_handler(CommandHandler(['delay', 'ping'], delay))
    dp.add_handler(CommandHandler(['life', 'comic'], life))
    dp.add_handler(CommandHandler(['time', 'timer', 'when', 'hour'], send_time))
    dp.add_handler(CommandHandler('start', private_start, Filters.chat_type.private))
    dp.add_handler(CommandHandler('help', private_help, Filters.chat_type.private))
    dp.add_handler(CommandHandler(['en', 'Eng', 'English'], help_english, Filters.chat_type.private))
    dp.add_handler(CommandHandler(['ja', 'Japanese'], help_japanese, Filters.chat_type.private))

    dp.add_handler(MessageHandler(Filters.chat_type.groups, process_msg))
    dp.add_handler(MessageHandler((Filters.command & Filters.chat_type.private), private_unknown))
    dp.add_handler(MessageHandler(Filters.chat_type.private, private_message))

    return True


def manager():
    scheduler = botSession.scheduler
    scheduler.add_job(sync_life, 'cron', hour=14, minute=1)
