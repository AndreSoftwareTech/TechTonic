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

    cursor.execute('CREATE TABLE pessoa (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(15) NOT NULL, idade INTEGER NOT NULL, altura VARCHAR(20) NOT NULL);')
    print('Sua tabela pessoa foi criada!')

    # cursor.execute('CREATE TABLE usuarios (nome VARCHAR(15) NOT NULL, nickname VARCHAR(30) PRIMARY KEY NOT NULL, senha VARCHAR(30) NOT NULL);')
    # print('Sua tabela usuarios foi criada!')

    conn.commit()
    cursor.close()
    conn.close()
