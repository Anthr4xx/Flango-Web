from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'supersecretkey'

PRODUCTS = [
    {"name": "Casa de la Brisa", "price": 200000.00, "image": "static/images/Casa de la Brisa.jpg"},
    {"name": "Castillo Stormveil", "price": 500000000.00, "image": "static/images/Stormveil Castle.jpg"},
    {"name": "Viñedo Corvo Bianco", "price": 5000000.00, "image": "static/images/Corvo Bianco.jpg"},
    {"name": "Minehouse", "price": 350000.00, "image": "static/images/Minehouse.jpg"},
    {"name": "Departamento en Corpo Plaza", "price": 10000000.00, "image": "static/images/Departamento en Corpo Plaza.jpg"},
    {"name": "Yate", "price": 200000000.00, "image": "static/images/Yate.jpg"},
    {"name": "Chalet", "price": 30000000.00, "image": "static/images/Chalet.jpg"},
    {"name": "Laboratorio del Profesor Oak", "price": 800000.00, "image": "static/images/Laboratorio del Profesor Oak.jpg"},
    {"name": "Decoración con laboratorio de alquimia", "price": 45000.00, "image": "static/images/Laboratorio de alquimia.jpg"},
    {"name": "Renovación de hogar", "price": 1500000.00, "image": "static/images/Renovación.jpg"}
]


@app.route('/')
def home():
    session.pop('cart', None) 
    return render_template('home.html')


@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        productos_seleccionados = request.form.getlist('productos')
        
        if 'cart' in session:
            session['cart'].extend([p for p in productos_seleccionados if p not in session['cart']])
        else:
            session['cart'] = productos_seleccionados
        
        session.modified = True
        return redirect(url_for('confirmacion'))
    
    return render_template('productos.html', productos=PRODUCTS, carrito=session.get('cart', []))


@app.route('/confirmacion', methods=['GET', 'POST'])
def confirmacion():
    if 'cart' not in session or not session['cart']:
        return redirect(url_for('productos'))
    
    total_price = sum(float(product["price"]) for product in PRODUCTS if product["name"] in session['cart'])
    total_price_formatted = f"{total_price:,.2f}"

    if request.method == 'POST':  
        session['total_price'] = total_price_formatted
        return redirect(url_for('datos'))

    return render_template('confirmacion.html', carrito=[product for product in PRODUCTS if product['name'] in session['cart']], total_price=total_price_formatted)


@app.route('/eliminar_producto', methods=['POST'])
def eliminar_producto():
    producto_eliminar = request.form.get('producto_eliminar')

    if 'cart' in session and producto_eliminar in session['cart']:
        session['cart'].remove(producto_eliminar)
        session.modified = True

    return redirect(url_for('confirmacion'))


@app.route('/datos', methods=['GET', 'POST'])
def datos():
    if request.method == 'POST':
        session['nombre'] = request.form.get('nombre')
        session['apellido'] = request.form.get('apellido')
        session['telefono'] = request.form.get('telefono')
        session['direccion'] = request.form.get('direccion')
       
        email = request.form.get('email', '').strip()
        session['email'] = email if email else 'El correo electrónico no fue proporcionado'


        session['numero_tarjeta'] = request.form.get('numero_tarjeta')
        session['nombre_titular'] = request.form.get('nombre_titular')
        session['fecha_vencimiento'] = request.form.get('fecha_vencimiento')
        session['cvv'] = request.form.get('cvv')
        return redirect(url_for('exito'))
    
    return render_template('datos.html')


@app.route('/exito')
def exito():
    carrito = session.get('cart', [])
    nombre = session.get('nombre')
    apellido = session.get('apellido')
    telefono = session.get('telefono')
    direccion = session.get('direccion')
    email = session.get('email', 'El correo electronico no fue proporcionado')

    total_price = session.get('total_price', "0.00")
    tarjeta_censurada = "**** **** **** " + session.get('numero_tarjeta', '0000')[-4:] if 'numero_tarjeta' in session else "No proporcionado"

    return render_template('exito.html', carrito=[product for product in PRODUCTS if product["name"] in session["cart"]],
                           nombre=nombre, apellido=apellido, telefono=telefono, direccion=direccion, email=email,
                           total_price=total_price, nombre_completo=f"{nombre} {apellido}", tarjeta_censurada=tarjeta_censurada)

if __name__ == '__main__':
    app.run(debug=True)
