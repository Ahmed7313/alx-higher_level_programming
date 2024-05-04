#!/usr/bin/python3
"""Module for Base class."""

class Base:
    """Base class for all future classes in the project.
    The purpose of this class is to manage the id attribute in all future classes
    and to avoid duplicating code and potential bugs.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.
        Args:
            id (int): The id of the object, or None for automatic assignment.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
