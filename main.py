from flask import Flask, render_template, request
from flask import g
from flask_wtf.csrf import CSRFProtect
from flask import flash
import forms

app=Flask(__name__)
app.secret_key="Llave secreta"
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    g.nombre="Omar"
    print("Antes de la petición")
    
@app.after_request
def after_request(response):
    print("Después de la petición")
    return response

@app.route('/Alumnos',methods=['POST','GET'])
def alumnos():
    mat=""
    nom=""
    edad=""
    correo=""
    ape=""
    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        edad=alumnos_clase.edad.data
        correo=alumnos_clase.email.data
        ape=alumnos_clase.apellidos.data
        mensaje="Bienvenido {}!!!".format(nom)
        flash(mensaje,"success")
    return render_template('Alumnos.html',form=alumnos_clase,mat=mat,nom=nom,edad=edad,correo=correo,ape=ape)

@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Omar","Luis","Jorge","Erick","Javier"]
    print("Index 2")
    print("Hola {}".format(g.nombre))
    return render_template('index.html',grupo=grupo,lista=lista)

#@app.route('/OperasBas')
#def OperasBas():
#return render_template('OperasBas.html')

@app.route('/OperasBas',methods=['POST','GET']) 
def OperasBas():
    if request.method=='POST':
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        resultado=int(num1)+int(num2)
        return render_template('OperasBas.html',resultado=resultado)
    else:
        return render_template('OperasBas.html')

@app.route('/cinepolis',methods=['POST','GET'])
def cinepolis():
    if request.method=='POST':
        boletos=int(request.form.get("boletos",0))
        tarjeta=request.form.get("tarjeta","no")
        compradores=int(request.form.get("compradores",1))
        if boletos / compradores > 7:
            return render_template('accionesCnp.html', resultado=" Máximo 7 boletos por persona.")
        if boletos>5 and tarjeta=="si":
            resultado=((boletos*12)*.85)*.90 
            return render_template('accionesCnp.html',resultado=" " + str(round(resultado,2)) + "$")
        elif boletos>5 and tarjeta=="no":
            resultado=(boletos*12)*.85
            return render_template('accionesCnp.html',resultado=" " + str(round(resultado,2)) + "$")
        if 3 <= boletos <= 5 and tarjeta=="si":
            resultado=((boletos*12)*.90)*.90
            return render_template('accionesCnp.html',resultado=" " + str(round(resultado,2)) + "$")
        elif 3 <= boletos <= 5 and tarjeta=="no":
            resultado=(boletos*12)*.90
            return render_template('accionesCnp.html',resultado=" " + str(round(resultado,2)) + "$")
        if boletos<3 and tarjeta=="si":
            resultado=(boletos*12)*.90
            return render_template('accionesCnp.html',resultado=" " + str(round(resultado,2)) + "$")
        if boletos<3 and tarjeta=="no":
            resultado=(boletos*12)
            return render_template('accionesCnp.html',resultado=" " + str(round(resultado,2)) + "$")
    else:
        return render_template('accionesCnp.html')
 
@app.route('/ejemplo1')
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')
def ejemplo2():
    return render_template('ejemplo2.html')

@app.route('/hola')
def hola():
    return"!!!Hola"

@app.route('/user/<string:user>')
def user(user):
    return"Hola "+user  
    #return f"Hola {user}"

@app.route('/numeri/<int:n>')
def numeri(n):
    return f"Numero {n}"

@app.route('/user/<string:user>/<int:id>')
def username(user,id):
    return f"Nombre: {user} ID: {id}!!!"

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return "La suma es: {}!!!".format(n1+n2) 

@app.route("/default")   
@app.route("/default/string:nom")
def function(nom="Omar"):
    return "Hola {}".format(nom) 

@app.route("/form1")  
def form1():
    return'''
            <form>
            <label>Nombre:</label>
            <input type="text" name="nombre" placeholder="Nombre></input>
            </form>
        '''

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True,port=3000)