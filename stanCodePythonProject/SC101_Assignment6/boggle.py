"""
File: boggle.py
Name: Linda Zhao
----------------------------------------
This is a 4*4 boggle game, user can input 4 letters and 4 lines,
program would fine all the word in boggle.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	user input 4 letters and 4 lines.
	dictionary would fine the word only with user input letters.
	And search the word that could find in boggle.
	"""
	print("Please input 4 letters, and use space to split the letters, ex:a b c d")
	print("**Note: no space after 4th letters")
	row_ls = []
	if user_input(row_ls):
		start = time.time()
		####################
		dictionary = set()
		read_dictionary(dictionary, row_ls)
		words = set()
		find_word(dictionary, row_ls, words)
		print(f'There are {len(words)} words in total.')
		####################
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')
	else:
		print('illegal input')


def user_input(row_ls):
	"""
	:param row_ls: ls, an empty list to put all the letter user input
	:return: bool, if user input in correct format
	"""
	for i in range(4):
		row = str(input(f'{i+1} row of letters: '))
		if len(row) == 7:
			row = row.split(' ')
		else:
			return False
		for ch in row:
			if not ch.isalpha() or len(ch) != 1:
				return False
		row_ls.append(row)
	return True


def read_dictionary(dictionary, row_ls):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:param dictionary: set, an empty set to contain the first letter of word include in user input letters
	:param row_ls: ls, an dictionary which put all the letter that user input
	:return: None.
	"""
	letters = ''
	for i in range(4):
		for j in range(4):
			letters += row_ls[i][j]
	with open('dictionary.txt', 'r') as d:
		for line in d:
			if 4 <= len(line) - 1 <= 16:
				word = line.strip()
				if check_ch(word, letters):
					dictionary.add(word)


def check_ch(word, letters):
	"""
	To check if the word's each ch is contain in letters.
	:param word: str, the word in dictionary
	:param letters: str, contain all the latter in user input rows
	:return: bool
	"""
	for ch in word:
		if ch not in letters:
			return False
	return True


def find_word(dictionary, row_ls, words):
	"""
	:param dictionary: set, contain the first letter of word include in user input letters
	:param row_ls: ls, put all the letter user input
	:param words: set, put all the word that found in dictionary
	:return: None
	"""
	for i in range(4):
		for j in range(4):
			word = str(row_ls[i][j])
			row_ls[i][j] = 0
			find_word_helper(dictionary, row_ls, words, word, i, j)
			row_ls[i][j] = word


def find_word_helper(dictionary, row_ls, words, word, now_x, now_y):
	"""
	:param dictionary: set, contain the first letter of word include in user input letters
	:param row_ls: ls, put the letter user input
	:param words: set, put all the word that found in dictionary
	:param word: str, the word trying to spelling
	:param now_x: int, the x coordinate of boggle
	:param now_y: int, the y coordinate og boggle
	:return: None
	"""
	if now_x >= 4 or now_y >= 4:
		return
	for i in range(now_x-1, now_x+2):
		for j in range(now_y-1, now_y+2):
			if 0 <= i < 4 and 0 <= j < 4:
				if row_ls[i][j] is not 0:
					word += str(row_ls[i][j])
					if has_prefix(word, dictionary):
						if len(word) >= 4 and word in dictionary:
							print(f'Founding: {word}')
							words.add(word)
						row_ls[i][j] = 0
						find_word_helper(dictionary, row_ls, words, word, i, j)
					row_ls[i][j] = word[len(word)-1]
					word = word[:-1]


def has_prefix(sub_s, dictionary):
	"""
	:param dictionary:
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
