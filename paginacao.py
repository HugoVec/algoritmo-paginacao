import random

#Função alocarMemoria passe o tamanho da memoria fisica como argumento
def alocarMemoria(tMemoriaFisica): 

    #Linha 11 - Cria a memoria fisica com o tamanho do argumento escolhido
    #Linha 12 - Sorteia um valor aleatorio entre 10% e 15% e preenche com 1
    #Linha 13 - Calcula a quantidade de memoria fisica disponivel,no caso seria os valores sorteados na variavel
    #espaco utilizado, mas toda vez que uma nova inserção de dados for feita tem que reduzir a quantidade 
    # de memoria fisica disponivel 
    memoria_fisica = [0]*tMemoriaFisica
    espaco_usado = random.randint(tMemoriaFisica*0.1,tMemoriaFisica*0.3)
    memoria_disponivel = len(memoria_fisica) - espaco_usado

    #Linha 17 - Pega o retorno da variavel espaco_usado e preenche na memoria fisica como espaço utilizado
    #Linha 19 - O shuffle embaralha os valores da memoria fisica
    for i in range(espaco_usado):
        memoria_fisica[i] = 1
    random.shuffle(memoria_fisica)

    #Linha 24 - Função para alterar a memoria. Enquanto o valor de y for menor que o tamanho da memoria fisica
    #o laço percorre todos as posições da lista e se esse valor for 0 ele altera para 2 que no caso
    # indica que aquele espaço na memoria está alocado
    def alterarMemoria():
        contador = 0
        for y in range(len(memoria_fisica)):
            if memoria_fisica[y] == 0 and contador != memoria_logica and memoria_disponivel > 0:
                memoria_fisica[y] = 2
                contador +=1

    print(memoria_fisica)

    #Laço de repetição que pergunta para o usuário qual o tamanho da memoria logica que quer inserir
    # Caso o usuário queira inserir um valor maior do que o tamanho da memoria fisica disponivel 
    # Entra no segundo while que solicita uma nova inserção de dados de um valor que seja menor
    #Quando a memoria disponivel for igual a zero o laço encerra 
    while memoria_disponivel > 0:
        memoria_logica = 0
        while memoria_logica <= memoria_disponivel and memoria_disponivel > 0:
            memoria_logica = int(input('Olá usuário, insira o tamanho da memoria lógica: '))
            if(memoria_logica > memoria_disponivel):
                break
            alterarMemoria()
            memoria_disponivel -= memoria_logica
            memoria_logica =  memoria_disponivel
            print(memoria_fisica)
            print("A memoria disponivel é de ", memoria_disponivel)
    
        while memoria_logica > memoria_disponivel and memoria_disponivel != 0:
            memoria_logica = int(input('O valor inserido é maior que a quantidade de memoria disponivel, insira um valor menor: '))
            if(memoria_logica <= memoria_disponivel):
                alterarMemoria()
                memoria_disponivel -= memoria_logica
            print(memoria_fisica)
            print("A memoria disponivel é de ", memoria_disponivel)

    
if __name__ == '__main__':
    alocarMemoria(10)


