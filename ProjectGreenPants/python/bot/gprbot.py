#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
green pants revenge bot
"""

import logging
import os
import random
from combat import attack, defend
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('gpr bot started')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("-Commands-\r\n\r\nAttack:\r\n/a <Skill #>\r\n\t[weapon skill + modifiers like advantage. ex: /a 60]\r\n\r\nDefend:\r\n/d <Skill #>\r\n\t[weapon skill + modifiers like advantage. ex: /d 50]\r\n\r\nRoll Dice:   (1d100)\r\n/r\r\n\t[roll 1d100. ex: /r]\r\n\r\n-Note-\r\n\tBi = Biped(Human/Humanoid)\r\n\tQuad = Quadruped(Beast)")

def attack_handler(update, context):
    username = update.message.from_user.first_name
    #response = f"[ATT] @{username} [SL]:+5  [Roll]:18  [Bi/Quad]: L-Leg/BL-Leg"   
    response = ""
    if len (context.args) == 0 or not context.args[0].isdigit():
        response = "attack usage: /a <skill>\r\n\t\twhere <skill> is your weapon skill + any combat modifiers"
    else:
        response = attack (int(context.args[0]), username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def defend_handler(update, context):
    username = update.message.from_user.first_name
    #response = f"[DEF] @{username} [SL]:+5  [Roll]:18  [Bi/Quad]: L-Leg/BL-Leg"   
    response = ""
    if len (context.args) == 0 or not context.args[0].isdigit():
        response = "defend usage: /d <skill>\r\n\t\twhere <skill> is your weapon skill + any combat modifiers"
    else:
        response = defend (int(context.args[0]), username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def roll_handler(update, context):
    username = update.message.from_user.first_name
    result = int(random.uniform (1, 100))
    response = f"[Roll @{username}]: {result}"   
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.environ["GPR_BOT_TOKEN"], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler(["a","attack"], attack_handler))
    dp.add_handler(CommandHandler(["d","defend"], defend_handler))
    dp.add_handler(CommandHandler(["r","roll"], roll_handler))
 
    # on noncommand i.e message - echo the message on Telegram
    #  dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()