# BigBlueButton-float_chat
This is a selenium based python application which is used to make the chat box in the Big Blue Button, an online classroom, a floating chat box.

This is achieved by opening the Chat site using Selenuim browser automation and capturing the chat details using their respective xpath. The captured details is then displayed on tkinter window which always stays on top.

Float chat options can be toggled using main menu which opens when the float_chat.py script is executed.

<b>Note:</b>
* Current version only support Chrome browser
* Chat window must be made visible in the webpage in order to capture the data
* The layout of the browser must not be changed as it my change the xpath of the elements

## Getting started
1) Cloning the repository
```commandline
git clone https://github.com/dheena2k2/BigBlueButton-float_chat.git
cd BigBlueButton-float_chat
```
2) Check your Chrome browser version by typing 'chrome://version/' in the address bar and download the respective chrome driver from [here](https://chromedriver.chromium.org/downloads) and make sure to convert it into executable using 'chmod' command if you are using linux.
3) Place the executable of the chrome driver in 'data/drivers/' directory
4) Create 'data/base_data.xml' file using 'data/base_data_template.xml'
5) Install pipenv if not already installed
```commandline
pip install pipenv
```
6) Switch to the main directory (i.e. directory of BigBlueButton-float_chat). Install necessary packages and activate pipenv shell
```commandline
pipenv install
pipenv shell
```

## Running the main script
Switch to float_chat directory and run the float_chat.py script (make sure pipenv shell is active)
```commandline
cd float_chat/
python float_chat.py
```
