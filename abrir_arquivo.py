try:
    with open('emails.doc') as arquivo:
        print(arquivo.readlines())
except FileNotFoundError:
    print('arquivo nao existe')

#conteudo = arquivo.readlines()

#for linha in conteudo:
#    print(linha.strip())