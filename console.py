#!/usr/bin/python3
"""console module doc"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    file = None
    ClassList = ["BaseModel", "Place", "State", "City", "\
Amenity", "Review", "User"]

    def do_create(self, arg):
        """creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            if arg in self.ClassList:
                var = eval("{}()".format(arg))
                var.save()
                print("{}".format(var.id))
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        var = arg.split(" ")
        if len(var) == 1 and var[0] == '':
            print("** class name missing **")
        else:
            if var[0] not in self.ClassList:
                print("** class doesn't exist **")
            elif len(var) == 1:
                print("** instance id missing **")
            else:
                my_dict = storage.all()
                for obj in my_dict:
                    var2 = obj.split(".")
                    if var2[1] == var[1]:
                        print("{}".format(my_dict[obj]))
                        return
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        var = arg.split(" ")
        if len(var) == 1 and var[0] == '':
            print("** class name missing **")
        else:
            if var[0] not in self.ClassList:
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
            if arg not in self.ClassList:
                print("** class doesn't exist **")
            else:
                my_dict = storage.all()
                for obj in my_dict:
                    var2 = obj.split(".")
                    if var2[0] == arg:
                        lis.append(str(my_dict[obj]))
                        print("{}".format(lis))
        else:
            my_dict = storage.all()
            for obj in my_dict:
                lis.append(str(my_dict[obj]))
            print("{}".format(lis))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        spl = arg.split(" ")
        if len(spl) == 1 and spl[0] == '':
            print("** class name missing **")
        else:
            if spl[0] not in self.ClassList:
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

    def do_count(self, arg):
        """retrieve the number of instances of a class"""
        count = 0
        if arg:
            if arg not in self.ClassList:
                print("0")
            else:
                my_dict = storage.all()
                for obj in my_dict:
                    var = obj.split(".")
                    if var[0] == arg:
                        count += 1
                print("{}".format(count))
        else:
            print("0")

    def default(self, line):
        """Method called when the command prefix is not recognized"""
        var = line.split(".")
        if len(var) == 2:
            var2 = var[1].split("(")
            if len(var2) == 2:
                var3 = var2[1].split(")")
        try:
            print(var[0])
            print(var2[0])
            print(var3[0])
            print(var3)
            print(var[0] + " " + var3[0])
            if var3[0] != '':
                eval("self.do_{}".format(var2[0]))(var[0] + " " + var3[0])
            else:
                eval("self.do_{}".format(var2[0]))(var[0])
        except Exception:
                print("*** Unknown syntax: {}".format(line))

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        print("")
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """checks if there's no input for the prompt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
