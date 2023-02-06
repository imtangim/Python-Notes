letter = '''Dear <|name|>,
your are selected
Date : <|date|>'''

Name = input("Enter your name ")
date = input("Enter your date ")
letter=letter.replace("<|name|>", Name)
letter=letter.replace("<|date|>", date)

print(letter)