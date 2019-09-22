# 1.feladat
file = open ('szavazatok.txt', 'r')
lista = file.read().strip().split(' ')
n = 0;
while len(lista) < n:
	egysor = lista.ReadLine().Split(' ')
	kepviselo[n].korzet = egysor[0]
	kepviselo[n].szavazat = int(egysor[1])
	kepviselo[n].vnev = egysor[2]
	kepviselo[n].unev = egysor[3]
	kepviselo[n].part = egysor[4]
	n+=1
file.close()
print(kepviselo)
