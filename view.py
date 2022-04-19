from models.LinkedList import LinkedList

def main():
    ll = LinkedList()
    while True:
        comandos = input().split()
        op = comandos[0].upper()
        parametros = comandos[1:]
        if(op == 'RIP'):
            ll.insert_at_start(parametros)
            ll.traverse_list()
          