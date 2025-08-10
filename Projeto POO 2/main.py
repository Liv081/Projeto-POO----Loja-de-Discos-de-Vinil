import tkinter as tk
from interfaces.app_loja_de_vinil import AppLojaVinil
from dados_iniciais.dados import carregar_dados, salvar_dados

def fechar_aplicacao(app):
    #Função chamada ao fechar a janela para salvar os dados.
    salvar_dados()
    app.destroy()

if __name__ == "__main__":
    carregar_dados()  # Carrega os dados do arquivo ao iniciar
    app = AppLojaVinil()
    app.protocol("WM_DELETE_WINDOW", lambda: fechar_aplicacao(app)) # Chama a função de salvamento ao fechar
    app.mainloop()