from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        available_commands = self.command_handler.commands.keys()
        formatted_commands = (f"- {command}" for command in available_commands)
        print("Available Commands:\n" + "\n".join(formatted_commands))
