class Calculadora:
  def __init__(self,Digito1,Digito2):
    self.Digito1=Digito1
    self.Digito2=Digito2
 
  def soma(self):
    soma = self.Digito1 + self.Digito2
    print("soma:"+str(soma))
 
  def sub(self):
    sub = self.Digito1 - self.Digito2
    print("sub:"+str(sub))
 
calculadora = Calculadora(int(input()),int(input()))
calculadora.soma()
calculadora.sub()
class Continuacao(Calculadora):
  def __init__(self):  
 
    Calculadora.__init__(self,Digito1=int(input()),Digito2=int(input()))
    
 
 
  def multiplica(self):
    print(self.Digito1*self.Digito2)
  
  def divisao(self):
    print(self.Digito1/self.Digito2)
  
  def exponencial(self):
    print(self.Digito1**self.Digito2)
 
calculadora2=Continuacao()
calculadora2.multiplica()
calculadora2.divisao()
calculadora2.exponencial()