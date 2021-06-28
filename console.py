#!/usr/bin/python3
""" This module defines the class HBNBCommand as a console """
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand is a console
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
            instance_id = get_id(args)
            if instance_id:
                print(storage.all().get(instance_id))

    def do_destroy(self, line):
        """($ destroy <classname> <id>): Deletes an instance based on the class
        name and id
        """
        args = line.split()
        if is_correct_class_name(args):
            instance_id = get_id(args)
            if instance_id:
                del(storage.all()[instance_id])
                storage.save()

    def do_all(self, line):
        """($ all [<classname>]):Prints all string representation of all
        instances based or not on the class name
        """
        args = line.split()
        if len(args) == 0 or is_correct_class_name(args):
            dictionaries = []
            for key, instance in storage.all().items():
                dictionaries.append(instance.to_dict())
            print(dictionaries)

    def do_update(self, line):
        """($ update <class name> <id> <attribute name> "<attribute value>"):
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        args = line.split()
        if is_correct_class_name(args):
            instance_id = get_id(args)
            if instance_id and is_valid_attribute(args):
                attribute_name = args[2]
                instance = storage.all().get(instance_id)

                prev_attr = getattr(instance, attribute_name)
                type_attr = type(prev_attr)

                setattr(instance, attribute_name, type_attr(args[3]))
                instance.save()

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

    instance_id = "BaseModel." + args[1]
    if instance_id in storage.all().keys():
        return instance_id
    else:
        print("** no instance found **")


def is_valid_attribute(args):
    """ check if exist and the correct format for the attributes
    """
    if len(args) == 2:
        """If the attribute name is missing, print ** attribute name missing **
        (ex: $ update BaseModel existing-id)"""
        print("** attribute name missing **")
        return False
    elif len(args) == 3:
        """If the value for the attribute name doesn’t exist, print
        ** value missing ** (ex: $ update BaseModel existing-id first_name)"""
        print("** value missing **")
        return False
    elif args[3] in ['id', 'created_at', 'created_at']:
        return False
    else:
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
