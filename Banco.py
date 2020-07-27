import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        # idusuario integer primary key autoincrement
        c.execute("""create table if not exists usuarios (
                    idusuario primary key,
                    nome text,
                    telefone text,
                    email text,
                    usuario text,
                    senha text)""")
        self.conexao.commit()
        c.close()