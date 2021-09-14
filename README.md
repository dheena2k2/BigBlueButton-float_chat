# BigBlueButton-float_chat
This is a selenium based python application which is used to make the chat box in the Big Blue Button, an online classroom, a floating chat box.

This is achieved by opening the Chat site using Selenuim browser automation and capturing the chat details using their respective xpath. The captured details is then displayed on tkinter window which always stays on top.

Float chat options can be toggled using main menu which opens when the float_chat.py script is executed.

<b>Note:</b> Current version only support Chrome browser.

## Getting started
1) Download the respective chrome driver from [here](https://chromedriver.chromium.org/downloads) and make sure to convert it into executable using 'chmod' command if you are using linux. Chrome browser version can be checked by typing 'chrome://version/' in the address bar of the chrome browser
2) Place the executable of the chrome driver in 'data/drivers/' directory
3) Create 'data/base_data.xml' file using 'data/base_data_template.xml'
4) Install pipenv if not already installed
```commandline
$ pip install pipenv
```
5) Switch to the main directory (i.e. directory of BigBlueButton-float_chat). Activate pipenv shell and install necessary packages
```commandline
$ pipenv shell
$ pipenv install
```

## Running the main script
Switch to float_chat directory and run the float_chat.py script (make sure pipenv shell is active)
```commandline
$ cd float_chat/
$ python float_chat.py
```
