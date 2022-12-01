from Pessoa import Pessoa;

class Academia:

  def __init__(self, pessoas):
    self.pessoas = pessoas
  
  def exibir_informacoes(self):
    i = 0
    while i < len(self.pessoas):
      print(self.pessoas[i].nome, ' treinou por ', self.pessoas[i].dias_treino, 'dia(s)')
      i=i+1
  
  def pagamento(Pessoa, pagou):
    if pagou:
      Pessoa.inadiplente = False
      print(Pessoa.nome," pagou a mensalidade")
      
      return True
    
    else:
      Pessoa.inadiplente = True
      print(Pessoa.nome," está inadiplente")
      
      return False
    
  def treinar(self, pessoas):
    
    i = 0
    #percorre o array de pessoas
    while i < len(pessoas):
      
      #testa se é inadiplente
      if pessoas[i].inadiplente:
        print(pessoas[i].nome, ' está inadiplente!')
        i=i+1
      
      else:         
        pessoas[i].dias_treino = pessoas[i].dias_treino + 1
        
        print(self.pessoas[i].nome, ' está treinando há ', self.pessoas[i].dias_treino, 'dias')
        i=i+1
