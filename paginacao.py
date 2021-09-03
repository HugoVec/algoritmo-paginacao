import random

def paginacao():
    
    memoria_fisica = [0]*10
    espaco_usado = random.randint(2, 9)
    memoria_disponivel = len(memoria_fisica) - espaco_usado

    # Aloca espaco usado aleatoriamente na memoria fisica
    for i in range(espaco_usado):
        memoria_fisica[i] = 1
        
    print(memoria_fisica)

    # Pede ao usuário a memoria logia a ser inserida na memoria fisica
    memoria_logica = int(input('Ola usuario, qual o tamanho de memoria logica que deseja inserir? '))

    # Caso a memoria logica pedida seja maior que a memoria disponivel ele pede que insira uma nova
    while memoria_logica > memoria_disponivel:
        memoria_logica = int(input('Por favor insira uma quantidade menor ou igual a: '))

    # Aloca a memoria logica na fisica
    for x in range(len(memoria_fisica)):
        if memoria_fisica[x] == 0 and memoria_logica > 0:
            memoria_fisica[x] = 2
            memoria_logica = memoria_logica - 1

    print(memoria_fisica)

    
    



if __name__ == '__main__':
    paginacao()














