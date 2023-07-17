import sqlite3

print("Testando...")

try:
    conn = sqlite3.connect('aplication.sqlite3')
    print('VOCÊ ESTÁ CONECTADO...')
except Exception:
    print('VOCÊ ESTÁ SEM CONEXÃO...')

if conn is not None:
    print('Sua Conexão está estabilizada!')

    cursor = conn.cursor()

    cursor.execute('CREATE TABLE  pessoa (id serial, nome VARCHAR(15)NOT NULL, idade VARCHAR(15)NOT NULL, altura varchar(15) NOT NULL, PRIMARY KEY(id));')
    print('Sua tabela pessoa foi criada!')

    cursor.execute('CREATE TABLE usuarios  (nome VARCHAR(15) NOT NULL, nickname VARCHAR(30)NOT NULL, senha VARCHAR(30)NOT NULL,  PRIMARY KEY(nickname) );')
    print('Sua tabela usuario foi criada!')

    conn.commit()
    cursor.close()
    conn.close()
