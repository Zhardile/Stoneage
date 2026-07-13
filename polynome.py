class polynome:
  def __init__(self,coeffs):
    self.coeffs = coeffs
  def __repr__(self):
    p = []
    for i,c in enumerate(self.coeffs):
      if c !=0:
        p.append(f"{c}x**{i}")
    return " + ".join(p) if p else "0" 
  def __add__(self,autre):
    mx = max(len(self.coeffs),len(autre.coeffs))
    g =[]
    for i in range(mx):
      a = self.coeffs[i] if i < len(self.coeffs) else 0
      b = autre.coeffs[i] if i < len(autre.coeffs) else 0
      g.append(a+b)
    return polynome(g)
  def __mul__(self,autre):
    res = (len(self.coeffs)+len(autre.coeffs)-1)*[0]
    for i,a in enumerate(self.coeffs):
      for j,b in enumerate(autre.coeffs):
        res[i+j] += a*b
    return polynome(res)
  def derivee(self):
    p = [ i*self.coeffs[i] for i in range (1,len(self.coeffs))]
    return polynome(p) 
