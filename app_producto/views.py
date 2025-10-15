from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria # Importa ambos modelos

# Listar productos
def index(request):
    """
    Muestra una lista de todos los productos.
    """
    productos = Producto.objects.all().order_by('nombre') # Obtiene todos los productos, ordenados por nombre
    return render(request, 'listar_producto.html', {'productos': productos})

# Ver detalle de un producto
def listar_producto(request, id):
    """
    Muestra los detalles de un producto específico.
    """
    producto = get_object_or_404(Producto, id=id) # Obtiene el producto por su ID
    return render(request, 'listar_producto.html', {'producto': producto})

# Agregar un nuevo producto
def agregar_producto(request):
    """
    Maneja la lógica para agregar un nuevo producto.
    Si es un POST, guarda el producto; de lo contrario, muestra el formulario.
    """
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = float(request.POST['precio']) # Asegúrate de convertir a float
        stock = int(request.POST['stock'])     # Asegúrate de convertir a int
        categoria_id = request.POST['categoria'] # Obtiene el ID de la categoría
        
        # Obtiene el objeto Categoria correspondiente al ID
        categoria = get_object_or_404(Categoria, id=categoria_id)

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria # Asigna el objeto Categoria
        )
        return redirect('inicio') # Redirige al listado principal después de agregar

    # Si no es POST, renderiza el formulario con todas las categorías
    categorias = Categoria.objects.all().order_by('nombre') # Obtiene todas las categorías para el <select>
    return render(request, 'agregar_producto.html', {'categorias': categorias})

# Editar un producto existente
def editar_producto(request, id):
    """
    Maneja la lógica para editar un producto existente.
    """
    producto = get_object_or_404(Producto, id=id) # Obtiene el producto a editar

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = float(request.POST['precio'])
        producto.stock = int(request.POST['stock'])
        
        categoria_id = request.POST['categoria']
        # Obtiene y asigna la nueva categoría
        producto.categoria = get_object_or_404(Categoria, id=categoria_id)

        producto.save() # Guarda los cambios en la base de datos
        return redirect('inicio') # Redirige al listado principal

    # Si no es POST, renderiza el formulario con el producto y todas las categorías
    categorias = Categoria.objects.all().order_by('nombre') # Necesario para el <select>
    return render(request, 'editar_producto.html', {'producto': producto, 'categorias': categorias})

# Borrar un producto
def borrar_producto(request, id):
    """
    Maneja la lógica para borrar un producto.
    """
    producto = get_object_or_404(Producto, id=id) # Obtiene el producto a borrar

    if request.method == 'POST':
        producto.delete() # Elimina el producto de la base de datos
        return redirect('inicio') # Redirige al listado principal

    # Si no es POST, muestra la página de confirmación
    return render(request, 'borrar_producto.html', {'producto': producto})