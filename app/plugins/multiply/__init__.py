from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, args):
        result = float(args[0]) * float(args[1]) if len(args) == 2 else "Invalid number of arguments for 'multiply' command."
        print(f"Result: {result}")