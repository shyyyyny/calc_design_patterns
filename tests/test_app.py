import pytest
from app import App

def test_app_exit_command(capfd, monkeypatch):
    """Test that the application exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_unknown_command(capfd, monkeypatch):
    """Test how the application handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_app_no_input(capfd, monkeypatch):
    """Test how the application handles no input before exiting."""
    # Simulate user entering no input followed by 'exit'
    inputs = iter(['', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Verify that the application prompts for a command
    captured = capfd.readouterr()
    expected_output = """Type 'exit' to exit.
Please enter a command.
"""
    assert captured.out.strip() == expected_output.strip()

def test_app_menu_command(capfd, monkeypatch):
    """Test how the application handles the 'menu' command."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Verify that the 'menu' command displays available commands
    captured = capfd.readouterr()
    expected_output = """
   Type 'exit' to exit.
Available Commands:
- greet
- subtract
- multiply
- divide
- add
- goodbye
- menu
- exit
"""
    assert captured.out.strip() == expected_output.strip()