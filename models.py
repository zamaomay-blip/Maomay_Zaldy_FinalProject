"""
models.py

Contains classes for the Student Organizer system.
"""


class ClassSchedule:

    def __init__(self, subject, day, time, room, instructor):
        self.subject = subject
        self.day = day
        self.time = time
        self.room = room
        self.instructor = instructor

    def to_dict(self):
        return self.__dict__


class Assignment:

    def __init__(self, title, subject, deadline):
        self.title = title
        self.subject = subject
        self.deadline = deadline
        self.is_completed = False

    def to_dict(self):
        return self.__dict__


class GradeRecord:

    def __init__(self, subject, grade):
        self.subject = subject
        self.grade = grade

    def to_dict(self):
        return self.__dict__


class Note:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def to_dict(self):
        return self.__dict__
