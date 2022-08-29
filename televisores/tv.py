class TV:
  numTV=0
  def __init__(self,marca,estado):
    self.marca=marca
    self.canal=1
    self.precio=500
    self.estado=estado
    self.volumen=1
    self.control=None
    TV.numTV+=1        
  
  def setNumTV(numTV):
    TV.numTV=numTV
  def getNumTV():
    return TV.numTV

  def setMarca(self, marca):
    self.marca=marca
  def getMarca(self):
    return self.marca

  def setControl(self, control):
    self.control=control
  def getControl(self):
    return self.control

  def setPrecio(self, precio):
    self.precio=precio
  def getPrecio(self):
    return self.precio

  def setVolumen(self, volumen):
    if self.volumen>=0 and self.volumen<=7 and self.estado==True:
      self.volumen=volumen
  def getVolumen(self):
    return self.volumen

  def setCanal(self, canal):
    if canal>=1 and canal<=120 and self.estado==True:
      self.canal=canal
  def getCanal(self):
    return self.canal

  def turnOn(self):
    self.estado=True
  def turnOff(self):
    self.estado=False

  def getEstado(self):
    return self.estado

  def canalUp(self):
    if self.canal>=1 and self.canal<120 and self.estado==True:
      self.canal+=1
  def canalDown(self):
    if self.canal>1 and self.canal<=120 and self.estado==True:
      self.canal-=1
  def volumenUp(self):
    if self.volumen>=0 and self.volumen<7 and self.estado==True:
      self.volumen+=1
  def volumenDown(self):
    if self.volumen>=0 and self.volumen<7 and self.estado==True:
      self.volumen-=1