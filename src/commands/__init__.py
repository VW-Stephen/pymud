class BaseCommand(object):
    """
    Base command object that all other commands must inherit
    """
    commands: list
    help_text: str

    @staticmethod
    def handle(args, client, server):
        """
        Method that's called to handle the command when it matches the message from the client. Must implement in each
        child object
        """
        raise NotImplementedError(f"Command not implemented, DUMMY")
