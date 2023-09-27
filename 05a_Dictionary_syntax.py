from typing import Dict


myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'}
}
# print(myDict['Fast'])
# print(myDict['Harry'])
myDict['Marks'] = [45, 78]
print(myDict['Marks'])
print(myDict['anotherdict']['harry'])

# also can declare by using this syntax:
""" myDict = dict([
    ("Fast", "In a Quick Manner"),
    ("Harry", "A Coder"),
    ("Marks", [1, 2, 5]),
    ("anotherdict", {'harry': 'Player'})
]) """
