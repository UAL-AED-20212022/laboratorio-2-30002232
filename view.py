from models.LinkedList import LinkedList

def main():
    ll = LinkedList()
    while True:
        comandos = input().split()
        op = comandos[0].upper()
        if(op == 'RIP'):
             print (op)