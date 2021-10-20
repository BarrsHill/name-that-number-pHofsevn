word="word"
x= 0
dict = {'a': '1', 
    'b': '1',
    'c': '1',
    'd': '2',
    'e': '2',
    'f': '2',
    'g': '3',
    'h': '3',
    'i': '3',
    'j': '4',
    'k': '4',
    'l': '4',
    'm': '5',
    'n': '5',
    'o': '5',
    'p': '6',
    'q': '6',
    'r': '6',
    's': '7',
    't': '7',
    'u': '7',
    'v': '8',
    'w': '8',
    'x': '8',
    'y': '9',
    'z': '9',
}
while len(word)!= 10:
  word = input('Please input a combination of letters you wish to translate into numbers:\n').lower()

for x in str(len(word)):
  print(dict[x])
    

