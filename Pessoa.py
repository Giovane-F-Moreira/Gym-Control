class Pessoa:

  def __init__(self, nome, foto, inadiplente, dias_treino):
    self.nome = nome
    self.foto = foto
    self.inadiplente = inadiplente
    self.dias_treino = dias_treino
  
  def exibir_informacoes(self):
    print(self.nome, self.foto, self.inadiplente, self.dias_treino)
