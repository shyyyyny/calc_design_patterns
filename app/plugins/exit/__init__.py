import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, *args, **kwargs):
        exit_message = "Terminating..." if args else "Terminating..."
        exit_code = kwargs.get('exit_code', 0)
        sys.exit(f"{exit_message}\nCode: {exit_code}")
