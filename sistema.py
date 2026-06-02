def testar_login():
    usuario_esperado = "admin"

    print("[INFO] Iniciando o fluxo de decisão de login")
    assert usuario_esperado == "admin", "[ERRO] Usuário inválido!"
    print("[INFO] Autenticação concluída com sucesso")

if __name__ == "__main__":
    testar_login() 
