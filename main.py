# Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from tkcalendar import DateEntry

# Importação
from view import *
global tree

# Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # sky blue

# Janela
janela = Tk()
janela.title("")
janela.geometry('1061x465')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

# Configurando a Janela
frame_cima = Frame(janela, width=330, height=60, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=330, height=400, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=1280, height=465, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, sticky=NSEW)

# Label Cima
app_nome = Label(frame_cima,text='Formulário de Consultoria', anchor=NW, font=('Arial 14 bold'), # Configurando Interface
                  bg=co2, fg=co1, relief='flat')
app_nome.place(x=38, y=17)

# Função Inserir
def Inserir_info():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    data = e_data.get()
    estado = e_estado.get()
    sobre = e_sobre.get()

    lista = [nome, email, telefone, data, estado, sobre]

    if nome=='':
        messagebox.showerror('ERROR','O nome não pode ser vazio.')
    else:
        Inserir(lista)
        messagebox.showinfo('Sucesso','Os dados foram inseridos com Sucesso!')

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_data.delete(0,'end')
        e_estado.delete(0,'end')
        e_sobre.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

# Função Atualizar
def Atualizar_info():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        valor = tree_lista[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_data.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_sobre.delete(0, 'end')

        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_telefone.insert(0, tree_lista[3])
        e_data.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_sobre.insert(0, tree_lista[6])

    except IndexError:
        messagebox.showerror('ERROR', 'Selecione um dos dados na tabela')

    def Update():
        nome = e_nome.get()
        email = e_email.get()
        telefone = e_telefone.get()
        data = e_data.get()
        estado = e_estado.get()
        sobre = e_sobre.get()

        lista = [nome, email, telefone, data, estado, sobre, valor]

        if nome == '':
            messagebox.showerror('ERROR', 'O nome não pode ser vazio.')
        else:
            Atualizar(lista)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com Sucesso!')
            e_nome.delete(0, 'end')
            e_email.delete(0, 'end')
            e_telefone.delete(0, 'end')
            e_data.delete(0, 'end')
            e_estado.delete(0, 'end')
            e_sobre.delete(0, 'end')
        for widget in frame_direita.winfo_children():
            widget.destroy()
        mostrar()

    # Botão Atualizar
    b_confirmar = Button(frame_baixo, command=Update, text='Confirmar', width=8, font=('Arial 10 bold'),
                             bg=co2, fg=co1, relief='raised', overrelief='ridge')
    b_confirmar.place(x=128, y=370)

# Função Deletar
def Deletar_info():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        valor = tree_lista[0]

        Deletar([valor])

        messagebox.showinfo('SUCESSO', 'Os dados foram deletados com Sucesso!')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('ERROR', 'Selecione um dos dados na tabela')

# Label Baixo
l_nome = Label(frame_baixo,text='Nome', anchor=NW, font=('Arial 12 bold'), # Nome
                  bg=co0, fg=co4, relief='flat')
l_nome.place(x=10, y=15)
e_nome = Entry(frame_baixo, width=51, justify='left', relief='solid')
e_nome.place(x=10, y=42)

# E-mail
l_email = Label(frame_baixo,text='E-mail', anchor=NW, font=('Arial 12 bold'),
                  bg=co0, fg=co4, relief='flat')
l_email.place(x=10, y=80)
e_email = Entry(frame_baixo, width=51, justify='left', relief='solid')
e_email.place(x=10, y=105)

# Telefone
l_telefone = Label(frame_baixo,text='Telefone', anchor=NW, font=('Arial 12 bold'),
                  bg=co0, fg=co4, relief='flat')
l_telefone.place(x=10, y=140)
e_telefone= Entry(frame_baixo, width=51, justify='left', relief='solid')
e_telefone.place(x=10, y=165)

# Data da Consulta
l_data = Label(frame_baixo,text='Data da Consulta', anchor=NW, font=('Arial 12 bold'),
                  bg=co0, fg=co4, relief='flat')
l_data.place(x=10, y=200)
e_data = DateEntry(frame_baixo, width=10, background='darkblue', foreground='white', borderwidth=2)
e_data.place(x=10, y=225)

# Estado
l_estado = Label(frame_baixo,text='Estado da Consulta', anchor=NW, font=('Arial 12 bold'),
                  bg=co0, fg=co4, relief='flat')
l_estado.place(x=165, y=200)
e_estado = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_estado.place(x=166, y=225)

# Sobre
l_sobre = Label(frame_baixo,text='Informação Extra', anchor=NW, font=('Arial 12 bold'),
                  bg=co0, fg=co4, relief='flat')
l_sobre.place(x=10, y=270)
e_sobre = Entry(frame_baixo, width=51, justify='left', relief='solid')
e_sobre.place(x=10, y=295)

# Botão Inserir
b_inserir = Button(frame_baixo, command=Inserir_info , text='Inserir', width=8, font=('Arial 12 bold'),
                   bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=10,y=335)

# Botão Atualizar
b_atualizar = Button(frame_baixo,command=Atualizar_info,text='Atualizar', width=8, font=('Arial 12 bold'),
                   bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=120,y=335)

# Botão Deletar
b_deletar = Button(frame_baixo,command=Deletar_info, text='Deletar', width=8, font=('Arial 12 bold'),
                   bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=231,y=335)

# Frame Direita
def mostrar():
    global tree

    lista = Ler()

    # Lista Cabeçario
    tabela_head = ['ID', 'Nome', 'E-mail', 'telefone', 'Data', 'Estado', 'Sobre']

    # Criando a Tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)

# Função Mostrar
mostrar()

janela.mainloop()