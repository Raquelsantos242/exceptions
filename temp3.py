import math

ok = True
try:
    x = float(input('digite x: '))
except:
    print('x deve ser um numero')
    ok = False
    
if ok:
    try:
        y = math.sqrt (x)
        print('a raiz quadrada de', x, 'é:', y)
    except:
        pritn('x deve ser positivo')