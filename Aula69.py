"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados. 
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra global faz uma variável do escopo externo
ser a mesma no escopo interno.
"""
# É possivel acessar variáveis apenas de dentro para fora,
# não é possivel acessar uma variavel dentro de uma função
# mas uma função pode usar uma variável fora dela mesma. 

x = 1

def escopo():
    #global x - má prática, porém serve para mudar a var externa pelo valor interno
    x = 10
    
    def interno():
        #global x
        x = 22
        y = 2
        print(x, y)
    
    interno()
    print(x)

print(x)
escopo()
print(x)