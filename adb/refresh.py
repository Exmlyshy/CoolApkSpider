import os
import time
from datetime import datetime


def main():

    tap_times = 0
    for i in range(10):
        p = os.popen('adb connect 127.0.0.1:21503')
        out = p.read()
        print(datetime.fromtimestamp(int(time.time())), out)
        if 'unable' in out:
            time.sleep(1)
            continue
        while True:
            os.system('adb shell input tap 360 800')
            tap_times += 1
            print('%s refresh %s times' %
                  (datetime.fromtimestamp(int(time.time())), tap_times))
            time.sleep(40)
    pid = os.getpid()
    os.kill(pid, 1)


if __name__ == '__main__':
    main()
