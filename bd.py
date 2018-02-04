#recupération de la sortie de la base donnée j'ai un peu arragné la sortie :)
base = "1|bookC|4\n2|bookA|3\n3|bookB|9\n4|bookC|11" 
print(base)
base = list(base) #conversion de la chaine de caractère en liste 
print(base)


bookC = bookA = bookB = i = 0 #initialisation des variables
for lettre in base: #on boucle la liste pour la traité
	if (base[i] == 'C' ):
		bookC += int(base[i + 2])
	if (base[i] == 'A' ):
		bookA += int(base[i + 2])
	if (base[i] == 'B' ):
		bookB += int(base[i + 2])
	i = i + 1

print(bookA)
print(bookB)
print(bookC)

a = input("Taper le nombre de book A vendu en plus : \n")
a = int(a) + bookA
b = input("Taper le nombre de book B vendu en plus : \n")
b = int(b) + bookB
c = input("Taper le nombre de book C  vendu en plus : \n")
c = int(c) + bookC

print("le nombre total de livre vendu est de ",a)
print("le nombre total de livre vendu est de ",b)
print("le nombre total de livre vendu est de ",c)


	








