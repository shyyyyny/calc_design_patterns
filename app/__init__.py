import os
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self._load_commands()

    def _load_commands(self):
        command_dir = "app/plugins" 
        for subdir in os.listdir(command_dir):
            subdir_path = os.path.join(command_dir, subdir)
            if os.path.isdir(subdir_path):
                # try:
                    if subdir.lower() == "menu":
                        command_instance = MenuCommand(self.command_handler)
                    else:
                        module_name = f"app.plugins.{subdir}.__init__"
                        command_class_name = getattr(__import__(module_name, fromlist=[f"{subdir.capitalize()}Command"]), f"{subdir.capitalize()}Command")
                        command_instance = command_class_name()
                    self.command_handler.register_command(subdir, command_instance)
                # except Exception:
                #     pass

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            if not user_input:
                print("Please enter a command.")
                continue
            command_name = user_input[0].lower()
            args = user_input[1:]
            self.command_handler.execute_command(command_name, args)