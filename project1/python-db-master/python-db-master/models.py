from collections import namedtuple

Internship = namedtuple("Internship", ["id","iname", "company", "i_year","status"])
Student = namedtuple("Student", ["usn", "name", "sem","placed"])
Registration = namedtuple("Registration",["iid","usn","status"])