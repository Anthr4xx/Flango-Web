# Flango Web - Tienda en Línea

## Descripción

Flango Web es una tienda en línea desarrollada con Flask.  
Permite a los usuarios seleccionar productos, gestionar su carrito, confirmar la compra, ingresar datos de envío y visualizar un resumen final.  
También ofrece la opción de generar un comprobante en PDF con los detalles de la compra.

---

## Características

- Página de inicio con botón de acceso a la tienda.
- Selección de productos con opción de agregar o eliminar del carrito.
- Resumen del carrito con detalles de los productos y total de la compra.
- Formulario para ingresar datos de envío y pago.
- Página de confirmación con revisión final de la compra.
- Página de éxito con resumen y opción para descargar un comprobante en PDF.

---

## Instalación y Ejecución

Este proyecto puede instalarse utilizando Pipenv o pip con venv.

### Opcion 1: Usando Pipenv (Recomendado)

1. Instalar Pipenv (si no está instalado):

   `pip install pipenv`

2. Instalar las dependencias:

   `pipenv install --deploy`

3. Activar el entorno virtual:

   `pipenv shell`

4. Ejecutar la aplicación:

   `python app.py`

5. Acceder a la aplicación en el navegador:

     `http://127.0.0.1:5000/`

---

### Opcion 2: Usando pip y venv

1. Crear un entorno virtual:

   `python -m venv venv`

2. Activar el entorno virtual:

    ` venv\Scripts\activate`
   
3. Instalar las dependencias:

   `pip install -r requirements.txt`

4. Ejecutar la aplicación:

   `python app.py`

5. Acceder a la aplicación en el navegador:

   `http://127.0.0.1:5000/`

---