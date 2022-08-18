import nltk  # natural language toolkit that we can use for NLP--making human language usable in computer
import re  # regular expression for white spaces, modifiers, identifiers ex r'\b\b'
#  remember the nltk syntax


def recognizing_words():
    noun_list = []
    adj_list = []

    start = 0  # so that i can trace which index that needs to be caught
    print('ENTER 3 NOUNS')
    while True:
        try:
            for i in range(start, 3):
                noun = input(f'N{i+1}: ')
                if noun == '':
                    raise BaseException
                else:
                    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(noun))):
                        if pos in ('NN', 'NNS', 'NNP', 'NNPS') and noun not in noun_list:
                            noun_list.append(noun)
                            start += 1
                        else:
                            if noun in noun_list:
                                raise Exception
                            elif start == 0:
                                raise KeyError
                            elif start == 1:
                                raise KeyError
                            elif start == 2:
                                raise KeyError
            break
        except KeyError:
            print('Word is not a noun but a(n)', pos)
            continue
        except Exception as e:
            print('Noun exists. Try another.', e)
            continue
        except BaseException as e:
            print('That is empty.', e)
            continue

    print('ENTER 3 ADJECTIVES')
    start = 0
    while True:
        try:
            for i in range(start, 3):
                adj = input(f'Adj{i+1}: ')
                if adj == '':
                    raise BaseException
                else:
                    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(adj))):
                        if pos in ('JJ', 'JJR', 'JJS') and adj not in adj_list:
                            adj_list.append(adj)
                            start += 1
                        else:
                            if adj in adj_list:
                                raise Exception
                            elif start == 0:
                                raise KeyError
                            elif start == 1:
                                raise KeyError
                            elif start == 2:
                                raise KeyError
            break
        except KeyError:
            print('Word is not an adjective but a(n)', pos)
            continue
        except Exception as e:
            print('Adjective exists. Try another.', e)
            continue
        except BaseException as e:
            print('That is empty.', e)
            continue

    poem = '''
    Burdens are numbered like the stars
    The door of fortitude is left ajar.
    Twins of pessimism crawled in
    Prying upon hopes, all for the win;
    
    They sip vintage wine in bleak times
    Holiday of misery, it chimes
    Chaining its heart to oblivion
    A plea for finality, none of agitation;
    
    This castle of life felt a million years old
    Torn and chaotic, even patience it can't hold
    Burn it up 'til the embers sing a lie
    Of what remains a good memory to go by.
    
    Poem by: Marifer Tablada
    '''

    poem_noun = [word for word, pos in nltk.pos_tag(nltk.word_tokenize(str(poem))) if pos in ('NN','NNS', 'NNP', 'NNPS')]
    poem_adj = [word for word, pos in nltk.pos_tag(nltk.word_tokenize(str(poem))) if pos in ('JJ', 'JJR', 'JJS')]

    new_words = {  # key or the word to replace and then the value or words to be replaced || dic
        poem_noun[0]: noun_list[0].upper(),
        poem_noun[1]: noun_list[1].upper(),
        poem_noun[2]: noun_list[2].upper(),
        poem_adj[0]: adj_list[0].upper(),
        poem_adj[1]: adj_list[1].upper(),
        poem_adj[2]: adj_list[2].upper(),
    }
    print('-------------------ORIGINAL-------------------')
    print(poem)
    print('--------------------RESULT--------------------')
    for key, value in new_words.items():  # re.sub in replacing specific strings
        poem = (re.sub(r'\b%s\b' % key, value, poem))  # will read string as whole word in the dic new_words
    print(poem)
    try_again()


def try_again():
    while True:
        run = input('Try again? (y/n): ')

        if run.lower() == 'y':
            recognizing_words()
            break
        elif run.lower() == 'n':
            print('Thank you.')
            break
        else:
            print('Invalid input')
            continue


recognizing_words()