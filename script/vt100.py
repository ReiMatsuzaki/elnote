"""
Controll standard output color.
See https://qiita.com/ironguy/items/8fb3ddadb3c4c986496d.
"""

END = '\033[0m'

BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
INVISIBLE = '\033[8m'
STRIKETHROUGH = '\033[9m'

class fg:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    DEFAULT = '\033[39m'

class bg:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    DEFAULT = '\033[49m'

    
