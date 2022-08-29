class Control:
  def __init__(self):
    self.tv=None
  
  def turnOn(self):
    self.tv.estado=True
  def turnOff(self):
    self.tv.estado=False

  def canalUp(self):
    if self.tv.canal>=1 and self.tv.canal<120 and self.tv.estado==True:
      self.tv.canal+=1
  def canalDown(self):
    if self.tv.canal>1 and self.tv.canal<=120 and self.tv.estado==True:
      self.tv.canal-=1

  def volumenUp(self):
    if self.tv.volumen>=0 and self.tv.volumen<7 and self.tv.estado==True:
      self.tv.volumen+=1
  def volumenDown(self):
    if self.tv.volumen>=0 and self.tv.volumen<7 and self.tv.estado==True:
      self.tv.volumen-=1
  
  def setCanal(self, canal):
    if canal>=1 and canal<=120 and self.tv.estado==True:
      self.tv.canal=canal

  def enlazar(self,tv):
    self.tv=tv
    tv.setControl(self)

  def getTv(self):
    return self.tv
  def setTv(self, tv):
    self.tv=tv