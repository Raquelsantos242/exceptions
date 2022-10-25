try:
    x = float(input('digite um número > 0: '))
    y = 1 / x
    print('1/', x, '=',y)
    
except ZeroDivisionError:
    print('você não pode digitar o valor zero')
    
except ValueError:
        print('você não pode digitar um texto')
        
    
except:
    print('aconteceu algum erro inesperado')
print('FIM')
