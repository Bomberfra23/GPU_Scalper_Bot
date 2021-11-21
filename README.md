<img src="Source/GPU_Scalper_Bot_ASCII.png">


Please star my repo if helped you! Thanks!

Please Join [Support & FAQ Telegram Group](https://t.me/HwGroupTech) if you have any questions about this software.

# FREE Add-To-Cart Bot for upon 10 stores GPU/PS5/Xbox

## Description
GPU Scalper Bot Alpha, is an automatic add to cart, remote alert and check product availability completely free Bot. It can scrape various gpu and informatic stores, check if a product is available or not, add to cart it automatically and send you a status notification via Telegram Bot. It works on Chrome and on every device that has Python installed so Windows 7/8/10/11, MacOS, Linux Distro.

## Chrome Browser Configuration
In order to work, this bot must collaborate with Chrome WebDriver that is an open source tool for automated testing of webapps across Google Chrome Browser.
#### Download Chrome Webdriver
<img src="Source/webdriver_download.png">

1. Download it at this [link](https://chromedriver.chromium.org/downloads)
2. Place it in a directory (example, C:\Program Files (x86)\chromedriver.exe)
3. Enter the path in the <b>script_settings</b> file in <b>Chromedriver_path</b>
## Get Started with the bot
Now we are ready to start the script, let's see how to do it
#### requirements

1. Python 3.6 or superior installed on your MacOS, Windows or Linux machine
2. Python PIP installed
3. (optional) an IDE like PyCharm for modify Py files
#### Bot Files
<img src="Source/main_files.png">
This Pyhton Software is composed by 6 files:

1. <b>main.Py</b> which is the main file to run to get evrything started
2. <b>GUI.Py</b> which is the file responsible for the graphical interface
3. <b>script_functions.Py</b> which is the "engine" file of the software
4. <b>script_settings.Py</b> which is the file that we have to modify for change settings like alert filters ecc
5. <b>requirements.txt</b> which is a TXT file that tells automatically to Python PIP what packages install (Windows, Linux, MacOS)
6. <b>Windows_Installer.Bat</b> which is a BAT file that install automatically all the requirements of the bot if you run it (only Windows)

#### install packages
Windows, Linux, MacOS
1. after installing Python PIP on your machine, open Terminal or CMD
2. with the cd command, enter on the GPU Scalper Bot folder
3. write the command as below to install all the packages
<img src="Source/bot_requirements.png">

Only Windows

1. simply open the GPU Scalper Bot folder and double click on the BAT file

#### run main file and the home

<img src="Source/first_run.png">

1. run the <b>main.Py</b> file as shown to start the software 

<img src="Source/bot_home.png">

This is the main home of the bot where you can choose which shop to point to, visit our Telegram Group or Exit!

#### change settings

<img src="Source/settings_guide.png">

When your first open the <b>script_settings.Py</b> file, you find this four entries

1) <b>Chromedriver_path</b> where you have to insert the location of the <b>chromedriver.exe</b> file
2) <b>telegram_bot_token</b> where you have to insert you telegram bot Token after have create it with [BotFather](https://t.me/botfather)
3) <b>telegram_chat_id</b> where you have to insert your personal Telegram chat id that you can take from [here](https://t.me/chatIDrobot)
4) <b>telegram_alert_status</b> that enable or disable the Telegram Alert Notifications entering True or False

