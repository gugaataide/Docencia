'''Por que usar funçoes?
        Servem para reaproveitar um bloco de código e organizar seu código
         

'''


#funcao simples
def soma(numero1, numero2):
    resultado = numero1 + numero2
    
    return resultado

res = soma(1+1)


''' PRÁTICA
   1. Desenvolva uma funçao que multiplique dois numeros

   2. Desenvolva uma funcao que verifique se uma string é igual a "SENHA". Se sim, retorne True, se nao, retorne False
'''





# Recursividade
def fatorial(n):
    # Caso base: O fatorial de 0 é 1
    if n == 0:
        return 1
    # Caso recursivo: Chamamos a função fatorial com um valor menor (n-1)
    else:
        return n * fatorial(n - 1)
