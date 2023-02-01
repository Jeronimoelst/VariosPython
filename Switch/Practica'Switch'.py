# Python no contiene Switch pero hay maneras de intentar emparejarlo 
# // Ojo, esto no es Python
# switch(condicion) {
#   case 1:
#     // haz a
#     break;
#   case 2:
#     // haz b
#     break;
#   case 3:
#     // haz c
#     break;
#   default:
#     // haz x
# }
# esa es una estructura switch


def opera1(operador, a, b):
    if operador == 'suma':
        return a + b
    elif operador == 'resta':
        return a - b
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None

def opera2(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)

opera1('suma', 5, 9)

opera2('suma', 5, 9)()

# volver aleer y practicar 

