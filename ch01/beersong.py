
word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        if (beer_num - 1) == 1:
            word = "bottle"
        print(beer_num - 1, word, "of beer on the wall.")
    print()
