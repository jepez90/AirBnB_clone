#  AirBnB Clone Project

<p align="center">
    <img src="https://www.holbertonschool.com/holberton-logo.png"/>
</p>

`AirBnb_Clone` project from Holberton School, it's a project to implement the console which will be the command interpreter. The project has been done in python language. The present project is the first part of the AirBnB clone.

## Description

Will do the next task, just as it is propused: create the data model, manage the data: create, update, destroy, read objects via the console (command interpreter), finally, store and persist objects to a file JSON file

## First steps

You can get a copy of the project, cloning from the repository with:
```
https://github.com/Gdsoto/AirBnB_clone.git
```

## Developed with
- Programming languaje: Python
- Editor: Vim / Emacs

## File Structure
These are the files with the custom funtions and system calls, each one contains a brief description:

|   ***File***    |  ***Description***                   |
|---------------|---------------------------------------|
|  [`/models`]	|  folder containing the classes	|
|  [`/tests`]	|  folder containing the unity tests	|
|  [`console.py`] | console launcher |

## How to compile
After cloning the repository, we will use chmod to add permissions.

```
chmod 775 console.py
```
Just because it has been written on python language the compile process is easier than you can imagine

```
./console.py
```
## How to use

 - Run the console.py file: `./console.py`
 - Use the commands `EOF`, `quit`, `help`, `create`, `show`, `destroy`, `update`, `all` to handle the classes `BaseModel`,         `User`, `Place`, `State`, `City`, `Amenity`, `Review`
```shell
$ ./console.py
(hbnb) ?

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

Miscellaneous help topics:
==========================
class_name

(hbnb) create User
b782ff6c-5420-4a88-b172-2565247f4fc1
(hbnb) User.show('b782ff6c-5420-4a88-b172-2565247f4fc1')
[User] (b782ff6c-5420-4a88-b172-2565247f4fc1) {'id': 'b782ff6c-5420-4a88-b172-2565247f4fc1', 'created_at': datetime.datetime(2021, 7, 1, 12, 7, 12, 237730), ...}
(hbnb) User.
User.all      User.count    User.destroy  User.show     User.update
(hbnb) User.destroy('b782ff6c-5420-4a88-b172-2565247f4fc1')
(hbnb) User.show('b782ff6c-5420-4a88-b172-2565247f4fc1')
** no instance found **
(hbnb) City.update('e78bcbfd-13cb-4e05-9621-411f085882e5', 'first_name', 'Jerson')
(hbnb) quit
$
```

## Features
- [x] `EOF` | exit the program 
- [x] `quit` | exit the program
- [x]  `help` | Shows help as documentation
- [x] `create <Class name>` | Creates a new instance of _\<Class name>_, saves it (to the JSON file) and prints the _id_.
- [x] `show <Class name> <id>` | Prints the string representation of an instance based on the _\<Class name>_ and _id_
- [x] `destroy <Class name> <id>` | Deletes an instance based on the _\<Class name>_ and _id_
- [x] `all [<Class name>]` | Prints all string representation of all instances based or not on the _\<Class name>_
- [x] `update <Class name> <id> <attribute name> <attribute value>` | Updates an instance based on the _\<Class name>_ and _id_ by adding or updating an specific attribute
- [x] `<Class name>.<command>([<args>])`
    - `<Class name>.all()` | shows all instances of the class
    - `<Class name>.count()` | shows the number of instances of ther class
    - `<Class name>.show(<id>)` | shows the instance of the class with the specific **id**
    - `<Class name>.destroy(<id>)` | removes the instance of the class with the specific **id**
    - `<Class name>.update(<id>, <attribute name>, <attribute value>)` | Updates the instance of the class name with the specific **id** by adding or updating an specific attribute
    - `<Class name>.update(<id>, {<attribute name>: <attribute value>, ...})` | Updates the instance of the class name with the specific **id** by adding or updating attributes gived as dictionary
- [x] use `<tab>` key for autocomplete the classnames and commands


## AUTHORS
* Jerson Perez
* Gerson Soto
