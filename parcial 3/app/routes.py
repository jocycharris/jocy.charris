from config import connection
from flask import render_template, request, redirect, url_for
from init import app
from config import cursor


# Mostrar todos los libros
@app.route('/')
def index():
    cursor.execute('SELECT * FROM biblioteca.libros')
    books = cursor.fetchall()
    return render_template('index.html', books=books)

# Agregar un nuevo libro
@app.route('/add', methods=['POST'])
def add_book():
    # Obtener datos del formulario
    book_name = request.form['book_name']
    book_author = request.form['book_author']
    book_editorial = request.form['book_editorial']
    book_year = request.form['book_year']

    # Insertar el nuevo libro en la base de datos
    cursor.execute(
        'INSERT INTO biblioteca.libros (nombre, autor, editorial, año) VALUES (%s, %s, %s, %s)',
        (book_name, book_author, book_editorial, book_year)
    )
    connection.commit()

    return redirect(url_for('index'))

# Eliminar un libro
@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    cursor.execute('DELETE FROM biblioteca.libros WHERE id_libro = %s', (book_id,))
    connection.commit()

    return redirect(url_for('index'))



