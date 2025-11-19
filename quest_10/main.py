from usuario import Usuario, Administrador


usuario = Usuario("Miguel")
administrador= Administrador("José")

 
print(f"{usuario.username}: {usuario.verificar_permissoes()}")
print(f"{administrador.username}: {administrador.verificar_permissoes()}")





   
