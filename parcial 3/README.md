Descripción de la aplicación
--Esta es una aplicación simple de lista de libros de una biblioteca desarrollada con Flask y MySQL. Permite a los usuarios crear, ver los libros,  eliminar libros.

Requisitos
--Python 3
--Flask
--MySQL Connector Python
instalación
--1.Clonar el repositorio:
---git clone https://github.com/Bard/flask-todo-app.git
--2.Cambiar al directorio del proyecto:
---cd flask-todo-app
--3.Crear un archivo virtual:
---python3 -m venv venv
--4.Activar el archivo virtual:
---source venv/bin/activate
--5.Instalar las dependencias:
---pip install -r requirements.txt
Para configurar la aplicación, edite el archivo app/config.py. Necesitará proporcionar la siguiente información:
--SQLALCHEMY_DATABASE_URI: La cadena de conexión a la base de datos MySQL.
Ejecución de la aplicación
--Para ejecutar la aplicación, ejecute el siguiente comando:
---flask run
La aplicación se ejecutará en el puerto 5000 de forma predeterminada. Puede acceder a la aplicación en su navegador web en la siguiente dirección:
--http://localhost:5000
Uso de la aplicación
--Para ingresar un nuevo libro, ingrese el nombre, autor, editorial, año del libro en los campos de texto y haga clic en el botón "Agregar".
--Para eliminar un libro, haga clic en el botón "Eliminar" junto al libro.