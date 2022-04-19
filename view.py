from models.LinkedList import LinkedList

def main():
    ll = LinkedList()
    while True:
        comandos = input().split()
        op = comandos[0].upper()
        parametros = comandos[1:]
        if(op == 'RIP'):
            ll.insert_at_start(parametros[0])
            ll.traverse_list()
        elif(op == 'RPF'):
            ll.insert_at_end(parametros[0])
            ll.traverse_list()
        elif(op == 'RPDE'):
            ll.insert_after_item(parametros[1], parametros[0])
            ll.traverse_list()
        elif(op == 'RPAE'):
            ll.insert_before_item(parametros[1], parametros[0])
            ll.traverse_list()
        elif(op == 'RPI'):
            ll.insert_at_index(int(parametros[1]), parametros[0])
            ll.traverse_list()
        elif(op == 'VNE'):
            print(f"O número de elementos são {ll.get_count()}")
        elif(op == 'VP'):
            if(ll.search_item(parametros[0])):
                print(f"O país {parametros[0]} encontra-se na lista.")
            else:
                print(f"O país {parametros[0]} não se encontra na lista.")
        elif(op == 'EPE'):
            primeiro_elemento = ll.start_node
            ll.delete_at_start()
            print(f"O país {primeiro_elemento} foi eliminado da lista.")
        elif(op == 'EUE'):
            ll.delete_at_end()
            print(f"O país {parametros[0]} foi eliminado da lista.")
        elif(op == 'EP'):
            if(ll.search_item(parametros[0])):
                ll.delete_element_by_value(parametros[0])
                print(f"O país {parametros[0]} foi eliminado da lista.")
            else:
                print(f"O país {parametros[0]} não se encontra na lista.")