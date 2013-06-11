from flask import current_app
from flask.ext.script import Command, Option, Manager

manager = Manager()

class HelloDev(Command):
    @property
    def app(self):
        return current_app
    
    def run(self):
        print "Hello Dev"


manager.add_command("hello_dev", HelloDev())
