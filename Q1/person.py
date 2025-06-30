class Person:

    def __init__(self, user_id, name, age=None, gender=None, biography=""):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.biography = biography

    def __str__(self):
        return f"@{self.user_id} ({self.name})"
