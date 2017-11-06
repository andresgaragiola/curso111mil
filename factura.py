'''
Created on Nov 6, 2017

@author: andresgaragiola
'''
def mostrarProductos(una_lista_productos):
    """Lista todos los productos en consola.
    Args:
        una_lista_productos: Matriz con la lista de productos
    """
    for a in range(0,len(una_lista_productos[0])):
        print(str(a)+"-> "+una_lista_productos[0][a]+" - $"+str(una_lista_productos[1][a]))
        
def mostrarTicket(una_lista_tickets):
    """Lista todos los tickets.
    Args:
        una_lista_tickets: Matriz con la lista de tickets.
    """
    sumaTotalTicket = 0
    for a in range(0,len(una_lista_tickets[0])):
        print(una_lista_tickets[0][a]," - ",una_lista_tickets[1][a]," - $",una_lista_tickets[2][a]) 
        sumaTotalTicket = sumaTotalTicket + una_lista_tickets[2][a]
    print("Total: ",sumaTotalTicket)

productos = [["Yerba","Azucar","Leche","Pan"],[70,15,25,26]]
ticket = [[],[],[]]

termina = 'no'
while termina == 'no':
    mostrarProductos(productos)
    codigo = input("ingresar codigo de articulo ")
    cantidad = input("ingresar cantidad de articulo ")
    ticket[0].append(int(cantidad))
    ticket[1].append(productos[0][int(codigo)])
    ticket[2].append(int(cantidad)*productos[1][int(codigo)])                                  
    termina = input("termina? si/no ")

mostrarTicket(ticket) #Muestra el ticket una vez que terminamos la carga.