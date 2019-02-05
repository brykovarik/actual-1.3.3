from __future__ import print_function # use Pyton 3.0 printing

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13
    if age < AGE_LIMIT:
        print (age, 'is below the age limit.')
    else:
            print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
def report_grade(percent):
     '''Step 6b if-else'''
     MINIMUM_PERCENT = 80
     if percent < MINIMUM_PERCENT:
        print(percent, 'is below the minimum percent.')
     else:
            print(percent, 'is good enough.')
def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
# should check len(letter)==1
def letter_in_word(guess, word):
    word = 'hockey'
    if guess in word:
        return True
    else:
        return False
def hint(color, secret):
    secret = ['red','red','yellow','yellow','black']
    if color in secret:
        print(color, 'IS in the secret sequence of colors.')
    else:
        print(color, 'IS NOT in the secret sequence of colors.')

