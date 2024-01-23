import cmd
import os

tracker_project = None

class ProjectCLI(cmd.Cmd):
    prompt = ":> "
    intro = "\nType 'help' for available project commands.\n"

    def do_create(self, args):
        """file path(str) - Creates a project JSON file at the entered directory."""

    def do_set(self, args):
        """file path(str) - Sets the active project."""

    def do_entry(self, line):
        """category(str), value(float) - Adds a data point to a category."""
        category, value = [str(s) for s in line.split()]
        float(value)
        print(f"{category}")
        print(f"{value}")

    def do_return(self, line):
        """Returns to the main Tracker CLI."""
        return True

class TrackerCLI(cmd.Cmd):
    # Define our CLI prompt symbol, and send an intro message.
    prompt = ": "
    intro = "Hello! Type 'help' for available commands."

    def do_project(self, line):
        """Enters the 'Project' CLI"""
        ProjectCLI().cmdloop()

    def do_exit(self, line):
        """Exit the CLI."""
        return True

if __name__ == "__main__":
    TrackerCLI().cmdloop()