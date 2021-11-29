from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from Dominio.Libro import Libro
from Dominio.Comic import Comic
from Dominio.Revista import Revista
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'
mysql = MySQL(app)

app.secret_key = "mysecretkey"

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libros')
    dataLibros = cur.fetchall()
    cur.execute('SELECT * FROM revistas')
    dataRevistas = cur.fetchall()
    cur.execute('SELECT * FROM comics')
    dataComics = cur.fetchall()
    print(dataLibros)
    print(dataRevistas)
    print(dataComics)
    cur.close()
    return render_template('index.html', libros = dataLibros, revistas = dataRevistas, comics = dataComics)


@app.route('/add_libro', methods=['POST'])
def addLibro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        editorial = request.form['editorial']
        l = Libro(nombre,autor,editorial)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO libros (id, nombre, autor, editorial) VALUES (%s,%s,%s,%s)", (l.id_libro, l.nombre,l.autor,l.editorial))
        mysql.connection.commit()
        flash('Libro Guardado Exitosamente')
        return redirect(url_for('Index'))
@app.route('/edit_libro/<id>')
def get_Libro(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libros WHERE id = %s',[id])
    data = cur.fetchall()
    cur.close()
    return render_template('edit-libro.html', libro=data[0])
@app.route('/update_libro/<id>', methods=['POST'])
def update_libro(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        editorial = request.form['editorial']
        l = Libro(nombre,autor,editorial)
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE libros
            SET nombre = %s,
                autor = %s,
                editorial = %s
            WHERE id = %s
        """, (l.nombre,l.autor,l.editorial, id))
        flash('Libro Actualizado Exitosamente')
        mysql.connection.commit()
        return redirect(url_for('Index'))
@app.route('/delete_libro/<string:id>', methods = ['POST','GET'])
def deleteLibro(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM libros WHERE id = %s',[id])
    mysql.connection.commit()
    flash('Libro Eliminado Exitosamente')
    return redirect(url_for('Index'))




@app.route('/add_revista', methods=['POST'])
def addRevista():
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        edicion = request.form['edicion']
        r = Revista(nombre,autor,edicion)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO revistas (id, nombre, autor, edicion) VALUES (%s,%s,%s,%s)", (r.id_revista, r.nombre,r.autor,r.edicion))
        mysql.connection.commit()
        flash('Revista Guardado Exitosamente')
        return redirect(url_for('Index'))
@app.route('/edit_revista/<id>')
def get_revista(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM revistas WHERE id = %s',[id])
    data = cur.fetchall()
    cur.close()
    return render_template('edit-revista.html', revista=data[0])
@app.route('/update_revista/<id>', methods=['POST'])
def update_revista(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        edicion = request.form['edicion']
        r = Revista(nombre,autor,edicion)
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE revistas
            SET nombre = %s,
                autor = %s,
                edicion = %s
            WHERE id = %s
        """, (r.nombre,r.autor,r.edicion, id))
        flash('Revista Actualizado Exitosamente')
        mysql.connection.commit()
        return redirect(url_for('Index'))
@app.route('/delete_revista/<string:id>', methods = ['POST','GET'])
def deleteRevista(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM revistas WHERE id = %s',[id])
    mysql.connection.commit()
    flash('Revista Eliminado Exitosamente')
    return redirect(url_for('Index'))


@app.route('/add_comic', methods=['POST'])
def addComic():
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        numero = request.form['numero']
        c = Comic(nombre,autor,numero)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO comics (id, nombre, autor, numero) VALUES (%s,%s,%s,%s)", (c.id_comic, c.nombre,c.autor,c.numero))
        mysql.connection.commit()
        flash('Comic Guardado Exitosamente')
        return redirect(url_for('Index'))
@app.route('/edit_comic/<id>')
def get_comic(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM comics WHERE id = %s',[id])
    data = cur.fetchall()
    cur.close()
    return render_template('edit-comic.html', comic=data[0])
@app.route('/update_comic/<id>', methods=['POST'])
def update_comic(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        numero = request.form['numero']
        c = Comic(nombre,autor,numero)
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE comics
            SET nombre = %s,
                autor = %s,
                numero = %s
            WHERE id = %s
        """, (c.nombre,c.autor,c.numero, id))
        flash('Comic Actualizado Exitosamente')
        mysql.connection.commit()
        return redirect(url_for('Index'))
@app.route('/delete_comic/<string:id>', methods = ['POST','GET'])
def deleteComic(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM comics WHERE id = %s',[id])
    mysql.connection.commit()
    flash('Comic Eliminado Exitosamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)