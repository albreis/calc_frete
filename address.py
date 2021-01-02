#!/usr/bin/python
# -*- coding: utf-8 -*-
import http.client
from xml.dom import minidom
import GUI

def parseStrXML(xmlStr):
    xmlDom = minidom.parseString(xmlStr)
    resultText = "\n\n"
    #for e in xmlDom.getElementsByTagName('webservicecep')[0].childNodes:            
    #    if len(e.childNodes) > 0:
    #        resultText += e.tagName+' = '+e.childNodes[0].data+"\n"        
    return str(resultText.encode('latin-1'))
def getAddrOrig(cep = 0):
    #print self.cep
    url = 'republicavirtual.com.br'
    uri = '/web_cep.php?cep='+str(cep)
    conn = http.client.HTTPConnection(url, 80)
    conn.request('GET', uri)
    response = conn.getresponse()
    #print response.read()
    responseString = response.read()
    print(responseString)
    xmlDom = minidom.parseString(responseString)
    GUI.enderecoOrigemCEP['text'] = 'CEP: '+cep
    Logradouro = ''
        
    if len(xmlDom.getElementsByTagName('uf')) and len(xmlDom.getElementsByTagName('uf')[0].childNodes)>0:
        GUI.enderecoOrigemUF['text'] = 'UF: '+xmlDom.getElementsByTagName('uf')[0].childNodes[0].data
        
    if len(xmlDom.getElementsByTagName('cidade')) and len(xmlDom.getElementsByTagName('cidade')[0].childNodes)>0:
        GUI.enderecoOrigemCidade['text'] = 'Cidade: '+xmlDom.getElementsByTagName('cidade')[0].childNodes[0].data
        
    if len(xmlDom.getElementsByTagName('bairro')) and len(xmlDom.getElementsByTagName('bairro')[0].childNodes)>0:
        GUI.enderecoOrigemBairro['text'] = 'Bairro: '+xmlDom.getElementsByTagName('bairro')[0].childNodes[0].data
        
    if len(xmlDom.getElementsByTagName('tipo_logradouro')) and len(xmlDom.getElementsByTagName('tipo_logradouro')[0].childNodes)>0:
        Logradouro = xmlDom.getElementsByTagName('tipo_logradouro')[0].childNodes[0].data+"\n"
        
    if len(xmlDom.getElementsByTagName('logradouro')) and len(xmlDom.getElementsByTagName('logradouro')[0].childNodes)>0:
        GUI.enderecoOrigemLogradouro['text'] = 'Logradouro: '+Logradouro+xmlDom.getElementsByTagName('logradouro')[0].childNodes[0].data
    
    
def getAddrDest(cep = 0):
    #print self.cep
    url = 'cep.republicavirtual.com.br'
    uri = '/web_cep.php?formato=xml&cep='+str(cep)
    conn = http.client.HTTPConnection(url, 80)
    conn.request('GET', uri)
    response = conn.getresponse()
    #print response.read()
    responseString = response.read()
    xmlDom = minidom.parseString(responseString)
    GUI.enderecoDestinoCEP['text'] = 'CEP: '+cep
    Logradouro = ''
    
    if len(xmlDom.getElementsByTagName('uf')) and len(xmlDom.getElementsByTagName('uf')[0].childNodes)>0:
        GUI.enderecoDestinoUF['text'] = 'UF: '+xmlDom.getElementsByTagName('uf')[0].childNodes[0].data
        
    if len(xmlDom.getElementsByTagName('cidade')) and len(xmlDom.getElementsByTagName('cidade')[0].childNodes)>0:
        GUI.enderecoDestinoCidade['text'] = 'Cidade: '+xmlDom.getElementsByTagName('cidade')[0].childNodes[0].data
        
    if len(xmlDom.getElementsByTagName('bairro')) and len(xmlDom.getElementsByTagName('bairro')[0].childNodes)>0:
        GUI.enderecoDestinoBairro['text'] = 'Bairro: '+xmlDom.getElementsByTagName('bairro')[0].childNodes[0].data
        
    if len(xmlDom.getElementsByTagName('tipo_logradouro')) and len(xmlDom.getElementsByTagName('tipo_logradouro')[0].childNodes)>0:
        Logradouro = xmlDom.getElementsByTagName('tipo_logradouro')[0].childNodes[0].data+"\n"
        
    if len(xmlDom.getElementsByTagName('logradouro')) and len(xmlDom.getElementsByTagName('logradouro')[0].childNodes)>0:
        GUI.enderecoDestinoLogradouro['text'] = 'Logradouro: '+Logradouro+xmlDom.getElementsByTagName('logradouro')[0].childNodes[0].data
        
