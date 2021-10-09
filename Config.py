from enum import Enum

START_MONEY = 1500
SALARY = 1500
MAX_TURN = 100

class BoardColor(Enum):
    BG = "\x1b[6;37;40m"
    END ='\x1b[0m'        # reset
    P1 = '\x1b[6;31;40m'
    P2 = '\x1b[6;32;40m'
    P3 = '\x1b[6;33;40m'
    P4 = '\x1b[6;34;40m'
    P5 = '\x1b[6;35;40m'
    P6 = '\x1b[6;36;40m'

