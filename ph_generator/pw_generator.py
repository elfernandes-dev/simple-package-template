#Gerador de Senhas
import random, string

print('#'*3 +' Gerador de Senhas '+ '#'*3 )
print('-'*25)

size = int(input('Digite o tamanho da senha que você deseja: '))
chars = string.ascii_letters + string.digits + '!?/@#$%*_-+=§Çç;:<>,.'
rnd = random.SystemRandom()
print('\nSua senha é: ' + ''.join(rnd.choice(chars) for i in range(size)))