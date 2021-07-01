#  AirBnB Clone Project

<p align="center">
    <img src="https://www.holbertonschool.com/holberton-logo.png"/>
</p>

`AirBnb_Clone` project from Holberton School, it's a project to implement the console which will be the command interpreter. The project has been done in python language. The present project is the first part of the AirBnB clone.

# Description

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

# How to compile
After cloning the repository, we will use chmod to add permissions.

```
chmod 775 console.py
```
Just because it has been written on python language the compile process is easier than you can imagine

```
./console.py
```
### How to use

 - Run the console.py file: `./console.py`
 - Use the commands `EOF` `quit` `help` `create` `show` `destroy` `update` `all`

## Features
- [ ] `EOF` | exit the program 
- [ ] `quit` | exit the program
- [ ]  `help` | Shows help as documentation
- [ ] `create` | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id 
- [ ] `show` | Prints the string representation of an instance based on the class name and id
- [ ] `destroy` | Deletes an instance based on the class name and id
- [ ] `all` | Prints all string representation of all instances based or not on the class name
- [ ] `update` | Updates an instance based on the class name and id by adding or updating attribute


## AUTHORS
* Jerson Perez
* Gerson Soto
