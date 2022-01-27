# ProjectGreenPants
Dice Rolling Bot for playing Warhammer Fantasy Role Playing 4th Ed (https://www.cubicle7games.com/our-games/warhammer-fantasy-roleplay/)


<a brief but clear understanding of why someone should be interested>
Want to play Warhammer fantasy RPG with remote friends in a telegram chat?
For example, you can attack, defend, use a skill etc…


<how do I set this up>
It's free to run your own bot for your games.  Only one person needs to setup the bot and everyone else just needs a telegram account and a private telegram chat with the bot and all members.
This will be simple to setup just following the directions below:

all users:
	- install telegram
	- create/join private group chat

one user:

	1. install telegram:
https://desktop.telegram.org/
(this also works on all mobile devices, pcs, tables that support telegram)

	2. create a private bot and a token by going here (takes 2 minutes or less):
	https://core.telegram.org/bots#6-botfather
	this will create and return a token in 2 minutes or less:  110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw  <- SAMPLE TOKEN
	DO NOT SHARE YOUR PRIVATE TOKEN WITH ANYONE
	Save the bots name somewhere so you don't forget it (just write it down for now)

	(background info on telegram bots: https://core.telegram.org/bots)


	3. install python 3: https://www.python.org/downloads/

	
	Choose Install Now option.
	Check box to Add Python 3.xx to PATH
	
	4. install python-telegram-bot package
	Open windows command prompt (type "CMD" into windows taskbar search)
	From command prompt type "pip install python-telegram-bot"

	5. Create an environment variable
	From command prompt type "setx GPR_BOT_TOKEN <YOUR TOKEN HERE>"
	Example: "setx GPR_BOT_TOKEN 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw"
	Note: there is a space after GPR_BOT_TOKEN

	6. Download the app
	Go to the following url: https://github.com/jjbutler52/ProjectGreenPants
	
	
