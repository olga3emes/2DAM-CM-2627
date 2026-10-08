x=4
match x:
    case 0:
        print('Cero')
    case 1:
        print('Uno')
    case 2 | 3:
        print('Dos o tres')
    case _ if x < 0:
        print('Negativo')
    case _:
        print('Más grande que tres')