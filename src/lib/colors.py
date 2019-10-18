from lib.log import log

COLOR_MAP = {
    "blue": "\u001b[34m",
    "bright_black": "\u001b[30;1m",
    "bright_blue": "\u001b[34;1m",
    "bright_green": "\u001b[32;1m",
    "bright_magenta": "\u001b[35;1m",
    "bright_red": "\u001b[31;1m",
    "green": "\u001b[32;2m",
    "magenta": "\u001b[35;2m",
    "normal": "\u001b[0m",
    "red": "\u001b[31m",
    "yellow": "\u001b[33;1m"
}


def colorize(message: str):
    """
    Returns the correctly colorized message based on the known color codes
    """
    if not message.endswith("{normal}"):
        message = message + "{normal}"
    try:
        return message.format(**COLOR_MAP)
    except Exception as e:
        log(e)
        return message
