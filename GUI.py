#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
import tkinter.font
colorBlue = '#4169e1'
colorYellow = '#ffd700'
colorRed = '#a00'
colorWhite = '#FFFFFF'
colorBlack = '#000'
tk = tkinter
root = tk.Tk()
font = tkinter.font.Font(size=8)
#header = tk.Frame(root, bg ='#f5f5f5', width=100, height=20)
sidebarLeft = tk.Frame(root, bg =colorWhite, width=100)
sidebarRight = tk.Frame(root, bg =colorWhite, width=100)
footer = tk.Frame(sidebarRight, bg =colorWhite, width=100)
origemBox = tk.Frame(sidebarRight, bg=colorWhite, width=50, height=5)
destinoBox = tk.Frame(sidebarRight, bg=colorWhite, width=50, height=5)
textBox = tk.Frame(sidebarRight, bd=0, bg='#ffffff', width=100,height=330, pady=20)
buttonsBox = tk.Frame(sidebarLeft, bg='#4169e1')

textBox.grid(row=2,column=0,padx=10, pady=10, columnspan=2, sticky='news')

#header.grid(row=0, column=0, sticky='news')
sidebarLeft.grid(row=1, column=0, sticky='news')
sidebarRight.grid(row=1, column=1, sticky='news')

enderecoOrigem = tk.Label(origemBox, text='Origem', bg=colorWhite, font=tkinter.font.Font(size=10, weight='bold'))
enderecoOrigem.grid(row=0, column=0, sticky='w')
enderecoOrigemCEP = tk.Label(origemBox, text='CEP:', bg=colorWhite)
enderecoOrigemCEP.grid(row=1, column=0, sticky='w')
enderecoOrigemUF = tk.Label(origemBox, text='UF:', bg=colorWhite)
enderecoOrigemUF.grid(row=2, column=0, sticky='w')
enderecoOrigemCidade = tk.Label(origemBox, text='Cidade:', bg=colorWhite)
enderecoOrigemCidade.grid(row=3, column=0, sticky='w')
enderecoOrigemBairro = tk.Label(origemBox, text='Bairro:', bg=colorWhite)
enderecoOrigemBairro.grid(row=4, column=0, sticky='w')
enderecoOrigemLogradouro = tk.Label(origemBox, text='Logradouro:', bg=colorWhite)
enderecoOrigemLogradouro.grid(row=5, column=0, sticky='w')
origemBox.grid(row=1, column=0, sticky='w')

enderecoDestino = tk.Label(destinoBox, text='Destino', bg=colorWhite, font=tkinter.font.Font(size=10, weight='bold'))
enderecoDestino.grid(row=0, column=0, sticky='w')
enderecoDestinoCEP = tk.Label(destinoBox, text='CEP:', bg=colorWhite)
enderecoDestinoCEP.grid(row=1, column=0, sticky='w')
enderecoDestinoUF = tk.Label(destinoBox, text='UF:', bg=colorWhite)
enderecoDestinoUF.grid(row=2, column=0, sticky='w')
enderecoDestinoCidade = tk.Label(destinoBox, text='Cidade:', bg=colorWhite)
enderecoDestinoCidade.grid(row=3, column=0, sticky='w')
enderecoDestinoBairro = tk.Label(destinoBox, text='Bairro:', bg=colorWhite)
enderecoDestinoBairro.grid(row=4, column=0, sticky='w')
enderecoDestinoLogradouro = tk.Label(destinoBox, text='Logradouro:', bg=colorWhite)
enderecoDestinoLogradouro.grid(row=5, column=0, sticky='w')
destinoBox.grid(row=1, column=1)


# rodape
working = tk.Label(footer, bg=colorWhite, height=2, width=100)
working.grid(row=0, column=0)
bannerRodape = tk.Label(footer, text='Desenvolvido por WebCI Soluções Web', bg=colorWhite)
bannerRodape.grid(row=1,column=0, stick='e')
footer.grid(row=3, column=0, columnspan=2, sticky='en')

lab = tk.Label(textBox, text='Serviço', bg='#ffffff', bd=5, font=tkinter.font.Font(weight='bold', size=9))
lab['activeforeground'] = '#222'
lab['activebackground'] = '#ffffff'
lab['justify'] = 'left'
lab.grid(row=0, column=0, sticky='w', padx=2)

lab = tk.Label(textBox, text='Valor', bg='#ffffff', bd=5, font=tkinter.font.Font(weight='bold', size=9))
lab['activeforeground'] = '#222'
lab['activebackground'] = '#ffffff'
lab['justify'] = 'left'
lab.grid(row=0, column=1, sticky='w', padx=2)

lab = tk.Label(textBox, text='Prazo de Emtrega', bg='#ffffff', bd=5, font=tkinter.font.Font(weight='bold', size=9))
lab['activeforeground'] = '#222'
lab['activebackground'] = '#ffffff'
lab['justify'] = 'left'
lab.grid(row=0, column=2, sticky='w', padx=2)

lab = tk.Label(textBox, text='Valor da Mão Própria', bg='#ffffff', bd=5, font=tkinter.font.Font(weight='bold', size=9))
lab['activeforeground'] = '#222'
lab['activebackground'] = '#ffffff'
lab['justify'] = 'left'
lab.grid(row=0, column=3, sticky='w', padx=2)

lab = tk.Label(textBox, text='Valor Aviso', bg='#ffffff', bd=5, font=tkinter.font.Font(weight='bold', size=9))
lab['activeforeground'] = '#222'
lab['activebackground'] = '#ffffff'
lab['justify'] = 'left'
lab.grid(row=0, column=4, sticky='w', padx=2)

lab = tk.Label(textBox, text='Valor Declarado', bg='#ffffff', bd=5, font=tkinter.font.Font(weight='bold', size=9))
lab['activeforeground'] = '#222'
lab['activebackground'] = '#ffffff'
lab['justify'] = 'left'
lab.grid(row=0, column=5, sticky='w', padx=2)

lab = tk.Label(textBox, text='Entrega Domiciliar', bg='#ffffff', bd=5, font=tkinter.font.Font(weight='bold', size=9))
lab['activeforeground'] = '#222'
lab['activebackground'] = '#ffffff'
lab['justify'] = 'left'
lab.grid(row=0, column=6, sticky='w', padx=2)

lab = tk.Label(textBox, text='Entrega Sábado', bg='#ffffff', bd=5, font=tkinter.font.Font(weight='bold', size=9))
lab['activeforeground'] = '#222'
lab['activebackground'] = '#ffffff'
lab['justify'] = 'left'
lab.grid(row=0, column=7, sticky='w', padx=2)
