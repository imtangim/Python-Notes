mydict = {
    "pakha": "fan",
    "kedara":"chair",
    "sorasori": "live",
    "hi": "ei",
    "Biddut": "electricity"
}
print("Select from those word: ",mydict.keys())
a = input("enter the bangla word in bangla spelling: ")
print("The english of your word is: ", mydict.get(a))