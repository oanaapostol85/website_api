from quickweb import controller
from cherrypy import HTTPError
import re


class Controller(object):

    def __init__(self):
        self.email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

    @controller.publish
    def register(self, email):
        if not self.email_regex.match(email):
            raise HTTPError(400, "Email adress is not valid")

        return "Python"
