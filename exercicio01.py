'''
Desenvolva um programa que conte de 1 a 100 e exiba apenas os números pares. Utilize o "for" e "while" para resolução.

'''

#Utilizando o'for'
print("Números pares de 1 a 100 usando for:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)


#Usando o'while'
print("Número pares de 1 a 100 usando while")
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
