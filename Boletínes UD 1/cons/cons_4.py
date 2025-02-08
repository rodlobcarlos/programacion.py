#Modifica el programa anterior para que sólo pinte el borde del cuadrado

n = 4
i = 1

while i <= n:
    if i == 1 or i == n: 
        print(n * '*')    
    else:
        print('*' + ' ' * (n - 2) + '*')  
    i += 1  