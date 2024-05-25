import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename = 'bot.log', level = logging.INFO)
import settings

def greet_user(update, context):  # update - это то, что поступило от пользователя Telegram. Context - это спец. штука с помощью которой мы можем изнутри функции отдавать команды боту
    print('Вызван /start')
    print(update.message.reply_text('Здравствуй пользователь!'))

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context = True)
    
    dp = mybot.dispatcher  # в переменную dp кладём это, чтобы в дальнейшем не набирать длинное название
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()

main()