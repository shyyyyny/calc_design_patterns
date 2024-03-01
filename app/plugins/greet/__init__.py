from app.commands import Command

class GreetCommand(Command):
    def execute(self, *args, **kwargs):
        print(f"{kwargs.get('greeting', 'Hello')}, {args[0] if args else 'World'}!")