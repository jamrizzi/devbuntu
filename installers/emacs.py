import os
import sys

def read(message):
    if sys.version_info[0] < 3: # python 2
        return raw_input(message)
    else: # python 3
        return input(message)

def question(message, defaultAnswer = 'y'):
    if defaultAnswer.lower() == 'y':
        response = True
        answer = read(message + ' [Y|n]: ')
        if len(answer) > 0 and answer[0].lower() == 'n':
            response = False
    else:
        response = False
        answer = read(message + ' [y|N]: ')
        if len(answer) > 0 and answer[0].lower() == 'y':
            response = True
    return response

if os.getuid() == 0:
    os.system('''
        apt-get install -y emacs
    ''')

else:
    print 'This program must be run as root'
    exit()