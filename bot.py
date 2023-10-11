# from telegram.ext import Updater, CommandHandler

# # This function will be called when the "/start" command is sent to the bot
# def start(update, context):
#     update.message.reply_text('שלום שוטר')

# # Initialize the Updater
# updater = Updater(token='6350910417:AAEKdQx5xaDsGUPLFmbM1mQik-0abDOJo54', use_context=True)

# # Get the dispatcher to register handlers
# dispatcher = updater.dispatcher

# # Add command handler for "/start"
# dispatcher.add_handler(CommandHandler('start', start))

# # Start the Bot
# updater.start_polling()
import telebot

bot = telebot.TeleBot('6350910417:AAEKdQx5xaDsGUPLFmbM1mQik-0abDOJo54')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "שלום לך")

bot.polling()
