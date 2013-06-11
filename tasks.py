#! /usr/bin/env python
import sys
from flask.ext.script import Manager

from flaskbp.application import create_app

app = create_app()
manager = Manager(app)

from flaskbp.tasks.devel import manager as devel_manager
manager.add_command("devel", devel_manager)

if __name__ == "__main__":
    manager.run()