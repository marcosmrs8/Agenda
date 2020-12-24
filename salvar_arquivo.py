try:
    with open('nomes.txt', 'a') as arquivo:
        arquivo.write('\nMarcos')
        print(arquivo.readlines())
except Exception as error:
    print('algum erro ocorreu')
    print(error)
'''
#modo r para ler, 
# w para escrever, mas arquivo é 
a para escrever mas não sobrescreve
+ adiciona 
b binario

'''