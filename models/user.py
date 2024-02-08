#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """user class"""

    def __init__(self, email="", password="", first_name="", last_name=""):
        """Initialize User attributes."""
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

