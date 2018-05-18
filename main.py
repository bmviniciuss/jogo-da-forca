#!/usr/bin/env python3
# Jogo da forca - Vinicius Barbosa
# For this time, the game only accepts simples words with 0(zero) spaces.

import random
import InputHandler
import wordGenerator
import utils
import Draw


# GAME
gameOn = True

while gameOn:
	print("Jogo da Forca - Feito por Vinícius Barbosa")
	print("The secret word must be \na single word, with none spaces.")
	print()

	solo = InputHandler.playAlone()

	if solo:
		secretWord = wordGenerator.randomWord()
		print("A hint: The word is a object!")
	else:
		secretWord = InputHandler.getSecretWord()
		utils.cls()

	secretWordList = [l for l in secretWord]
	index = {}
	guesses = []
	correctAttempts = []
	wrongAttempts = []
	erros = 0
	underscore = ['_']*len(secretWordList)
	control = True
	MAX_ATTEMPTS = 6

	# ------- INDEX ------- Generate indexes values for word revel
	for value in secretWordList:
		if value in index:
			index[value] = [ind for ind, letra in enumerate(
				secretWordList) if letra == value]
		else:
			index[value] = secretWordList.index(value)
	# ------------------------------------------------------------

	# Start game
	while control:
		if utils.checkWin(underscore, secretWordList):  # check if game has finished
			utils.cls()  # clear the screen

			print("CONGRATULATIONS!!! Your guess was correct!")
			print("The secret word was: ", " ".join(underscore))

			Draw.drawWin(erros)
			control = False
			break

		# NOT FINISHED
		print("The Word: ", " ".join(underscore))
		Draw.draw(erros, wrongAttempts, secretWord)

		# Make a guess
		guess = InputHandler.getGuess()

		if guess == secretWord:  # guess equals the secret word
			utils.cls()
			print("CONGRATULATIONS!!! Your guess was correct!")
			print("The secret word was: ", " ".join(secretWordList))

			Draw.drawWin(erros)
			control = False
			break

		# Guesses Wrong
		elif guess not in(secretWordList):  # Guess not in the word
			utils.cls()  # clear scrren

			if guess in guesses:  # User already tried this letter
				print("WRONG!!! You already tried this letter.!")
				continue

			else:  # Word does not cotains the letter
				print("WRONG!!! Secret Word does not contains this letter.")

				guesses.append(guess)
				wrongAttempts.append(guess)
				erros += 1

				# MAX ATTEMPTS
				if erros == MAX_ATTEMPTS:  # Max attemps
					Draw.draw(erros, wrongAttempts, secretWord)
					print("GAME OVER!!!")

					control = False
					break
		# GUESS IS IN THE WORD
		else:
			utils.cls()  # Clear the screen
			print("GO ON!!! You got it right!")

			guesses.append(guess)
			correctAttempts.append(guess)

			# If letter only appers once in the word
			if secretWord.count(guess) <= 1:  
				underscore[index[guess]] = guess
				continue

			# If appers more than once
			elif secretWord.count(guess) > 1:  
				numberToIndex = secretWord.count(guess)
				controle = 0

				while not controle == numberToIndex:
					underscore[index[guess][controle]] = guess
					controle += 1

	# Restart
	restartGame = InputHandler.playAgain()
	if restartGame:
		print()
		utils.cls()
		continue
	else:
		print("Thanks for playing!!")
		break
	break
