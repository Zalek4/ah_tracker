import cmd
import json
import os

tracker_project = None

class ProjectCLI(cmd.Cmd):
    prompt = ":> "
    intro = "\nType 'help' for available project commands.\n"

    def do_create(self, line):
        """file path(str), project name(str) - Creates a project JSON file at the entered directory."""

        # Parse the arguments into a string and a float value.
        path, name = [str(s) for s in line.split()]
        name = f"{name}.json"
        path = os.path.join(path, name)
        data = {}

        # Store the JSON data in a file
        with open(path, "w") as file:
            json.dump(data, file)

        # Write the project name and directory to a json stored in the user documents directory.

    def do_set(self, args):
        """file path(str) - Sets the active project."""

    def do_list(self, line):
        """Lists all available projects."""
        # Read our user json if it exists and list all the available projects.
        return True

    def do_entry(self, line):
        """category(str), value(float) - Adds a data point to a category."""

        # Parse the arguments into a string and a float value.
        category, value = [str(s) for s in line.split()]
        float(value)

        # Check to see if the category exists already.

        # Create the category if it doesn't exits.

        # Add our data entry to the category in the json.

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