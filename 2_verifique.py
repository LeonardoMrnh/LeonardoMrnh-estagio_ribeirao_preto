""""

2) Escreva um programa que verifique, em uma string, a existência da letra a, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência 
ou pode ser previamente definida no código;

"""

def verifique (texto):

    #Converte a string para minúscula
    texto = texto.lower()

    #Verifica se contem a letra 'a'
    contem_a = 'a' in texto

    #Contador de vezes do 'a'
    quantidade_a = texto.count('a')

    return contem_a, quantidade_a

#Texto do input
texto = input('Digite uma palavra contem a palavra: ')

contem_a, quantidade_a = verifique(texto)

if contem_a:
    print(f"A letra 'a' está presente na string '{texto}' e aparece **{quantidade_a}** vezes.")
else:
    print(f"A letra 'a' não está presente na string '{texto}'.")