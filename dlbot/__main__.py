#!/usr/bin/env python
import sys
import os

if __name__ == '__main__':
    ROOT_PATH = os.path.abspath(os.path.join(os.path.split(sys.argv[0])[0], '..'))
    print(ROOT_PATH)
    sys.path.append(ROOT_PATH)
    from dlbot.dlbot import app
    app.run()
    