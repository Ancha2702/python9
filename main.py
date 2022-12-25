from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN
from botcalc import *


updater = Updater(TOKEN)
dispetcher = updater.dispatcher

hello_handler = CommandHandler('hello', callback)
start_handler = CommandHandler('start', get_message)
help_handler = CommandHandler('help', help_command)
time_handler = CommandHandler('time', time_command)
sum_handler = CommandHandler('sum', sum_command)
sub_handler = CommandHandler('sub', sub_command)
mult_handler = CommandHandler('mult', mult_command)
div_handler = CommandHandler('div', div_command)
pow_handler = CommandHandler('pow', pow_command)
sqrt_handler = CommandHandler('sqrt', sqrt_command)

message_handler = MessageHandler(Filters.text, get_message)

dispetcher.add_handler(hello_handler)
dispetcher.add_handler(time_handler)
dispetcher.add_handler(start_handler)
dispetcher.add_handler(help_handler)
dispetcher.add_handler(sum_handler)
dispetcher.add_handler(sub_handler)
dispetcher.add_handler(mult_handler)
dispetcher.add_handler(div_handler)
dispetcher.add_handler(pow_handler)
dispetcher.add_handler(sqrt_handler)

# last dispetcher
dispetcher.add_handler(message_handler)

print('сервер запущен')
updater.start_polling()
updater.idle()