#!/usr/bin/python3

import os


class PathHelper:
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__import__("__main__").__file__))


