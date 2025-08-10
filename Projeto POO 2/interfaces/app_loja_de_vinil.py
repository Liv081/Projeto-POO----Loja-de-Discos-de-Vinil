import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, ttk

# Importa as classes do pacote 'classes'
from Classes.classes import Cliente, Vendedor, DiscoVinil, ItemPedido, Pedido

# Importa os dados e as funções de persistência do pacote 'dados_iniciais'
from dados_iniciais.dados import clientes_cadastrados, vendedores_cadastrados, discos_disponiveis, salvar_dados, carregar_dados

class AppLojaVinil(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Loja de Vinil")
        self.geometry("500x300")

        self.criar_menu_principal()

    def criar_menu_principal(self):
       #Cria os botões na janela principal para navegar entre as funcionalidades.
        frame_menu = tk.Frame(self)
        frame_menu.pack(pady=20)

        label_titulo = tk.Label(frame_menu, text="Twilight - Discos de Vinil", font=("Helvetica", 16))
        label_titulo.pack(pady=10)

        btn_cad_cliente = tk.Button(frame_menu, text="Cadastrar Cliente", command=self.abrir_janela_cadastro_cliente, width=30)
        btn_cad_cliente.pack(pady=5)

        btn_cad_vendedor = tk.Button(frame_menu, text="Cadastrar Vendedor", command=self.abrir_janela_cadastro_vendedor, width=30)
        btn_cad_vendedor.pack(pady=5)

        btn_fazer_pedido = tk.Button(frame_menu, text="Fazer um Pedido", command=self.abrir_janela_fazer_pedido, width=30)
        btn_fazer_pedido.pack(pady=5)
        
        btn_visualizar_cadastros = tk.Button(frame_menu, text="Visualizar Cadastros", command=self.abrir_janela_visualizar, width=30)
        btn_visualizar_cadastros.pack(pady=5)

    def abrir_janela_cadastro_cliente(self):
       #Cria uma nova janela para o cadastro de clientes.
        janela_cliente = Toplevel(self)
        janela_cliente.title("Cadastro de Cliente")
        janela_cliente.geometry("400x200")

        frame = tk.Frame(janela_cliente, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

    #Grid para alinhamento
        tk.Label(frame, text="Cadastro de Novo Cliente", font=("Helvetica", 14, "bold")).grid(row=0, columnspan=2, pady=10)

        tk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        entry_nome = tk.Entry(frame, width=40)
        entry_nome.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(frame, text="E-mail:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        entry_email = tk.Entry(frame, width=30)
        entry_email.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(frame, text="Telefone:").grid(row=3, column=0, sticky="w", pady=5, padx=5)
        entry_telefone = tk.Entry(frame, width=30)
        entry_telefone.grid(row=3, column=1, pady=5, padx=5)

        def salvar_cliente():
            nome = entry_nome.get()
            email = entry_email.get()
            telefone = entry_telefone.get()
            if nome and email and telefone:
                novo_cliente = Cliente(nome, email, telefone)
                clientes_cadastrados.append(novo_cliente)
                salvar_dados() # Salva os dados após a alteração
                messagebox.showinfo("Sucesso", f"Cliente {novo_cliente.nome} cadastrado!")
                janela_cliente.destroy()
            else:
                messagebox.showerror("Erro", "Preencha todos os campos.")

        btn_salvar = tk.Button(frame, text="Salvar Cliente", command=salvar_cliente)
        btn_salvar.grid(row=4, columnspan=2, pady=15)

    def abrir_janela_cadastro_vendedor(self):
        #Cria uma nova janela para o cadastro de vendedores.
        janela_vendedor = Toplevel(self)
        janela_vendedor.title("Cadastro de Vendedor")
        janela_vendedor.geometry("400x200")

        frame = tk.Frame(janela_vendedor, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="Nome:", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w", pady=5, padx=5)
        entry_nome = tk.Entry(frame, width=40)
        entry_nome.grid(row=1, column=1, pady=5, padx=5)


        tk.Label(frame, text="E-mail:", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w", pady=5, padx=5)
        entry_email = tk.Entry(frame, width=40)
        entry_email.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(frame, text="Salário:", font=("Helvetica", 10)).grid(row=3, column=0, sticky="w", pady=5, padx=5)
        entry_salario = tk.Entry(frame, width=40)
        entry_salario.grid(row=3, column=1, pady=5, padx=5)


        def salvar_vendedor():
            nome = entry_nome.get()
            email = entry_email.get()
            salario_str = entry_salario.get()
            if nome and email and salario_str:
                try:
                    salario = float(salario_str)
                    novo_vendedor = Vendedor(nome, email, salario)
                    vendedores_cadastrados.append(novo_vendedor)
                    salvar_dados() # Salva os dados após a alteração
                    messagebox.showinfo("Sucesso", f"Vendedor {novo_vendedor.nome} cadastrado!")
                    janela_vendedor.destroy()
                except ValueError:
                    messagebox.showerror("Erro", "O salário deve ser um número válido.")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos.")

        btn_salvar = tk.Button(frame, text="Salvar Vendedor", command=salvar_vendedor, width=20)
        btn_salvar.grid(row=4, columnspan=2, pady=15)

    def abrir_janela_fazer_pedido(self):
        #Cria uma nova janela para o processo de fazer um pedido.
        if not clientes_cadastrados:
            messagebox.showerror("Erro", "Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
            return

        janela_pedido = Toplevel(self)
        janela_pedido.title("Fazer Pedido")
        janela_pedido.geometry("500x400")

        frame_principal = tk.Frame(janela_pedido, padx=20, pady=20)
        frame_principal.pack(fill="both", expand=True)

        # Seleção do Cliente
        frame_cliente = tk.Frame(frame_principal)
        frame_cliente.pack(fill="x", pady=(0, 15))
        tk.Label(frame_principal, text="Selecione o Cliente:", font=("Helvetica", 10, "bold")).pack(anchor="w")
        cliente_var = tk.StringVar(self)
        cliente_var.set(clientes_cadastrados[0].nome)
        menu_clientes = tk.OptionMenu(frame_principal, cliente_var, *[c.nome for c in clientes_cadastrados])
        menu_clientes.config(width=45)
        menu_clientes.pack(fill="x", pady=5)

        # Itens do Pedido
        tk.Label(frame_principal, text="Itens do Pedido:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(10, 5))
        frame_itens = tk.Frame(frame_principal)
        frame_itens.pack(fill="both", expand=True)

        #Adiciona barra de rolagem
        scrollbar = tk.Scrollbar(frame_itens)
        scrollbar.pack(side="right", fill="y")

        listbox_discos = tk.Listbox(frame_itens, selectmode=tk.MULTIPLE, height=10, yscrollcommand=scrollbar.set)
        listbox_discos.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=listbox_discos.yview)

        for disco in discos_disponiveis:
            listbox_discos.insert(tk.END, f"{disco.album} - R$ {disco.preco:.2f}")

        def concluir_pedido():
            cliente_selecionado = next((c for c in clientes_cadastrados if c.nome == cliente_var.get()), None)
            
            if not cliente_selecionado:
                messagebox.showerror("Erro", "Cliente não encontrado.")
                return

            pedido = Pedido(cliente_selecionado)
            
            itens_selecionados_indices = listbox_discos.curselection()
            if not itens_selecionados_indices:
                messagebox.showerror("Erro", "Nenhum item selecionado para o pedido.")
                return
                
            for index in itens_selecionados_indices:
                disco = discos_disponiveis[index]
                quantidade_str = simpledialog.askstring("Quantidade", f"Quantas unidades de '{disco.album}'?", parent=janela_pedido)
                try:
                    if quantidade_str:
                        quantidade = int(quantidade_str)
                        if quantidade > 0:
                            item = ItemPedido(disco, quantidade)
                            pedido.adicionar_item(item)
                        else:
                            messagebox.showwarning("Aviso", "A quantidade de discos deve ser maior que zero.")
                    else:
                        continue
                except ValueError:
                    messagebox.showerror("Erro", "Quantidade de discos inválida. Digite um número.")
                    return
            
            if not pedido.itens:
                messagebox.showwarning("Aviso", "Nenhum disco foi adicionado ao pedido.")
                return
                
            resumo_pedido = f"Pedido para: {pedido.cliente.nome}\n\n"
            resumo_pedido += "Itens:\n"
            for item in pedido.itens:
                resumo_pedido += f"  - {item.quantidade}x {item.produto.album} (Subtotal: R$ {item.subtotal():.2f})\n"
            resumo_pedido += f"\nTotal do Pedido: R$ {pedido.total():.2f}"
            
            messagebox.showinfo("Pedido Concluído", resumo_pedido)
            janela_pedido.destroy()

        btn_concluir = tk.Button(frame_principal, text="Concluir Pedido", command=concluir_pedido, width=30)
        btn_concluir.pack(pady=20)
        
    def abrir_janela_visualizar(self):
        #Cria uma janela para exibir os clientes e vendedores cadastrados.
        janela_visualizar = Toplevel(self)
        janela_visualizar.title("Visualizar Cadastros")
        janela_visualizar.geometry("600x400")
        
        notebook = ttk.Notebook(janela_visualizar)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Frame para Clientes
        frame_clientes = tk.Frame(notebook)
        notebook.add(frame_clientes, text="Clientes")
        
        tk.Label(frame_clientes, text="Clientes Cadastrados", font=("Helvetica", 12, "bold")).pack(pady=10)
        
        #Adicionando barra de rolagem
        scrollbar_clientes = tk.Scrollbar(frame_clientes)
        scrollbar_clientes.pack(side="right", fill="y")
        text_clientes = tk.Text(frame_clientes, wrap="word", yscrollcommand=scrollbar_clientes.set)
        text_clientes.pack(expand=True, fill="both", padx=10, pady=5)
        scrollbar_clientes.config(command=text_clientes.yview)

        for cliente in clientes_cadastrados:
            text_clientes.insert(tk.END, f"Nome: {cliente.nome}, E-mail: {cliente.email}, Telefone: {cliente.telefone}\n")
        text_clientes.config(state="disabled") # Torna o campo somente leitura
        
        # Frame para Vendedores
        frame_vendedores = tk.Frame(notebook)
        notebook.add(frame_vendedores, text="Vendedores")
        
        tk.Label(frame_vendedores, text="Vendedores Cadastrados", font=("Helvetica", 12, "bold")).pack(pady=10)

        #Adicionando barra de rolagem
        scrollbar_vendedores = tk.Scrollbar(frame_vendedores)
        scrollbar_vendedores.pack(side="right", fill="y")
        text_vendedores = tk.Text(frame_vendedores, wrap="word", yscrollcommand=scrollbar_vendedores.set)
        text_vendedores.pack(expand=True, fill="both", padx=10, pady=5)
        scrollbar_vendedores.config(command=text_vendedores.yview)

        for vendedor in vendedores_cadastrados:
            text_vendedores.insert(tk.END, f"Nome: {vendedor.nome},\n E-mail: {vendedor.email}, \n Salário: R$ {vendedor.salario:.2f}\n")
        text_vendedores.config(state="disabled") # Torna o campo somente leitura
