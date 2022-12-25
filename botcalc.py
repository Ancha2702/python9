from telegram import Update
from telegram.ext import CallbackContext

import time, math
from logger import write_log


def callback(update: Update, context: CallbackContext):
    after_command = context.args
    print(after_command)
    update.message.reply_text('Привет,я калькулятор')


def get_message(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if "прив" in message:
        update.message.reply_text("Привет!")
        return None
    update.message.reply_text(f'Вы ввели: {message},\n , нажмите /help, чтобы узнать, что я умею.')


def help_command(update: Update, context: CallbackContext):
    write_log(update, context)
    after_command = context.args
    # message = update.message.text
    print(after_command)
    update.message.reply_text(
        f'/hello - Приветствие \n /time - Текущее время \n/help - Помощь \n/sum - Сложение\n/sub -Разность\n/mult - Умножение\n/div -Деление \n/pow - Степень \n/sqrt - Корень числа\n'
        f'Пример: /sum 2 3')


def time_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    update.message.reply_text(f'{time.ctime(time.time())}')


def sum_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    if ',' in message:
        update.message.reply_text(f'Введите число-разделитель точка{message}')
    else:
        items = message.split()
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} + {y} = {x + y}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')



def sub_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message:
        update.message.reply_text(f'Введите число-разделитель точка{message}')
    else:
        items = message.split()
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} - {y} = {x - y}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')


def mult_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message:
        update.message.reply_text(f'Введите число-разделитель точка{message}')
    else:
        items = message.split()
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} * {y} = {round(x * y), 6}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')


def div_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message:
        update.message.reply_text(f'Введите число-разделитель точка. Вы ввели {message}')
    else:
        items = message.split()  # /div 123 534543
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} / {y} = {round(x / y, 6)}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')


def pow_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message:
        update.message.reply_text(f'Введите число-разделитель точка{message}')
    else:
        items = message.split()
        if len(items) != 3:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f'{x} в степени {y} = {round(x ** y), 6}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')


def sqrt_command(update: Update, context: CallbackContext):
    write_log(update, context)
    message = update.message.text
    print(message)
    if ',' in message:
        update.message.reply_text(f'Введите число-разделитель точка{message}')
    else:
        items = message.split()
        if len(items) != 2:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}')
        elif not items[1].isalpha() and not items[2].isalpha():
            x = float(items[1])
            y = float(items[2])
            update.message.reply_text(f' корень {x} = {round(math.sqrt(x)), 6}')
        else:
            update.message.reply_text(f'Некорректный ввод. Вы ввели {message}, возможно это не цифры')
