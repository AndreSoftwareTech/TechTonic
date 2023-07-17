from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Pessoa, Usuarios




#============================================================================================================================
#variavel de referencia ao flask 
app = Flask(__name__)

# encriptar o passwords do usuário
app.secret_key = 'moredevs'

#string conexao
SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\Andre Vitor\\Documents\\repositorios\\Python\\TechTonic\\modulo03\\aplication.sqlite3'



#================================================================================
db = SQLAlchemy(app)


#=========================================================================
lista = Pessoa.query.order_by(Pessoa.id)


@app.route('/')
def index():

    lista = Pessoa.query.order_by(Pessoa.id)

    #render template acessa nosso html, variavel titulo recebendo valor e sendo acessada via html.
    return render_template("lista.html", titulo = 'pessoas', pessoas = lista)



#return redirect('/login')
@app.route('/novo2')
def novo():

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        
        #recurso querystring
        return redirect(url_for('login2', proximo= url_for('novo2')))

    return render_template('novo.html', titulo='Novo Jogo')




@app.route('/criar2', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['categoria']
    idade = request.form['console']
    #variavel nova recebendo classe jogo e filtrando pelo nome
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    # if condicional recebendo a variavel caso exista jogos cadastrados 
    if pessoa:
        flash('Pessoa Ja Existente!')
        return redirect(url_for('index'))

    #variavel criada recebendo variaveis e as variaveis refente ao form
    nova_pessoa = Pessoa(nome=nome, idade=idade, console=idade)
    #acessando variavel db e o recurso session e adicionando dados a variavel novo jogo 
    db.session.add(nova_pessoa)
    #acessando variavel db e o recurso session e comitando dados no banco
    db.session.commit()
    #redirecionamento para lista de jogos
    return redirect(url_for('index'))


@app.route('/login2')
def login():

        proximo = request.args.get('proximo')

        return render_template('login.html', proximo=proximo)




@app.route('/autenticar2', methods=['POST',])
def autenticar():

    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    
    if usuario:
        
        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.nickname
            

            flash(usuario.nickname + 'logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)

    else:
        flash('usuario ou senha incorretos tente novamente')
        #dinamizando url

        return redirect(url_for('login'))


@app.route('/logout2')
def logout():
    session['usuario_logado'] = None
    flash('voce foi Desconectado')

    return redirect(url_for('login'))




app.run(debug=True)