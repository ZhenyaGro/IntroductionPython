from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'/hello\n/expression\n/help\n')


async def expression_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /expression 7+8
    result = eval(items[1])

    await update.message.reply_text(f'{items[1]} = {result}')
