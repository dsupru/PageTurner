# Why ?
Having a cup of tea with a book and feeling annoyed you have to put the tea down to turn the page?
Say no more!

This repo allows you to do just that - keep reading your book, viewing your pictures, .. , doing anything it is you're doing if you need to click left/right, I got you!

# But how does it work ?
At it's core this uses MediaPipe framework for hand gesture recognition and pyautogui library to issue keystroke signals.

Pyautogui is used to control the system and MediaPipe is used to control detection. When it detects a certain gesture, it calls the handler that either turns one page forward or backward. Pointing up - YAY, you're done with the page! The handler will go one page forward. Index finger up - Hold on, I need to go back! The handler will go one page backward.

# Installing Dependencies
Please run ```pip install -r Requirements.txt``` to install the required version of dependencies.

# Running
Run ```python3 pageTurner.py``` in terminal to run the application.
