from notificacoes import NotificacaoEmail, NotificacaoSMS

# Criando notificações de tipos diferentes
notificacao_boas_vindas = NotificacaoEmail("Bem-vindo ao nosso sistema!")
notificacao_codigo = NotificacaoSMS("Seu código de verificação é 12345.")

# Enviando as notificações
def enviar_notificacao(notificacao):
    notificacao.enviar()

enviar_notificacao(notificacao_boas_vindas)
enviar_notificacao(notificacao_codigo)


