"""
a = .-                      j = .---                s = ...
b = -...                    k = -.-                 t = -
c = -.-.                    l = .-..                u = ..-
d = -..                     m = --                  v = ...-
e = .                       n = -.                  w = .--
f = ..-.                    o = ---                 x = -..-
g = --.                     p = .--.                y = -.--
h = ....                    q = --.-                z = --..
i = ..                      r = .-.

Morse Code Translator

This Python script translates a given word or phrase into Morse code. It accepts various alphabet characters, spaces,
and a few common punctuation marks. Each character is matched to its corresponding Morse code representation and printed
as output.

Usage:
1. Run the script.
2. Enter the word or phrase you want to translate into Morse code.
3. The script will print the Morse code representation of each character, separated by newlines.
4. Each new line represents a letter. An empty line indicates the beginning of a new word.

Morse Code Mapping:
The following characters are supported:
- Alphabets (a-z)
- Space (' ')
- Punctuation: Comma (','), Question Mark ('?'), Exclamation Mark ('!'), Full Stop ('.'), Colon (':'),
    Semi-Colon (';'), Apostrophe ("'").

Note:
- Any characters other than the supported ones will result in an error message.
- The script is case-insensitive, converting input to lowercase.

Feel free to experiment with different words, phrases, and punctuation to see their Morse code equivalents!
"""

"""
-.
.
...-
.
.-.

--.
---
-.
-.
.-

--.
..
...-
.

-.--
---
..-

..-
.--.
,

-.
.
...-
.
.-.

--.
---
-.
-.
.-

.-..
.
-

-.--
---
..-

-..
---
.--
-.
,

-.
.
...-
.
.-.

--.
---
-.
-.
.-

.-.
..-
-.

.-
.-.
---
..-
-.
-..

.-
-.
-..

-..
.
...
.
.-.
-

-.--
---
..-
,

-.
.
...-
.
.-.

--.
---
-.
-.
.-

--
.-
-.-
.

-.--
---
..-

-.-.
.-.
-.--
,

-.
.
...-
.
.-.

--.
---
-.
-.
.-

...
.-
-.--

--.
---
---
-..
-...
-.--
.
,

-.
.
...-
.
.-.

--.
---
-.
-.
.-

-
.
.-..
.-..

.-

.-..
..
.

.-
-.
-..

....
..-
.-.
-

-.--
---
..-
"""

list = []

phrase = input("Enter the word you want to translate into Morse Code: ")

phrase = phrase.lower()

for letter in phrase:
    list.append(letter)

for letter in range(len(list)):
    
    if list[letter] == "a":
        print(".-")

    elif list[letter] == "b":
        print("-...")

    elif list[letter] == "c":
        print("-.-.")
    
    elif list[letter] == "d":
        print("-..")

    elif list[letter] == "e":
        print(".")

    elif list[letter] == "f":
        print("..-.")

    elif list[letter] == "g":
        print("--.")

    elif list[letter] == "h":
        print("....")

    elif list[letter] == "i":
        print("..")

    elif list[letter] == "j":
        print(".---")

    elif list[letter] == "k":
        print("-.-")
    
    elif list[letter] == "l":
        print(".-..")

    elif list[letter] == "m":
        print("--")

    elif list[letter] == "n":
        print("-.")

    elif list[letter] == "o":
        print("---")

    elif list[letter] == "p":
        print(".--.")

    elif list[letter] == "q":
        print("--.-")

    elif list[letter] == "r":
        print(".-.")

    elif list[letter] == "s":
        print("...")

    elif list[letter] == "t":
        print("-")

    elif list[letter] == "u":
        print("..-")

    elif list[letter] == "v":
        print("...-")

    elif list[letter] == "w":
        print(".--")

    elif list[letter] == "x":
        print("-..-")

    elif list[letter] == "y":
        print("-.--")

    elif list[letter] == "z":
        print("--..")

    elif list[letter] == "":
        print()

    elif list[letter] == " ":
        print()

    elif list[letter] == ",":
        print(",")

    elif list[letter] == "?":
        print("?")

    elif list[letter] == "!":
        print("!")

    elif list[letter] == ".":
        print(".")

    elif list[letter] == ":":
        print(":")

    elif list[letter] == ";":
        print(";")

    elif list[letter] == "'":
        print("'")

    else:
        print(f"Error on {list[letter]}! Input an acceptable phrase.")
        print("Acceptable phrases are: ")
        print("1. Any alphabet characters")
        print("2. A space character")
        print("3. Commas, Question Marks, Exclamation Marks, Full Stops, Colons, Semi-Colons, Apstrophe.")

    letter = letter + 1
