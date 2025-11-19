# 10) Usuários de um Sistema: Um sistema web precisa diferenciar usuários comuns de administradores. Administradores têm permissões que usuários comuns não têm.
# Crie uma classe Usuario com um atributo username e um método verificar_permissoes() que retorna a string "Usuário com permissões de leitura." 
# Crie uma subclasse Administrador que herda de Usuario. 
# Sobrescreva o método verificar_permissoes() nesta subclasse para que ele retorne a string "Administrador com permissões totais (leitura, escrita e exclusão).".
# Faça um script main.py que crie uma instância de Usuario e uma de Administrador. 
# Chame o método verificar_permissoes() de cada um e imprima os resultados para garantir que cada tipo de usuário exiba a mensagem de permissão correta.

class Usuario:
    def __init__(self, username):
        self.username = username
    
    def verificar_permissoes(self):
        return "Usuário com permissões de leitura."

class Administrador(Usuario):
     def verificar_permissoes(self):
        return  "Administrador com permissões totais (leitura, escrita e exclusão)."    
