# COUNTDOWN TIMER

import time


def counttime(usertime):
    while usertime:
        mins, sec = divmod(usertime, 60)
        time.sleep(1)
        print('{:02d} : {:02d}' .format(mins, sec))
        usertime = usertime-1
    print('Time Is finised')


usertime = int(input('Enter Second:'))
counttime(usertime)
