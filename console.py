#!/usr/bin/python3
"""console module doc"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                var = arg()
                with open()
            except NameError:
                print("** class doesn't exist **")

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
