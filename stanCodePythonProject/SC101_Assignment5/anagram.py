"""
File: anagram.py
Name: Linda Zhao
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    The program is going to split mainly in two parts.
    First, make a dictionary according to user input(s), the first letter of word in the dictionary would appear in s.
    Second, find all the anagram by 'find_anagrams' and 'find_anagrams_helper'.
    In the 'find_anagrams_helper' would also find if the combination of s is appear in dictionary.
    """
    print("Welcome to stanCode \"Anagram Generator\" or(-1 to quit): ")
    s = str(input('Find anagrams for: '))
    while True:
        start = time.time()
        dictionary = {}
        read_dictionary(s, dictionary)
        if s == EXIT:
            break
        else:
            find_anagrams(s, dictionary)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
        s = str(input('Find anagrams for: '))


def read_dictionary(s, dictionary):
    """
    :param s: str, a sting of character user input
    :param dictionary: dict, an empty dictionary, will contain a words list sorted by first letter which exists in s
    :return: none
    """
    with open(FILE, 'r') as d:
        for line in d:
            if len(line)-1 == len(s) and sorted(line.strip()) == sorted(s):
                # the length need to remove the newline character
                word = line.strip()
                dictionary[word] = 0


def find_anagrams(s, dictionary):
    """
    :param s: str, a sting of character user input
    :param dictionary: dist, the dictionary made by read_dictionary()
    :return: none
    """
    anagrams = []
    print('Searching...')
    find_anagrams_helper(s, '', dictionary, len(s), anagrams)
    print(f'{len(anagrams)} anagrams: {anagrams}')


def find_anagrams_helper(s, anagram, dictionary, length_s, anagrams):
    """
    :param s: str, letters are alphabetically
    :param anagram: str, an empty string that would be re-construct by s
    :param dictionary: dist, the dictionary made by read_dictionary()
    :param length_s: the length of s
    :param anagrams: list, an empty list that will contain all anagram exists in dictionary
    :return: none
    """
    if len(anagram) == length_s:
        if anagram not in anagrams:
            anagrams.append(anagram)
            print(f'Founding: {anagram}')
            print('Searching...')
    else:
        for i in range(len(s)):
            # choose
            anagram += s[i]
            # explore
            if has_prefix(anagram, dictionary):
                new_s = ''
                for j in range(len(s)):
                    if j != i:
                        # remove the letter that already choose
                        new_s += s[j]
                find_anagrams_helper(new_s, anagram, dictionary, length_s, anagrams)
            # un-choose
            anagram = anagram[:-1]


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: str, an incomplete anagram
    :param dictionary: dict, the dictionary made by read_dictionary()
    :return:
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
