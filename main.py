#!/usr/bin/python
# -*- coding: utf-8 -*-
from bysize import *
from byextension import *
from bydate import *


class Decide:

    def __init__(self, choice, path):
        self.choice = choice
        self.path = path

    def choose(self):
        if self.choice == 1:
            return self.runbysize(self.path)
        elif choice == 2:
            return self.runbyextension(self.path)
        elif choice == 3:
            return self.runbydate(self.path)

    def runbysize(self, path):
        p = sizecheck(self.path)
        return p

    def runbyextension(self, path):
        p = sort_exten(self.path)
        return p

    def runbydate(self, path):
        p = bydate(self.path)

        return p


if __name__ == '__main__':
    print ("--------------------------------")
    print ("Welcome to Junk File Organizer")
    print ("--------------------------------")
    print ("Project Created by Sahil Kumar")
    print ("--------------------------------")
    print ("Press 1 to Sort by Size")
    print ("--------------------------------")
    print ("Press 2 to sort by Extension")
    print ("--------------------------------")
    print ("Press 3 to sort by Date")
    print ("--------------------------------")
    choice = int(input())
    print ("Please enter the path")
    path = input()

    obj = Decide(choice, path)
    obj.choose()
