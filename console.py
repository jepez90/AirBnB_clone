#!/usr/bin/python3
""" This module defines the class HBNBCommand as a console """
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand is a console

    Attributes:
        prompt: custom prompt
    """

    prompt = "(hbnb)"

    def do_create(self, line):
        """($ create <classname>): Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = line.split()
        if is_correct_class_name(args):
            from models.base_model import BaseModel
            base_model_instance = BaseModel()
            base_model_instance.save()
            print(base_model_instance.id)

    def do_show(self, line):
        """($ show <classname> <id>): Prints the string representation of
        an instance based on the class name and id
        """
        args = line.split()
        if is_correct_class_name(args):
            id = get_id(args)
            if id:
                print(storage.all().get(id))

    def do_destroy(self, line):
        """($ destroy <classname> <id>): Deletes an instance based on the class
        name and id
        """
        args = line.split()
        if is_correct_class_name(args):
            id = get_id(args)
            if id:
                del(storage.all()[id])
                storage.save()

    def do_all(self, line):
        """($ all [<classname>]):Prints all string representation of all
        instances based or not on the class name
        """
        args = line.split()
        if len(args) == 0 or is_correct_class_name(args):
            dictionaries = []
            for key, obj in storage.all().items():
                dictionaries.append(obj.to_dict())
            print(dictionaries)

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


def is_correct_class_name(args):
    """ check if the classname was given as argument and exists
    return False on error or True
    """
    handle_classes_list = ["BaseModel"]

    if len(args) == 0:
        print("** class name missing **")
        return False
    elif args[0] not in handle_classes_list:
        print("** class doesn't exist **")
        return False
    else:
        return True


def get_id(args):
    """ return the id in the correct format when it exists
    in the stored objects
    """
    if len(args) == 1:
        print("** instance id missing **")
        return None

    id = "BaseModel." + args[1]
    if id in storage.all().keys():
        return id
    else:
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
