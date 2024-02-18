# Python projekt 1
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Titl
email: titlmichal@gmail.com
discord: Michal_T
"""

texts = ['''
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
separator = "-" * 45

print(separator)
user_name = input("Enter your user name: ")
user_password = input("Enter your password: ")
print(separator)

if user_name in users and user_password in passwords:
    if users.index(user_name) == passwords.index(user_password):
        print(f"Welcome, {user_name}!")
        chosen_text = input("Enter a nr 1, 2 or 3 to select: ")
        print(separator)
        if not chosen_text.isnumeric():
            print("Not a number!")
            print(separator)
        elif int(chosen_text) < 1 or int(chosen_text) > 3:
            print("Entered number is not between 1 and 3!")
            print(separator)

        else:
            text_into_words = (texts[int(chosen_text) - 1]).split()
            word_count = 0
            capital_start_word = 0
            all_capitals_word = 0
            all_lowercase_word = 0
            number_words = 0
            sum_of_number_words = 0
            word_lengths = dict()
            word_count = len(text_into_words)
            for i in text_into_words:
                if i[0].isupper():
                    capital_start_word = capital_start_word + 1
                if i.isupper() and not i[0].isnumeric():
                    all_capitals_word = all_capitals_word + 1
                if i.islower():
                    all_lowercase_word = all_lowercase_word + 1
                if i.isnumeric():
                    number_words = number_words + 1
                    sum_of_number_words = sum_of_number_words + int(i)
                else:
                    pass

            data_dict = {
                "Count of words          :" : word_count,
                "Count of titlecase words:" : capital_start_word,
                "Count of uppercase words:" : all_capitals_word,
                "Count of lowercase words:" : all_lowercase_word,
                "Count of numeric strings:" : number_words,
                "Sum of all the numbers  :" : sum_of_number_words
                }
            for key, value in data_dict.items():
                print(key, value)
            print(separator)

            print("LEN |  OCCURENCES     | NR OF OCCURENCES")
            length_of_word = 0
            for i in text_into_words:
                if "." in list(i) or "," in list(i):
                    length_of_word = len(i) - 1
                    if length_of_word not in word_lengths.keys():
                        word_lengths[length_of_word] = 1
                    else:
                        word_lengths[length_of_word] = word_lengths.get(length_of_word) + 1
                else:
                    length_of_word = len(i)
                    if length_of_word not in word_lengths.keys():
                        word_lengths[length_of_word] = 1
                    else:
                        word_lengths[length_of_word] = word_lengths.get(length_of_word) + 1
            word_lengths_sorted = dict(sorted(word_lengths.items()))
            print(separator)
            for key, value in word_lengths_sorted.items():
                print(str(key).rjust(4), "|", (value * "*").ljust(17), "|", value, sep="")
    else:
        print("Entered name and password dont match!")
else:
    print("Entered name or password doesnt exist!")