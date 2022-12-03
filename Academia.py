from Pessoa import Pessoa
import random

class Academia:

  def __init__(self, pessoas):
    self.pessoas = pessoas
  
  def exibir_informacoes(self):
    
    i = 0
    print('***************************************  Informações  ***************************************')
    while i < len(self.pessoas):
      print(self.pessoas[i].nome, ' treinou por ', self.pessoas[i].dias_treino, 'dia(s)')
      i=i+1
  
    destaque = ''
    if self.pessoas[0].dias_treino > self.pessoas[1].dias_treino:
      destaque = self.pessoas[0].nome
    
    else:
      destaque = self.pessoas[1].nome
       
    print('         ___________')       
    print('        \'._==_==_=_.\'')
    print('        .-\:      /-.')
    print('       | (|:.     |) |')
    print('        \'-|:.     |-\'')
    print('          \\::.    /')
    print('           \'::. .\'')
    print('             ) (')
    print('           _.\' \'._')
    print('          `"""""""`')
    print('Destaque por mais dias de treino: ', destaque)
    
    
  def realizar_pagamento(self, pessoas):
    print('****************************************  Pagamento  ****************************************') 
    cont = 0 
    while cont < len(self.pessoas):
      
      self.pessoas[cont].inadiplente = bool(random.getrandbits(1))
        
      if pessoas[cont].inadiplente:
        print(self.pessoas[cont].nome, 'não pagou a mensalidade, Catraca BLOQUEADA!')
        cont = cont + 1
      
      else:
        print(self.pessoas[cont].nome, 'pagou a mensalidade, Catraca LIBERADA!')
        cont = cont + 1
       
  def treinar(self, pessoa):
    i = 0
     
    if bool(random.getrandbits(1)):
      pessoa.dias_treino = pessoa.dias_treino + 1
      print(pessoa.nome, ' está treinando há ', pessoa.dias_treino, 'dia(s)')
    
    else:
      print(pessoa.nome, ' está treinando há ', pessoa.dias_treino, 'dias, mas não treinou hoje!')
