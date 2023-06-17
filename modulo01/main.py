from flask import Flask, render_template, request, redirect, session, flash
from modulo01.pessoa import Pessoa

# Importacao e ultilizacao da nossa clase pessoa
pessoa1 = Pessoa("Luciano", "18", "1.80")
pessoa2 = Pessoa("Jose", "35", "1.81")
pessoa3 = Pessoa("Marcelinho", "19", "1.60")
pessoa4 = Pessoa("Andre", "25", "1.80")

lista = [pessoa1, pessoa2, pessoa3, pessoa4]


# tudo que depende do nosso framework, deve estar abaixo do objeto da classe Flask
app = Flask(__name__)
app.secret_key = "123456"

@app.route("/")
def inicio():
    return render_template('index.html', titulo = 'Home', pessoas = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = "Cadastro")

@app.route('/criar', methods=['POST',])
def criar():

    nome = request.form["nome" ]
    idade = request.form["idade"]
    altura = request.form["altura"]

    pessoas = Pessoa(nome, idade, altura)

    lista.append(pessoas)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Softaware Tech')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '123456' == request.form['senha']:
        session['usuario_Logado'] = request.form['usuario']
        flash(session['usuario_Logado'] + 'Voce Esta Logado')
        return redirect("/")
    else:
        flash("Senha incorreta")
        return redirect('/login')
@app.route('/logout')   
def logout():
    session['usuario_Logado'] == None
    flash('Voce Foi Desconectado')
    return redirect('/login')

app.run(debug=True)