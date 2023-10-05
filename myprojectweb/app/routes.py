from config import connection
from flask import render_template, request, redirect, url_for
from init import app
from config import cursor


@app.route('/')
def index():
    cursor.execute('SELECT * FROM mydb.tareas')
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

# nueva tarea


@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    cursor.execute(
              
        'INSERT INTO mydb.tareas (descripcion, estado) VALUES (%s, %s)', (task_name, False))
    connection.commit()
    return redirect(url_for('index'))

#  hecha o no hecha


@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    cursor.execute('SELECT estado FROM mydb.tareas WHERE id_tareas = %s', (task_id,))
    task = cursor.fetchone()
    if task:
        new_done = not task[0]
        cursor.execute(
            'UPDATE mydb.tareas SET estado = %s WHERE id_tareas = %s', (new_done, task_id))
        connection.commit()
    return redirect(url_for('index'))

#  eliminar una tarea


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    cursor.execute('DELETE tareas FROM mydb.tareas WHERE id_tareas = %s', (task_id,))
    connection.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)