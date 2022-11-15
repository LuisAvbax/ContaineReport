from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

# Conexion MySQL
app.config['MYSQL_HOST'] = 'localhost' # servidor
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'prueba'

conexion = MySQL(app)


@app.before_request
def before_request():
    print("Antes de la peticion...")

@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response

@app.route('/')
def index():
    # return "Holaaaa"
    nombres = ['Miguel','Carlos','Sofia','Salvador']
    data ={ #diccionario
        'titulo': 'Index123',
        'bienvenida': 'saludos',
        'nombres' :nombres,
        'numero_nombres':len(nombres)

    }
    return render_template('index.html', data=data) #RENDERIZACION DE UNA PLANTILLA


@app.route('/contacto/<nombre>/<int:edad>') #contruccion de urls dinamicas a travez del paso de parametros 
def contacto(nombre,edad):
    data={
        'titulo':'contacto',
        'nombre':nombre,
        'edad':edad
    }
    return render_template('contacto.html',data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "ok"

@app.route('/cursos')
def listar_cursos():
    data={}
    try:
        cursor=conexion.connection.cursos()
        sql="SELECT codigo, nombre, creditos FROM curso ORDER BT nombre ASC"
        cursor.execute(sql)
        cursos=cursor.fetch()
        # print(cursos)
        data['cursos'] = cursos
        data['mensaje']='Exito'
    except Exception as ex:
            data['mensaje']='Error...'
    return jsonify(data)

def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))

if __name__=='__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True, port=5000)