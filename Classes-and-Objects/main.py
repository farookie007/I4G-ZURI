from typing import List


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: List, score: float):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
    
    def change_name(self, name: str):
        "Changes the name of the `Student` object"
        self.name = name

    def change_age(self, age: int):
        "Changes the age of the `Student` object"
        self.age = int(age)
    
    def add_track(self, track):
        "Adds new track to the `Student` track"
        self.tracks.append(track)

    def get_score(self):
        "Returns the students current score."
        return self.score




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
