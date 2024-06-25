class Style:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_color(text, color, postfix='\n'):
        color_code = getattr(Style, color.upper(), Style.RESET)
        print(f"{Style.BOLD}{color_code}{text}{Style.RESET}", end=postfix)
