import random

def paginacao():
    
    memoria_fisica = [1]*10
    tamanho = random.randint(2, 30)

    print(memoria_fisica)

    # mudar numero 50 pra um random 
    for i in range(30):
        memoria_fisica[i] = memoria_fisica[i] + 1
        
    print(memoria_fisica)



if __name__ == '__main__':
    paginacao()














