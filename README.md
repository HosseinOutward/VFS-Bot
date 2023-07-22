# VFS version 2 (new site)
for VFS Global v2, contact me. This code is for VFS v1

# VFS Appointment Bot v1
This Python script automatically checks available VFS appointments and notifies the earliest opening via Telegram.

### Logging
All logged Messages will be sent in the conversation where you initiate the `/start` command.
It can be yours or a chat group where you added the bot.
This way you and other people can track the journey of the robot and command the bot on telegram.

Important messages, as few as possible, such as when the appointment appears and is available, and rarely errors, are sent to the `channel_id` where you can also add friends to be warned.

## Dependencies
See `requirements.txt` for Python packages
System library `tesseract` is needed.

## How to use
1. Clone the repo.
2. Install the dependencies. 
3. Create a Telegram bot using [BotFather](https://t.me/BotFather) and save the auth token.
4. Make a Telegram channel to notify the appointment updates. 
5. Use [@username_to_id_bot](https://t.me/username_to_id_bot) or [@myidbot](https://t.me/myidbot) to find the channel id and your own account id.
7. Copy the config.ini.dist as config.ini and fill in the fields.
8. Edit the ajaxRequest.js file to match your visa center locations parameters.
9. Run the script and /start the bot from telegram !

### Captcha
It uses OpenCV along with Tesseract to recognize the captcha.
It can be low, sometimes it takes 10-15 tries, but it works (and for free !).

### Telegram
Add the created bot in the channel you want to post updates to.
Make sure to specify your account id (or several accounts) as admin_ids in the config.ini, it prevents others from using the bot, which might cause unexpected behaivor.

### Help
Here are the bot commands to use from telegram :
- `/help`: Prints the help message.
- `/start`: Starts the bot.
- `/quit`: Stops the bot. (It can be started again using /start as long as the Python script is running.)
- `/check`: Ask for a new spontaneous appointment check

VFSBot.py command as an optionn `--no-headless` for testing and debugging purpose.
It actually opens the chrome browser and you can visually follow every actions.

## Development
Feel free to improve this version by submitting a pull request.

As VFS appointments cause problems all over the world and with so many different websites, we could handle them all.
