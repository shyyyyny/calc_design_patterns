from app.commands import Command

class SubtractCommand(Command):
    def execute(self, args):
        result = float(args[0]) - float(args[1]) if len(args) == 2 else "Invalid number of arguments for 'subtract' command."
        print(f"Result: {result}")
