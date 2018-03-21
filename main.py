#!/usr/bin/env python3
#Jogo da forca - Vinicius Barbosa
#Até o presente momento, o jogo só aceita palavras simples e sem espaços!!
import random, os
#Funções
def cls(): # Limpar tela
		os.system("cls")
#Palavras
def palavra(): #Recebe palavra
		controle = True
		while controle:
				senha = str(input("Digite uma palavra secreta: ")).lower()
				if senha.isalpha():
						controle = False
						return senha
				else:
						print("Digite uma palavra válida!")
						print()
def palavra_random(): #Escolhe palavra ao acaso
		objetos = ["Algema","Bola","Casaco","Xampu","Agulha","Travesseiro","Computador","Gaiola","Hidrante","Interruptor","Leme","Panela","Dado",]
		return random.choice(objetos)
#Mecânica
def reiniciar(): #Reinicia o jogo
		controle = True
		while controle:
				rei = input("Deseja jogar novamente? (s/n)").lower()
				if rei.isalpha():
						controle = False
						return rei
				else:
						print("Digite um valor válido!!")
						print()
def jogo_solo():
		controle = True
		while controle:
				per = input("Você vai jogar sozinho? (s/n)").lower()
				if per in ("s","n"):
						return per
						break
				else:
						print("Comando inválido!")
						print()
def check_win(sub, senha_list): #Vê se o jogo terminou
		return sub == senha_list
def letra():
		controle = True
		while controle:
				le = input("Digite uma letra(ou a palavra): ")
				if le.isalpha():
						return le
						controle = False
				else:
						print("Digite um valor válido!")
						print()
#Desenho
def desenho(erros, lista_erros,palavra): #Desenha o boneco
		if erros == 0:
				print()
				print("|----- ")
				print("|    | ")
				print("|      ")
				print("|      ",lista_erros)
				print("|      ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 1:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|      ",lista_erros)
				print("|      ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 2:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|    | ",lista_erros)
				print("|    | ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 3:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|    |\\ ",lista_erros)
				print("|    | ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 4:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|   /|\\ ",lista_erros)
				print("|    | ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 5:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|   /|\\ ",lista_erros)
				print("|    | ")
				print("|     \\ ")
				print("_      ")
				print()
		elif erros == 6:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|   /|\\ ENFORCADO!!!",lista_erros)
				print("|    |  A palavra: ",palavra.capitalize())
				print("|   / \\ ")
				print("_      ")
				print()
def desenho_acerto(erros): #Desenha o boneco quando acertar
		if erros == 0:
				print()
				print("|----- ")
				print("|    | ")
				print("|      ")
				print("|      ACERTOU!!!")
				print("|      ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 1:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|      ACERTOU!!!")
				print("|      ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 2:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|    | ACERTOU!!!")
				print("|    | ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 3:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|    |\\ ACERTOU!!!")
				print("|    | ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 4:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|   /|\\ ACERTOU!!!")
				print("|    | ")
				print("|      ")
				print("_      ")
				print()
		elif erros == 5:
				print()
				print("|----- ")
				print("|    | ")
				print("|    O ")
				print("|   /|\\ ACERTOU!!!")
				print("|    | ")
				print("|     \\ ")
				print("_      ")
				print()
#------- JOGO -------
game_on = True
while game_on:
		print("Jogo da Forca - Feito por Vinícius Barbosa")
		print("A palavra secreta deve ser \numa palavra única! Sem espaços!")
		print()
		solo = jogo_solo()
		if solo == "s":
				palavra_secreta = palavra_random().lower()
				print("Uma dica: A palavra é um objeto!")
		else:
				palavra_secreta = palavra()
				for es in range(51): # Esconde a palavra
						print()
				cls()
		palavra_secreta_list = [l for l in palavra_secreta]
		index = {}
		tentativas = []
		tentativas_certas = []
		tentativas_erradas = []
		erros = 0
		sublinhado = ['_']*len(palavra_secreta_list)
		perguntar = True
		#------- INDEX ------- Gera index para revelação das letras
		for valor in palavra_secreta_list:
				if valor in index:
						index[valor] = [ind for ind,letra in enumerate(palavra_secreta_list) if letra == valor]
				else:
						index[valor] = palavra_secreta_list.index(valor)
		#---------------------
		#Começo do Jogo
		while perguntar:
				if check_win(sublinhado,palavra_secreta_list): #Vê se o jogo terminou!
						cls()
						print("Parabéns!!! Você Acertou!")
						print("A palavra: "," ".join(sublinhado))
						desenho_acerto(erros)
						perguntar = False
						break
				print("A palavra: "," ".join(sublinhado))
				desenho(erros,tentativas_erradas,palavra_secreta)
				tentativa = letra()
				if tentativa == palavra_secreta: #Input igual a palavra
						cls()
						print("A palavra: "," ".join(palavra_secreta_list))
						desenho_acerto(erros)
						print("Parabéns!!! Você acertou!! ")
						perguntar = False
				elif tentativa not in(palavra_secreta_list): #Input não esta na palavra
						cls()
						if tentativa in tentativas: #Input já foi colocado
								print("Você já tentou essa letra!")
								continue
						else: #Input não foi tentado
								print("A palavra não tem essa letra!")
								tentativas.append(tentativa)
								tentativas_erradas.append(tentativa)
								erros +=1
								if erros == 6: #numero maximo de tentativas
										desenho(erros,tentativas_erradas,palavra_secreta)
										print("Você perdeu!!!")
										perguntar = False
										break
				else: #input esta na palavra
						cls()
						print("Você acertou uma letra!")
						tentativas.append(tentativa)
						tentativas_certas.append(tentativa)
						if palavra_secreta.count(tentativa)<=1: #Controle do display
								sublinhado[index[tentativa]] = tentativa
								continue
						elif palavra_secreta.count(tentativa)>1: #controle do Display
								numero_para_index = palavra_secreta.count(tentativa)
								controle = 0
								while not controle == numero_para_index:
										sublinhado[index[tentativa][controle]] = tentativa
										controle+=1
		game_restart = reiniciar()
		if game_restart == "s":
				print()
				cls()
				continue
		elif game_restart == "n":
				print("Muito Obrigado!!")
				break
		break
