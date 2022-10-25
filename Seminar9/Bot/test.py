from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

file = open('Tokens.txt', 'r')
token = file.read().strip()
print(token)

app = ApplicationBuilder().token("{token}").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("expression", expression_command))

print('server start')

app.run_polling()
