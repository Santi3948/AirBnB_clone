#!/usr/bin/python3
"""console module doc"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            if arg == "BaseModel":
                var = eval(f'{arg}()')
                var.save()
                print(f'{var.id}')
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        var = arg.split(" ")
        if len(var) == 1 and var[0] == '':
            print("** class name missing **")
        else:
            if var[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(var) == 1:
                print("** instance id missing **")
            else:
                my_dict = storage.all()
                for obj in my_dict:
                    var2 = obj.split(".")
                    if var2[1] == var[1]:
                        print(f'{my_dict[obj]}')
                        return
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        var = arg.split(" ")
        if len(var) == 1 and var[0] == '':
            print("** class name missing **")
        else:
            if var[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(var) == 1:
                print("** instance id missing **")
            else:
                my_dict = storage.all()
                for obj in my_dict:
                    var2 = obj.split(".")
                    if var2[1] == var[1]:
                        my_dict.pop(obj)
                        return
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        lis = []
        if arg:
            if arg != "BaseModel":
                print("** class doesn't exist **")
            else:
                my_dict = storage.all()
                for obj in my_dict:
                    var2 = obj.split(".")
                    if var2[0] == arg:
                        lis.append(str(my_dict[obj]))
                    print(f'{lis}')
        else:
            my_dict = storage.all()
            for obj in my_dict:
                lis.append(str(my_dict[obj]))
            print(f'{lis}')

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        spl = arg.split(" ")
        if len(spl) == 1 and spl[0] == '':
            print("** class name missing **")
        else:
            if spl[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(spl) == 1:
                print("** instance id missing **")
            else:
                flag = 0
                my_dict = storage.all()
                for obj in my_dict:
                    var2 = obj.split(".")
                    if var2[1] == spl[1]:
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
                elif len(spl) == 2:
                    print("** attribute name missing **")
                elif len(spl) == 3:
                    print("** value missing **")
                else:
                    setattr(my_dict[obj], spl[2], spl[3])

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        self.close()
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        self.close()
        return True

    def close(self):
        """Quit command to exit the program"""
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        """checks if there's no input for the prompt"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
