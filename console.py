#!/usr/bin/python3
""" This module defines the class HBNBCommand as a console """
import cmd

class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand is a console

    public properties:
        prompt: custom promt
    """

    prompt ="(hbnb)"

    def do_EOF(self, line):
        """(ctrl+d) or ($ EOF): Exits the console """
        return True

    def do_quit(self, line):
        """($ quit): Exits the console """
        return True

    def emptyline(self):
        """does nothing"""
        pass

    def do_q(self, line):
        """($ q): Exits the console """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
