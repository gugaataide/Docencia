""" Por que Busca Binária?
        Eficiencia!
            Busca linear O(n)
                Busca de elemento em elemento, percorrendo toda a lista no pior caso
                
                (Alvo == 8)
                1 iteraçao: lista[|1|,2,3,4,5,6,7,8,9]
                2 iteraçao: lista[1,|2|,3,4,5,6,7,8,9]
                3 iteraçao: lista[1,2,|3|,4,5,6,7,8,9]
                4 iteraçao: lista[1,2,3,|4|,5,6,7,8,9]
                5 iteraçao: lista[1,2,3,4,|5|,6,7,8,9]
                6 iteraçao: lista[1,2,3,4,5,|6|,7,8,9]
                7 iteraçao: lista[1,2,3,4,5,6,|7|,8,9]
                8 iteraçao: lista[1,2,3,4,5,6,7,|8|,9]
                
                Achou após 8 Iteraçoes
                
                
            Busca binária O(log n):
                A cada iteração, a busca binária elimina metade da lista, diminuindo bastante o numero de iteraçoes necessárias

                (Alvo == 8)
                1 iteraçao: lista[1,2,3,4,|5|,6,7,8,9]     
                2 Iteração: lista[6,|7|,8,9]
                3 Iteração: lista[|8|,9]
                
                Achou o 8 com apenas 3 iteraçoes

"""

lista = [1,2,3,4,5,6,7,8,9]

#Ordene a lista
lista.sort()

def busca_binaria(lista, alvo):
    # Definindo os indices das bordas da lista
    esquerda = 0
    direita = len(lista) - 1 

    while esquerda <= direita:
        meio = (esquerda + direita) // 2  # Calcula o índice do elemento do meio
        # Compara o elemento do meio com o alvo
        if lista[meio] == alvo:
            return meio  # Elemento encontrado, retorna o índice
        elif lista[meio] < alvo:
            esquerda = meio + 1  # Elemento está na metade direita
        else:
            direita = meio - 1  # Elemento está na metade esquerda

    return None  # Elemento não encontrado na lista

busca_binaria(lista, 8)


''' PRÁTICA
   Me explique como funciona a busca binária e depois exemplifique com uma lista que você escolherá
'''