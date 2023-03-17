# exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
exam_marks = {'Cierra Vega': 130, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
user_input = int(input("Enter a value: "))
new_dict = {}
for key, value in exam_marks.items():
    if value >= user_input:
        new_dict[key] = value

print(new_dict)