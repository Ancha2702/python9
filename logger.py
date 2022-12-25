from telegram import Update
from telegram.ext import CallbackContext
import time

def write_log(update: Update, context: CallbackContext):
    file = open('Калькулятор.csv', 'a', encoding ='utf-8')
    file.write(f'{time.ctime(time.time())} | {update.effective_user.first_name} | {update.effective_user.id} | {update.message.text} | {context.args}\n')
    file.close()