from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return"Hola mundo!!! Nuevo"

@app.route('/hola')
def hola():
    return"!!!Hola"

@app.route('/user/<string:user>')
def user(user):
    return"Hola "+user  
    return f"Hola {user}"

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


if __name__ == '__main__':
    app.run(debug=True,port=3000)