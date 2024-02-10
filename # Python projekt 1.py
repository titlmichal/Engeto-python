# Python projekt 1
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Titl
email: titlmichal@gmail.com
discord: Michal_T
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
users = ("bob", "ann", "mike", "liz")
passwords = ("123", "pass123", "password123", "pass123")
user_name = input("Enter your user name: ")
user_password = input("Enter your password: ")
if user_name in users and user_password in passwords:
    if users.index(user_name) == passwords.index(user_password):
        print(f"Welcome {user_name}!")
        chosen_text = input("Enter a number between 1 and 3 to select text to analyze: ")
        if chosen_text < 1 and chosen_text > 3:
            print("Entered number is not between 1 and 3!")
            exit()
        elif type():
            print("Not a number!")
            exit()
        else:
            print("...")
    else:
        print("Entered name and password dont match!")
        exit()
else:
    print("Entered name or password doesnt exist!")
    exit()