# HACK: This is to get autocomplete while working w/ commands, when running these imports aren't included (since it
# would be a cyclical import) so we're good. REAL annoying python 3 thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from client import ClientThread
    from server import MUDServer


class BaseCommand(object):
    """
    Base command object that all other commands must inherit
    """
    commands: list
    help_text: str

    @staticmethod
    def handle(args: list, client: 'ClientThread', server: 'MUDServer'):
        """
        Method that's called to handle the command when it matches the message from the client. Must implement in each
        child object
        """
        raise NotImplementedError(f"Command not implemented, DUMMY")

    @staticmethod
    def help(args: list, client):
        """
        Method that's called when help is requested for the command. Implement if desired
        """
        user_input = " ".join(args)
        client.send(
            f"We can't help you with that. Probably because we're too lazy to explain whatever {{yellow}}{user_input}"
            f"{{normal}} is. Or it's not a real command. I could find out which case it is, but again, I'm just too "
            f"lazy to care either way..."
        )
