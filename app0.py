# Definimos una lista para almacenar los productos.
# Es una lista de diccionarios.
productos = []
# Definir un segundo arreglo para el carrito de compras
carrito = []

print("Hola mundo")

def agregar_producto(codigo, descripcion, cantidad, precio):
    # Creamos un diccionario con los datos del producto...
    nuevo_producto = {
         'codigo': codigo,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio
    }
    # Y lo agregamos a nuestro arreglo.
    productos.append(nuevo_producto)
    return True

def consultar_producto(codigo):
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # Refresamos el diccionario correspondiente.
            return producto
    # Si el bucle finaliza sin encontrar el producto,
    # regresamos "falso."
    return False

def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio):
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # ...actualizamos los valores de cada clave del diccionario
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio


            # Como no hay otro producto con ese código, salimos del bucle.
            return True
    # Si llegamos aqui, el producto no existe.
    return False

def listar_productos():
    # Recorremos la lista de productos...
    print("-"*30)
    for producto in productos:
        # Y mostramos los datos de cada uno de ellos.
        print(f"Código: {producto['codigo']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")
        print("-"*30)

def eliminar_producto(codigo):
    # Recorremos la lista de productos...
    for producto in productos:
        # Y si el código es el correcto,
        if producto['codigo'] == codigo:
            # ...lo quitamos de la lista.
            productos.remove(producto)
            # Como no hay otro producto con ese código, salimos del bucle.
            return True
    # Si llegamos aqui, el producto no existe.
    return False

def agregar_al_carrito(codigo, cantidad):
    # Vemos si existe el producto...
    producto = consultar_producto(codigo)


    # Si se devolvio un falso, el producto no existe.
    if producto is False:
        print("El producto no existe.")
        return False


    # Vemos si hay cantidad suficiente de ese producto...
    if producto['cantidad'] < cantidad:
        print("Cantidad en stock insuficiente.")
        return False


    # Verificar si el producto ya está en el carrito
    for item in carrito:
        if item['codigo'] == codigo:
            # Si existe, sumo a la cantidad del carrito...
            item['cantidad'] += cantidad
            # ...y descuento del stock de ese producto.
            producto['cantidad'] -= cantidad
            return True


    # Si el producto no está en el carrito, se agrega como un nuevo item
    nuevo_item = {
        'codigo': codigo,
        'descripcion': producto['descripcion'],
        'cantidad': cantidad,
        'precio': producto['precio']
    }
    carrito.append(nuevo_item)


    # ...y descuento del stock de ese producto.
    producto['cantidad'] += cantidad
    return True

def quitar_del_carrito(codigo, cantidad):
    # Recorremos la lista de productos en el carrito...
    for item in carrito:
        # Si se ecuentra ese producto...
        if item['codigo'] == codigo:
            # Si no hay cantidad suficiente en el carrito...
            if cantidad > item['cantidad']:
                print("Cantidad a quitar mayor a la cantidad en el carrito.")
                return False


            # Si llegue aqui, es que puedo descontarlos del carrito...
            item['cantidad'] -= cantidad


            # ...y reponerlos en el stock de productos!
            producto = consultar_producto(codigo)
            modificar_producto(codigo, producto["descripcion"], producto["cantidad"]-cantidad, producto["precio"] )


            # Compruebo si la cantidad de ese producto en el carrito es cero:
            if item['cantidad'] == 0:
                # Si quedo en cero, lo elimino del carrito.
                carrito.remove(item)
            return True


    # Si el bucle finaliza sin novedad, es que ese producto NO ESTA en el carrito.
    print("El producto no se encuentra en el carrito.")
    return False

def mostrar_carrito():
    """
    Muestra en pantalla el contenido del carrito de compras.
    """
    # Inicializamos una variable para sumar los importes de cada item
    suma = 0
    print("-"*30)


    # Recorremos la lista de productos en el carrito
    # y mostramos los datos de cada producto.
    for item in carrito:
        print(f'Cod: {item["codigo"]} - {item["descripcion"]}')
        print(f'Precio: {item["precio"]}  Cantidad: {item["cantidad"]}')


        # Calculamos el importe a pagar por el producto...
        importe = item["precio"] * item["cantidad"]


        # ...y acumulamos el importe en la variable suma.
        suma += importe
        print(f'Importe: {importe}')
        print("-"*30)
    print(f'Importe TOTAL: {suma}')
    return True

# Agregamos productos a la lista:
agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500)
agregar_producto(2, 'Mouse USB 3 botones', 5, 2500)
agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500)
agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500)
agregar_producto(5, 'Pad mouse', 5, 500)
# eliminar_producto(5) # Eliminamos un producto del stock.

# Testeo de funciones sueltas ******************************************************
# Consultar un producto por su código
# producto = consultar_producto(1)
# if producto:
#     print(f"Producto encontrado: {producto['descripcion']}")
# else:
#     print("Producto no encontrado.")


# Modificar un producto por su código
# modificar_producto(1, 'Teclado mecánico 62 teclas', 20, 34000)


# Listamos todos los productos en pantalla
listar_productos()


# Agregamos productos al carrito
agregar_al_carrito(1, 2)
agregar_al_carrito(2, 1)


# agregar_al_carrito(30, 1) # intentamos agregar un producto inexistente
# Intentar agregar un producto con cantidad insuficiente
# agregar_al_carrito(1, 150)


# Quitar un producto del carrito
quitar_del_carrito(1, 1)


# Mostrar el contenido del carrito
mostrar_carrito()