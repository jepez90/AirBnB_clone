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
        if self.is_correct_class_name(args):
            class_name = args[0]

            """get a reference to the class class_name"""
            class_reference = self.classes[class_name]

            """Create the instance of the class stored in class_reference"""
            class_instance = class_reference()
            class_instance.save()
            print(class_instance.id)

    def do_show(self, line):
        """($ show <classname> <id>): Prints the string representation of
        an instance based on the class name and id
        """
        args = line.split()
        if self.is_correct_class_name(args):
            instance_id = get_id(args)
            if instance_id:
                print(storage.all().get(instance_id))

    def do_destroy(self, line):
        """($ destroy <classname> <id>): Deletes an instance based on the class
        name and id
        """
        args = line.split()
        if self.is_correct_class_name(args):
            instance_id = get_id(args)
            if instance_id:
                del(storage.all()[instance_id])
                storage.save()

    def do_all(self, line):
        """($ all [<classname>]):Prints all string representation of all
        instances based or not on the class name
        """
        args = line.split()
        dictionaries = []
        if len(args) == 0:
            """if doesn't given class name, show all instances"""
            for key, instance in storage.all().items():
                dictionaries.append(instance.__str__())

        elif self.is_correct_class_name(args):
            """if was given a class name, show only instances of this class"""

            for key, instance in storage.all().items():
                class_of_instance = instance.__class__.__name__
                if class_of_instance == args[0]:
                    dictionaries.append(instance.__str__())
        else:
            """if class name was given but it doen't exist"""
            return

        print(dictionaries)

    def do_update(self, line):
        """($ update <class name> <id> <attribute name> "<attribute value>"):
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        args = line.split()
        if self.is_correct_class_name(args):
            instance_id = get_id(args)
            if instance_id and is_valid_attribute(args):
                attribute_name = args[2]
                instance = storage.all().get(instance_id)

                prev_attr = getattr(instance, attribute_name)
                type_attr = type(prev_attr)

                setattr(instance, attribute_name, type_attr(args[3]))
                instance.save()

    def default(self, line):
        """Method called on an input line when the command prefixis not
        recognized
        """
        # checs for the correct format of the line
        class_name, command, args = self.split_by_class_name(line)
        if class_name is None:
            super().default(line)
            return
        elif command is None:
            error_msg = "** unknown comand {} for clase {} **"
            print(error_msg.format(command, class_name))
            return

        if command == 'all':
            self.do_all(class_name)

        elif command == 'count':
            counter = 0
            for instance in storage.all().values():
                if instance.__class__.__name__ == class_name:
                    counter += 1
            print(counter)

        elif command == 'show':
            self.do_show(class_name + ' ' + args[0])

        elif command == 'destroy':
            self.do_destroy(class_name + ' ' + args[0])

        elif command == 'update':
            if len(args) == 1:
                self.do_update(class_name + ' ' + args[0])
            else:
                print("aun no actualizo con diccionarios")

        else:
            print("unhandle command")

    def do_EOF(self, line):
        """(ctrl+d) or ($ EOF): Exits the console """
        return True

    def do_quit(self, line):
        """($ quit): Exits the console """
        return True

    def help_classname(self):
        """ Show help string for <class name>.<command> options"""
        print("<ClassName>.<function>: can invoke the nexts classnames\n\
        [BaseModel, User]\n\
        with the follows actions\n\
        .show(): shows all instances of ClassName class\n")

    def completenames(self, text, *ignored):
        """ get the list of words to autocomplete """
        # call the parent method to the default list
        names = super().completenames(text, *ignored)

        if text.find('.') != -1:
            # ads the command after the class name e: User.a->User.all
            text_copy = text.split('.')
            if text_copy[0] in self.classes.keys():
                for word in ['all', 'count', 'show', 'destroy', 'update']:
                    if word.lower().startswith(text_copy[1].lower()):
                        names.append('{}.{}'.format(text_copy[0], word))
        else:
            # add the classes as commands to autocomplete
            for word in self.classes.keys():
                if word.lower().startswith(text.lower()):
                    names.append(word)
        return names

    def emptyline(self):
        """does nothing"""
        pass

    def preloop(self):
        """before to start the loop, load the classnames and rreferences"""
        from models.base_model import BaseModel
        from models.user import User
        self.classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": BaseModel,
            "State": BaseModel,
            "City": BaseModel,
            "Amenity": BaseModel,
            "Review": BaseModel
        }

    def is_correct_class_name(self, args):
        """ check if the classname was given as argument and exists
        return False on error or True
        """

        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return False
        else:
            return True

    def split_by_class_name(self, line):
        """splits the line when style Classname.command is used"""
        # gets the class name
        line = line.strip()
        line_split = line.split('.')
        class_name = line_split[0]
        if class_name not in self.classes.keys() or len(line_split) != 2:
            return None, None, None

        # gets the command_name
        line_split = line_split[1]
        index_to_split = line_split.find('(')

        if (index_to_split == -1):
            return None, None, None

        command = line_split[:index_to_split]
        if command not in ['all', 'count', 'show', 'destroy', 'update']:
            return class_name, None, None

        # gets the args of teh function
        args = []
        args.append(line_split[index_to_split + 1: -1])
        """line_split = line_split.split(',')
        args = []
        for arg in line_split:
            arg = arg.strip()
            args.append(arg)"""

        return class_name, command, args


def get_id(args):
    """ return the id in the correct format when it exists
    in the stored objects
    """
    if len(args) == 1:
        print("** instance id missing **")
        return None

    instance_id = "{}.{}".format(args[0], args[1])
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
