"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados. 
"""

x = 1

def escopo():
    global x
    x = 10
    
    def interno():
        global x
        x = 22
        y = 2
        print(x, y)
    
    interno()
    print(x)

print(x)
escopo()
print(x)