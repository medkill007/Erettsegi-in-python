file = open ('ip.txt', 'r')
lista_sz = [x.strip('\n') for x in file]
adatok = [x.split(':') for x in lista_sz]
file.close()
print('2.feladat:\n',len(adatok))

