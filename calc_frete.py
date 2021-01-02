#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import tkinter
import subprocess
import http.client
from xml.dom import minidom
import inspect
import string
import GUI
import address

class shipping:
    counter = 1
    op = tkinter.StringVar() #'CalcPrecoPrazoData'
    StrRetorno = tkinter.StringVar() #'xml'
    nCdServico = tkinter.StringVar() #41106
    servicos = {'PAC':'41106', 'SEDEX':'40010', 'SEDEX a Cobrar':'40045', 'SEDEX 10':'40215', 'SEDEX Hoje':'40290'}
    servicos2 = {'41106':'PAC', '40010':'SEDEX', '40045':'SEDEX a Cobrar', '40215':'SEDEX 10', '40290':'SEDEX Hoje'}
    sCepOrigem = tkinter.StringVar()
    sCepDestino = tkinter.StringVar()
    nVlPeso = tkinter.StringVar()
    nCdEmpresa = tkinter.StringVar() #0
    sDsSenha = tkinter.StringVar() #0
    nCdFormato = tkinter.StringVar() #1
    #sDtCalculo = tkinter.StringVar() #'12/05/2013'
    nVlAltura = tkinter.StringVar() #16
    nVlComprimento = tkinter.StringVar() #16
    nVlLargura = tkinter.StringVar() #16
    nVlDiametro = tkinter.StringVar() #16
    sCdMaoPropria = tkinter.StringVar() #'N'
    nVlValorDeclarado = tkinter.StringVar() #0
    sCdAvisoRecebimento = tkinter.StringVar() #'N'
    def __init__(self):
        sorted(self.servicos)
        colorBlue = '#4169e1'
        colorYellow = '#ffd700'
        colorGreen = '#d7ff00'
        colorRed = '#a00'
        colorWhite = '#fff'
        colorBlack = '#000'
        self.op.set('CalcPrecoPrazo')
        self.StrRetorno.set('xml')
        self.nCdEmpresa.set('08082650')
        self.sDsSenha.set('564321')
        self.nCdFormato.set(1)
        #self.sDtCalculo.set('12/05/2013')
        self.nVlValorDeclarado.set(0)
        # titulo da janela
        GUI.root.title('Cálculo de Frete - Correios.com.br')
        # input do CEP de origem
        labelCepOrig = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=0,text='CEP de origem',width=13,bg='#4169e1',fg=colorWhite,justify='left')
        labelCepOrig.grid(row=0, column=0)
        entryCepOrig = GUI.tk.Entry(GUI.buttonsBox, width = 10, textvariable = self.sCepOrigem)
        entryCepOrig['bd'] = 0
        entryCepOrig['bg'] = colorWhite
        entryCepOrig['fg'] = '#222'
        entryCepOrig['font'] = tkinter.font.Font()
        entryCepOrig.grid(row=1, column=0, padx=10, pady=5)
        # valor padrão
        strCepOrig = 'xxxxxxxx'
        self.sCepOrigem.set(strCepOrig)
        # ações para focus e blur
        entryCepOrig.bind("<FocusIn>", lambda a: self.sCepOrigem.set('') if self.sCepOrigem.get() == strCepOrig else None)
        entryCepOrig.bind("<FocusOut>", lambda b: self.sCepOrigem.set(strCepOrig) if self.sCepOrigem.get() == '' else None)
        # input do CEP de destino
        labelCepDest = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=0,text='CEP de destino',width=13,bg='#4169e1',fg=colorWhite,justify='left')
        labelCepDest.grid(row=2, column=0)
        entryCepDest = GUI.tk.Entry(GUI.buttonsBox, width = 10, textvariable = self.sCepDestino)
        entryCepDest['bd'] = 0
        entryCepDest['bg'] = colorWhite
        entryCepDest['fg'] = '#222'
        entryCepDest['font'] = tkinter.font.Font()
        entryCepDest.grid(row=3, column=0, padx=10, pady=5)
        # valor padrão
        strCepDest = 'xxxxxxxx'
        self.sCepDestino.set(strCepDest)
        # ações para focus e blur
        entryCepDest.bind("<FocusIn>", lambda c: self.sCepDestino.set('') if self.sCepDestino.get() == strCepDest else None)
        entryCepDest.bind("<FocusOut>", lambda d: self.sCepDestino.set(strCepDest) if self.sCepDestino.get() == '' else None)
        # input para o Peso
        labelPeso = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=0,text='Peso em gramas',width=13,bg='#4169e1',fg=colorWhite,justify='left')
        labelPeso.grid(row=4, column=0)
        entryPeso = GUI.tk.Entry(GUI.buttonsBox, width=10, textvariable=self.nVlPeso)
        entryPeso['bd'] = 0
        entryPeso['bg'] = colorWhite
        entryPeso['fg'] = '#222'
        entryPeso['font'] = tkinter.font.Font()
        entryPeso.grid(row=5,column=0,padx=0, pady=5)
        # valor padrão
        strPeso = '0.200'
        self.nVlPeso.set(strPeso)
        # ações para focus e blur
        entryPeso.bind("<FocusIn>", lambda c: self.nVlPeso.set('') if self.nVlPeso.get() == strPeso else None)
        entryPeso.bind("<FocusOut>", lambda d: self.nVlPeso.set(strPeso) if self.nVlPeso.get() == '' else None)
        # input para o Altura
        labelAltura = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=0,text='Altura em cm',width=13,bg='#4169e1',fg=colorWhite,justify='left')
        labelAltura.grid(row=6, column=0)
        entryAltura = GUI.tk.Entry(GUI.buttonsBox, width=10, textvariable=self.nVlAltura)
        entryAltura['bd'] = 0
        entryAltura['bg'] = colorWhite
        entryAltura['fg'] = '#222'
        entryAltura['font'] = tkinter.font.Font(size=12)
        entryAltura.grid(row=7,column=0,padx=10, pady=5)
        # valor padrão
        strAltura = '2'
        self.nVlAltura.set(strAltura)
        # ações para focus e blur
        entryAltura.bind("<FocusIn>", lambda c: self.nVlAltura.set('') if self.nVlAltura.get() == strAltura else None)
        entryAltura.bind("<FocusOut>", lambda d: self.nVlAltura.set(strAltura) if self.nVlAltura.get() == '' else None)
        # input para o Comprimento
        labelCepOrig = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=0,text='Comprimento em cm',width=13,bg='#4169e1',fg=colorWhite,justify='left')
        labelCepOrig.grid(row=8, column=0)
        entryComprimento = GUI.tk.Entry(GUI.buttonsBox, width=10, textvariable=self.nVlComprimento)
        entryComprimento['bd'] = 0
        entryComprimento['bg'] = colorWhite
        entryComprimento['fg'] = '#222'
        entryComprimento['font'] = tkinter.font.Font(size=12)
        entryComprimento.grid(row=9,column=0,padx=10, pady=5)
        # valor padrão
        strComprimento = '16'
        self.nVlComprimento.set(strComprimento)
        # ações para focus e blur
        entryComprimento.bind("<FocusIn>", lambda c: self.nVlComprimento.set('') if self.nVlComprimento.get() == strComprimento else None)
        entryComprimento.bind("<FocusOut>", lambda d: self.nVlComprimento.set(strComprimento) if self.nVlComprimento.get() == '' else None)
        # input para o Largura
        labelLargura = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=0,text='Largura em cm',width=13,bg='#4169e1',fg=colorWhite,justify='left')
        labelLargura.grid(row=10, column=0)
        entryLargura = GUI.tk.Entry(GUI.buttonsBox, width=10, textvariable=self.nVlLargura)
        entryLargura['bd'] = 0
        entryLargura['bg'] = colorWhite
        entryLargura['fg'] = '#222'
        entryLargura['font'] = tkinter.font.Font(size=12)
        entryLargura.grid(row=11,column=0,padx=10, pady=5)
        # valor padrão
        strLargura = '11'
        self.nVlLargura.set(strLargura)
        # ações para focus e blur
        entryLargura.bind("<FocusIn>", lambda c: self.nVlLargura.set('') if self.nVlLargura.get() == strLargura else None)
        entryLargura.bind("<FocusOut>", lambda d: self.nVlLargura.set(strLargura) if self.nVlLargura.get() == '' else None)
        # input para o Diâmetro
        labelDiametro = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=0,text='Diâmetro em cm',width=13,bg='#4169e1',fg=colorWhite,justify='left')
        labelDiametro.grid(row=12, column=0)
        entryDiametro = GUI.tk.Entry(GUI.buttonsBox, width=10, textvariable=self.nVlDiametro)
        entryDiametro['bd'] = 0
        entryDiametro['bg'] = colorWhite
        entryDiametro['fg'] = '#222'
        entryDiametro['font'] = tkinter.font.Font(size=12)
        entryDiametro.grid(row=13,column=0,padx=10, pady=5)
        # valor padrão
        strDiametro = '0'
        self.nVlDiametro.set(strDiametro)
        # ações para focus e blur
        entryDiametro.bind("<FocusIn>", lambda c: self.nVlDiametro.set('') if self.nVlDiametro.get() == strDiametro else None)
        entryDiametro.bind("<FocusOut>", lambda d: self.nVlDiametro.set(strDiametro) if self.nVlDiametro.get() == '' else None)
        # input para o Valor Declarado
        labelValorDeclarado = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=0,text='Valor declarado \nem R$',width=13,bg='#4169e1',fg=colorWhite,justify='left')
        labelValorDeclarado.grid(row=14, column=0)
        entryValorDeclarado = GUI.tk.Entry(GUI.buttonsBox, width=10, textvariable=self.nVlValorDeclarado)
        entryValorDeclarado['bd'] = 0
        entryValorDeclarado['bg'] = colorWhite
        entryValorDeclarado['fg'] = '#222'
        entryValorDeclarado['font'] = tkinter.font.Font(size=16)
        entryValorDeclarado.grid(row=15,column=0,padx=10, pady=5)
        # valor padrão
        strValorDeclarado = '0'
        self.nVlValorDeclarado.set(strValorDeclarado)
        # ações para focus e blur
        entryValorDeclarado.bind("<FocusIn>", lambda c: self.nVlValorDeclarado.set('') if self.nVlValorDeclarado.get() == strValorDeclarado else None)
        entryValorDeclarado.bind("<FocusOut>", lambda d: self.nVlValorDeclarado.set(strValorDeclarado) if self.nVlValorDeclarado.get() == '' else None)
        # input para o Mão Própria
        checkMaoPropria = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=3,text='Mão própria [N]',width=13,bg=colorWhite,fg=colorBlack,justify='center')
        checkMaoPropria.grid(row=16, column=0)
        checkMaoPropria['borderwidth'] = 0
        checkMaoPropria['activeforeground'] = colorBlack
        checkMaoPropria['activebackground'] = colorWhite
        checkMaoPropria['highlightbackground'] = colorWhite
        checkMaoPropria['relief'] = None
        checkMaoPropria['font'] = tkinter.font.Font(size=10)
        checkMaoPropria.grid(row=17,column=0,padx=0, pady=5)
        checkMaoPropria.bind('<ButtonRelease-1>', lambda a: self.mPropria(checkMaoPropria))
        # valor padrão
        strMaoPropria = 'N'
        self.sCdMaoPropria.set(strMaoPropria)
        # input para o Aviso de recebimento
        checkAvisoRecebimento = GUI.tk.Label(GUI.buttonsBox, anchor='w', pady=3,text='Aviso Recebimento\n[N]',width=15,bg=colorWhite,fg=colorBlack,justify='center')
        checkAvisoRecebimento['borderwidth'] = 0
        checkAvisoRecebimento['activeforeground'] = colorBlack
        checkAvisoRecebimento['activebackground'] = colorWhite
        checkAvisoRecebimento['highlightbackground'] = colorWhite
        checkAvisoRecebimento['relief'] = None
        checkAvisoRecebimento.bind('<ButtonRelease-1>', lambda a: self.mAvRecebimento(checkAvisoRecebimento))
        checkAvisoRecebimento['font'] = tkinter.font.Font(size=8)
        checkAvisoRecebimento.grid(row=18,column=0,padx=0, pady=5)
        # valor padrão
        strMaoPropria = 'N'
        self.sCdMaoPropria.set(strMaoPropria)
        # input para o Servico (ex.: PAC)
        optionServico = GUI.tk.OptionMenu(GUI.buttonsBox, self.nCdServico, *self.servicos)
        optionServico['borderwidth'] = 0
        optionServico['bg'] = colorWhite
        optionServico['fg'] = '#222'
        optionServico['activeforeground'] = '#222'
        optionServico['activebackground'] = colorWhite
        optionServico['highlightbackground'] = colorBlue
        optionServico['relief'] = None
        optionServico['width'] = 10
        optionServico['font'] = tkinter.font.Font(size=8)
        optionServico.grid(row=19,column=0,padx=0, pady=0)
        # valor padrão
        svck = list(self.servicos.keys())
        self.nCdServico.set(svck[1])
        # botao de submit (Calcular)
        buttonSubmit = GUI.tk.Button(GUI.buttonsBox, text = 'Calcular', command = self.getShippingCost)
        buttonSubmit['bd'] = 0
        buttonSubmit['activebackground'] = colorYellow
        buttonSubmit['activeforeground'] = '#040389'
        buttonSubmit['bg'] = '#ffd700'
        buttonSubmit['fg'] = '#040389'
        buttonSubmit['padx'] = 14
        buttonSubmit['pady'] = 0
        buttonSubmit['font'] = tkinter.font.Font(weight='bold')
        buttonSubmit.bind('<Button-1>', self.changeStatus)
        buttonSubmit.grid(row=20, column=0, padx=10, pady = 5, columnspan=3)
        GUI.buttonsBox.grid(ipady=0,row=0,column=0, sticky='w')
        GUI.sidebarLeft.grid()
        # textBox
        # executa programa
        GUI.root.mainloop()
    def changeStatus(self):        
        GUI.working['bg'] = '#ffd700'
        GUI.working['text'] = 'Aguarde enquanto a cosulta é feita...'
    def mPropria(self, el):
        if self.sCdMaoPropria.get()=='S':
            self.sCdMaoPropria.set('N')
            el['text'] = 'Mão própria [N]'
        else:
            self.sCdMaoPropria.set('S')
            el['text'] = 'Mão própria [S]'
    def mAvRecebimento(self, el):
        if self.sCdAvisoRecebimento.get()=='S':
            self.sCdAvisoRecebimento.set('N')
            el['text'] = 'Aviso Recebimento\n[N]'
        else:
            self.sCdAvisoRecebimento.set('S')
            el['text'] = 'Aviso Recebimento\n[S]'
    def getParams(self):
        svc = self.nCdServico.get()
        self.nCdServico.set(self.servicos[self.nCdServico.get()])
        params = ['/calculador/'+self.op.get()+'.aspx?']
        for v in inspect.getmembers(self):
            if str(v[1]).startswith('PY_VAR'):
                params.append(str(v[0])+'='+str(v[1].get()))
        params = '&'.join(params)
        #print params
        self.nCdServico.set(svc)
        return params
    def getShippingCost(self):
        # url do webservice dos correios
        url = 'ws.correios.com.br'
        # prepara a conexão
        conn = http.client.HTTPConnection(url, 80)
        print(url+self.getParams())
        # faz a requisição
        conn.request('GET', self.getParams())
        # guarda a resposta
        response = conn.getresponse()
        # manipula os dados XML
        StrXML = self.parseStrXML(response.read())
        # exibe resultado em forma de texto
        self.display_result(StrXML)
    def display_result(self, data):
        #addr = address()
        address.getAddrOrig(self.sCepOrigem.get())
        #addr = address()
        address.getAddrDest(self.sCepDestino.get())
        #GUI.textBox.insert(GUI.tk.INSERT, "\n"+data)
        #GUI.textBox['state'] = 'disabled'
    def parseStrXML(self, xmlStr):
        print(xmlStr)
        xmlDom = minidom.parseString(xmlStr)
        resultText = ''
        r=0

        for e in xmlDom.getElementsByTagName('cServico')[0].childNodes:
            if len(e.childNodes):
                if (e.tagName!='Erro' and e.tagName!='MsgErro'):
                    #resultText += e.tagName+' = '+e.childNodes[0].data+"\n"
                    val = e.childNodes[0].data
                    if val=='S':
                        val = 'Sim'
                    if val=='N':
                        val = 'Não'
                    tag = e.tagName
                    print(tag)
                    if e.tagName == 'Codigo':
                        val = self.servicos2[str(e.childNodes[0].data)]+' ('+e.childNodes[0].data+')'  
                    if e.tagName == 'Valor':
                        val = 'R$'+val  
                    if e.tagName == 'PrazoEntrega':
                        val += ' dias'  
                    if e.tagName == 'ValorMaoPropria':
                        val = 'R$'+val   
                    if e.tagName == 'ValorAvisoRecebimento':
                        val = 'R$'+val  
                    if e.tagName == 'ValorValorDeclarado':
                        val = 'R$'+val                
                    lab = GUI.tk.Label(GUI.textBox, text=val, bg='#ffffff', pady=5, bd=5)
                    lab['activeforeground'] = '#222'
                    lab['activebackground'] = '#fff'
                    lab['justify'] = 'left'
                    lab.grid(row=self.counter, column=r, sticky='w', padx=2)
                    r += 1                
                    
                if e.tagName=='Erro':
                    print(e.childNodes[0].data)
                    if str(e.childNodes[0].data) == '0':                     
                        GUI.working['bg'] = '#55aa00'
                        GUI.working['text'] = 'Ação concluída com êxito'
                        GUI.working['fg'] = '#ffff00'
                    else:
                        GUI.working['bg'] = '#aa5500'
                        GUI.working['fg'] = '#ffffff'
                        GUI.working['text'] = 'Houve um erro durante a consulta: '+xmlDom.getElementsByTagName('MsgErro')[0].childNodes[0].data    
        GUI.textBox['height']=330          
        self.counter += 1             
        return resultText

shipping()
