# 9)Tipos de Notificação: Você está criando um sistema que envia notificações para os usuários. 
# As notificações podem ser enviadas por E-mail ou por SMS, e o formato da mensagem muda.
# Crie uma classe Notificacao com um atributo mensagem e um método enviar() que, por padrão, lança uma exceção NotImplementedError, forçando as subclasses a implementá-lo. 
# Crie duas subclasses: NotificacaoEmail e NotificacaoSMS. Em NotificacaoEmail, o método enviar() deve imprimir "E-mail enviado: {mensagem}". 
# Em NotificacaoSMS, deve imprimir "SMS enviado: {mensagem}".

class Notificacao:
  def __init__(self, mensagem):
        self.mensagem = mensagem

  def enviar(self):
       
        raise NotImplementedError("O método enviar() deve ser implementado na subclasse")


class NotificacaoEmail(Notificacao):
    def enviar(self):
        print(f"E-mail enviado: {self.mensagem}")


class NotificacaoSMS(Notificacao):
    def enviar(self):
        print(f"SMS enviado: {self.mensagem}")



