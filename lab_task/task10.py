books = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure': 14}

lar_book = ""
lar_key = 0

for value in books:
    if(books[value]>lar_key):
        lar_key = books[value]
        lar_book = value
print(f'The highest selling book genre is {lar_book} and the number of books sold are {lar_key}.')