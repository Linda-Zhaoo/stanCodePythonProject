"""
File: coin_flip_runs.py
Name: Linda Zhao
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
	"""
	Generate a "T/H" string by random 0/1.
	stop until the run same as user input.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	toss = ''
	run = 0
	# first letter, and must not in continue mode
	f = random.randint(0, 1)
	if f == 0:
		toss += 'T'
	else:
		toss += 'H'
	a = f
	continuous = False
	while True:
		# keep generate the letter and add in string
		f = random.randint(0, 1)
		if f == 0:
			toss += 'T'
		else:
			toss += 'H'
		if f == a:
			# check if same as last letter
			if not continuous:
				run += 1
				continuous = True
		else:
			a = f
			continuous = False
		if run == num_run:
			break
	print(toss)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
