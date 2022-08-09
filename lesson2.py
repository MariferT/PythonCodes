def callthisfunction():
    a = int(input('Are you tired? [y/n]: '))
    if a == 1:
        tired()
    elif a.lower() == 'n':
        nottired()
    else:
        print('STREAM PSYCH')


def tired():
    print('ME TOO!')


def nottired():
    print('DO SOMETHING.')


callthisfunction()




while True:
    try:
        noun = str(input('N: '))
        break
    except KeyError:
        print('Word doesn\'t exist.')
        continue


text = ['0', 'a', 'pop', 'bear', 'across']
print(sorted(text))
while True:
    # float value is both pos and neg real numbers
    try:
        x = float(input('Enter first number: '))
        break
    except ValueError:
        print('Invalid input')
        continue
while True:
    try:
        y = float(input('Enter second number: '))
       # if y == 0 and optn.lower() == 'd':
        #    raise ZeroDivisionError
        break
    except ValueError:
        print('Invalid input')
        continue
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        continue

print("Mike said \'I love eating burger!\'")

print('''
===========A Perfect christmas============
my idea of a perfect xmas

''')


#print('I am taking \"BSCpE\"')
#print('John said \"I don\'t like vegetables\"')

#placeholders

sample = "My name is {name} i love {food} and playing {game}"
spl = sample.format(name="cassie", food="tinola", game="chess")
print(spl)

sample = "My name is {0} i love {1} and playing {2}"
spl = sample.format('name','food','pop')
print(spl)

#%s string format
t = "milk"
y = 9.98673
print('\nthis is %s at %.3f pesos' % (t, y))

print(''.join(("I'm learning Python.\n",
                          "I refer to TechBeamers.com tutorials.\n",
                          "It is the most popular site for Python programmers.")))

#"Total eductions: {variable:0.2f} para ma round off"

from nltk.corpus import wordnet as wn
words = ['amazing', 'interesting', 'love', 'great', 'nice']

for w in words:
    tmp = wn.synsets(w)[0].pos()
    print(w, ":", tmp)

noun = input('Enter noun: ')
noun1 = nltk.word_tokenize(noun)
chk_noun = nltk.pos_tag(noun1)

if str(chk_noun).__contains__('JJ'):
    print(noun, chk_noun)
else:
    print(f'not\n{noun}, {chk_noun}')

from nltk.corpus import wordnet as wn
adj_list = []
for i in range(0, 5):
    adj = input(f'Adj{i + 1}: ')
    adj_list.append(adj)
add = []
for w in adj_list:
    tmp = wn.synsets(w)[0].pos()
    if tmp == 'n':
        #str(tmp).__getitem__()
        add.append(tmp)
        print(add)
    #print(w, ":", tmp)