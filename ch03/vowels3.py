
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
        
for vowel in sorted(found):
    print(vowel, 'occurred', found[vowel], 'times.')
    
print()

for vowel in sorted(found, key=found.get, reverse=True):
    print(vowel, 'occurred', found[vowel], 'times.')
