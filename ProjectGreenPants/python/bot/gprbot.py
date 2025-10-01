#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
green pants revenge bot
"""

import logging
import os
import random
from combat import attack, defend, multiskill, oops, skill, winds, probability
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
    update.message.reply_text("-Commands-\r\n\r\nAttack:\r\n\t/a <Skill #>\r\n\t[weapon skill + modifiers like advantage. ex: /a 60]\r\n\r\nDefend:\r\n\t/d <Skill #>\r\n\t[weapon skill + modifiers like advantage. ex: /d 50]\r\n\r\nOops:\r\n\t/o\r\n\t[roll 1d100 on oops! table. ex: /o]\r\n\r\nRoll:   (1d100, 1d10, 2d10)\r\n\t/r\r\n\t[randomly generate rolls for 1d100, 1d10, 2d10. ex: /r]\r\n\r\nSkill:\r\n\t/s <Skill #>\r\n\t[skill + modifiers. ex: /s 50]\r\n\r\nSkill (multiple):\r\n\t/sm <Skill #> <Count>\r\n\t[skill + modifiers and count of rolls to make. ex: /sm 50 8]\r\n\r\nWinds:\r\n\t/w\r\n\t[determine the strength of the winds of magic.  ex. /w]\r\n\r\n-Note-\r\n\r\n\tBi = Biped(Human/Humanoid)\r\n\tQuad = Quadruped(Beast)")

def attack_handler(update, context):
    username = update.message.from_user.first_name
    response = ""
    if len (context.args) == 0 or not context.args[0].isdigit():
        response = "attack usage: /a <skill>\r\n\t\twhere <skill> is your weapon skill + any combat modifiers"
    else:
        response = attack (int(context.args[0]), username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def defend_handler(update, context):
    username = update.message.from_user.first_name
    response = ""
    if len (context.args) == 0 or not context.args[0].isdigit():
        response = "defend usage: /d <skill>\r\n\t\twhere <skill> is your weapon skill + any combat modifiers"
    else:
        response = defend (int(context.args[0]), username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def oops_handler(update, context):
    username = update.message.from_user.first_name
    response = ""
    response = oops (username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def winds_handler(update, context):
    username = update.message.from_user.first_name
    response = ""
    response = winds (username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def roll_handler(update, context):
    argc = len (context.args)
    username = update.message.from_user.first_name
    if argc == 0:
        username = update.message.from_user.first_name
        result = int(random.randint (1, 100))
        result10a = int(random.randint (1, 10))
        result10b = int(random.randint (1, 10))
        result2d10 = result10a + result10b
        response = f"[roll @{username}]: 1d100={result}          1d10={result10a}          2d10={result2d10}"   
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        return
            
    if argc == 1 and context.args[0].isdigit():
        response = f"[roll @{username}]: "
        rolls = int(context.args[0])
        for r in range (rolls):
            response += str (random.randint (1, 10)) + ' '
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        return

    if argc == 2 and context.args[0].isdigit() and context.args[1].isdigit():
        response = f"[ROLL @{username}]: "
        rolls = int(context.args[0])
        skill = int(context.args[1])
        S = 0
        F = 0
        response += '[' + str(rolls) + 'd10 vs ' + str (skill) + '] \n    '
        for r in range (rolls):
            rnd = random.randint (1, 10)
            if rnd <= skill:
                S += 1
            else:
                F += 1
            response += str (rnd)
            response += '  '
        response += '   ['
        if (S > 0):
            response += 'S:' + str (S)
        if (F > 0):
            if (S > 0):
                response += '  '
            response += 'F:' + str (F)
        response += ']'
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        return
    response = f"[roll @{username}] usage: /r or /r <# of d10s> or /r <characteristic> <skill>"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    return    

def probability_handler(update, context):
    username = update.message.from_user.first_name
    response = ""
    if len (context.args) != 2 or not context.args[0].isdigit() or not context.args[1].isdigit():
        response =  f"[probability @{username}] usage: /p <characteristic> <skill>"
    else:
        response = probability (int(context.args[0]), int(context.args[1]))
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def skill_handler(update, context):
    username = update.message.from_user.first_name
    response = ""
    if len (context.args) == 0 or not context.args[0].isdigit():
        response = "skill usage: /s <skill>\r\n\t\twhere <skill> is your skill + any modifiers"
    else:
        response = skill (int(context.args[0]), username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def multiskill_handler(update, context):
    username = update.message.from_user.first_name
    response = ""
    if len (context.args) != 2 or not context.args[0].isdigit() or not context.args[1].isdigit():
        response = "multiskill usage: /sm <skill> <count> \r\n\t\twhere <skill> is your skill + any modifiers and <count> is the number of attempts to make"
    else:
        response = multiskill (int(context.args[0]), username, int(context.args[1]))
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
    dp.add_handler(CommandHandler(["h", "help"], help))
    dp.add_handler(CommandHandler(["a","attack"], attack_handler))
    dp.add_handler(CommandHandler(["d","defend"], defend_handler))
    dp.add_handler(CommandHandler(["r","roll"], roll_handler))
    dp.add_handler(CommandHandler(["s","skill"], skill_handler))
    dp.add_handler(CommandHandler(["p","probability"], probability_handler))
    dp.add_handler(CommandHandler(["sm","multiskill"], multiskill_handler))
    dp.add_handler(CommandHandler(["o","oops"], oops_handler))
    dp.add_handler(CommandHandler(["w","winds"], winds_handler))

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