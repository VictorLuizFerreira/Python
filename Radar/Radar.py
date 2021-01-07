#Grupo:
# Victor Luiz Ferreira RA: 21802564
# Arthur Sanchez Fortuna RA: 21800184
# Luciano Duarte Gonzalez RA: 21804263
# Marconi Rodrigues Maia RA: 21606633

import csv
from graphics import *
import math
import time
Xmax = 800
Ymax = 600

def criar_tela():
corFundo = color_rgb(16, 16, 37)
win = GraphWin("Tela", Xmax, Ymax)
win.setBackground(corFundo)
return win

def ponto(x,y,cor,tamanho):
x = int(x+Xmax/2)
y = int(Ymax/2 - y)
if tamanho == 1:
win.plotPixel(x,y,cor)
if tamanho == 2:
win.plotPixel(x,y,cor)
win.plotPixel(x+1,y,cor)
win.plotPixel(x,y-1,cor)
win.plotPixel(x+1,y-1,cor)
if tamanho == 3:
win.plotPixel(x,y,cor)
win.plotPixel(x+1,y,cor)
win.plotPixel(x+1,y-1,cor)
win.plotPixel(x+1, y+1, cor)
win.plotPixel(x,y-1,cor)
win.plotPixel(x, y+1, cor)
win.plotPixel(x-1,y,cor)
win.plotPixel(x-1,y-1,cor)
win.plotPixel(x-1,y+1,cor)
return

def reta (x1,y1,x2,y2,cor,tamanho):
x = x1
y = y1
p = 0
DX = x2-x1
DY = y2-y1
xInc = 1
yInc = 1
if DX < 0:
xInc = -1
DX = -DX
if DY < 0:
yInc = -1
DY = -DY
if DY <= DX:
p = DX/2
while x != x2:
ponto(x,y,cor,tamanho)
p = p-DY
if p < 0:
y = y+yInc
p = p+DX
x = x+xInc
continue
else:
p = DY/2
while y != y2:
ponto(x,y,cor,tamanho)
p = p-DX
if p < 0:
x = x+xInc
p = p+DY
y = y+yInc
continue
ponto(x,y,cor,tamanho)

def pontilhada (x1,y1,x2,y2,cor,tamanho):
x = x1
y = y1
p = 0
conta=0

DX = x2-x1
DY = y2-y1
xInc = 1
yInc = 1
if DX < 0:
xInc = -1
DX = -DX
if DY < 0:
yInc = -1
DY = -DY
if DY <= DX:
p = DX/2
while x != x2:
if(conta % 10 == 0):
ponto(x, y, cor, tamanho)
conta = conta + 1
p = p-DY
if p < 0:
y = y+yInc
p = p+DX
x = x+xInc
continue
else:
p = DY/2
while y != y2:
if (conta % 10 == 0):
ponto(x, y, cor, tamanho)
conta = conta + 1
p = p-DX
if p < 0:
x = x+xInc
p = p+DY
y = y+yInc
continue
ponto(x,y,cor,tamanho)

def tracejada (x1, y1, x2, y2, cor, tam):
x = x1
y = y1
p = 0
contador = 0
dx = x2 - x1
dy = y2 - y1
xInc = 1

yInc = 1
if dx < 0:
xInc = -1
dx = -dx
if dy < 0:
yInc = -1
dy = -dy
if dy <= dx:
p = dx / 2
while x != x2:
if contador < 5:
ponto(x, y, cor, tam)
contador = contador + 1
if contador == 10:
contador = contador * 0
p = p - dy
if p < 0:
y = y + yInc
p = p + dx
x = x + xInc
continue
else:
p = dy / 2
while y != y2:
if contador < 5:
ponto(x, y, cor, tam)
contador = contador + 1
if contador == 10:
contador = contador * 0
p = p - dx
if p < 0:
x = x + xInc
p = p + dy
y = y + yInc
continue

def circulo(xc,yc,r,cor,tamanho):
x=0
y=r
p=5/4-r
ponto(x,y,cor,tamanho)
while x<y:

x=x+1
if p<0:
p=p+(2*x)+1
else:
y=y-1 #y=9
p=p+(2*x)+1-(2*y) #p=-3
x = x+xc
y = y+yc
ponto(x,y,cor,tamanho)
ponto(y,x,cor,tamanho)
ponto(y,-x,cor,tamanho)
ponto(-x,y,cor,tamanho)
ponto(-x,-y,cor,tamanho)
ponto(-y,-x,cor,tamanho)
ponto(-y,x,cor,tamanho)
ponto(x,-y, cor, tamanho)

def texto(x, y, palavra, cor, tamanho, estilo):
t = Text(Point(x,y), palavra)
t.setOutline(cor)
t.setSize(tamanho)
t.setStyle(estilo)
t.draw(win)
return

def Projetar(x,y,z,f, F):
xl = x * f/(F-z)
yl = y * f/(F-z)
return int(xl), int(yl)

def direcao():
x, y = Projetar(1000, 2000, 3000, 100, 5000)
m = y/x
alfa = math.atan(m)
return alfa

def read_csv(document_path):
file = []
with open(document_path, 'r') as csv_file:
reader = csv.reader(csv_file, delimiter=';')
for column in reader:
file.append(column)
return file

def transform_data_file(data):
data_dict = {}
for line in range(1, len(data)):
data_dict.update({(data[line][0], data[line][2]):

[data[line][0], data[line][1], data[line][2], data[line][3],
data[line][4], data[line][5], data[line][6], data[line][7]]})

return data_dict

def tela_fundo():
circulo(0, 0, 65, "purple", 1)
circulo(0,0,130,"purple",1)
circulo(0,0,210,"purple",1)
circulo(0,0,286,"purple",1)
tracejada(0, 290, 0, -290, "purple", 1)
tracejada(290, 0, -290, 0, "purple", 1)
tracejada(230, -180, -230, 180, "purple", 1)
tracejada(-230, -180, 230, 180, "purple", 1)
texto(400, 20, "0o", "purple", 10, "bold")
texto(490, 40, "15o", "purple", 10, "bold")
texto(560, 80, "30o", "purple", 10, "bold")
texto(615, 135, "45o", "purple", 10, "bold")
texto(650, 195, "60o", "purple", 10, "bold")
texto(665, 250, "75o", "purple", 10, "bold")
texto(675, 300, "90o", "purple", 10, "bold")
texto(660, 350, "105o", "purple", 10, "bold")
texto(640, 415, "120o", "purple", 10, "bold")
texto(610, 465, "135o", "purple", 10, "bold")
texto(560, 515, "150o", "purple", 10, "bold")
texto(480, 560, "165o", "purple", 10, "bold")
texto(400, 580, "180o", "purple", 10, "bold")
texto(315, 560, "195o", "purple", 10, "bold")
texto(240, 515, "210o", "purple", 10, "bold")

texto(190, 465, "225o", "purple", 10, "bold")
texto(160, 415, "240o", "purple", 10, "bold")
texto(140, 350, "255o", "purple", 10, "bold")
texto(130, 300, "270o", "purple", 10, "bold")
texto(140, 250, "285o", "purple", 10, "bold")
texto(155, 195, "300o", "purple", 10, "bold")
texto(190, 135, "315o", "purple", 10, "bold")
texto(245, 80, "330o", "purple", 10, "bold")
texto(315, 40, "345o", "purple", 10, "bold")
return

def apagar_tela(win):
win.close()
win = criar_tela()
return win

def iconeAviao(dados,win):
for t in range(0,151,10):
for voo in ["LA 2203", "GZ 0331", "AZ 0032", "AZ 0157", "GZ 0667"]:
tempo = str(t)
x = int(dados.get((tempo,voo))[-3])
y = int(float(dados.get((tempo,voo))[-2]))
z = int(dados.get((tempo,voo))[-1])
cor = dados.get((tempo,voo))[1]
if(cor=="P"):
cor = "green"
elif(cor=="S"):
cor = "white"
else:
cor = "red"
x, y = Projetar(x, y, z, 1000, 15000)
reta(x + 0, y + 0, x - 20, y + 0, cor, 1)
reta(x - 8, y + 8, x - 6, y + 0, cor, 1)
reta(x - 8, y - 8, x - 6, y + 0, cor, 1)
reta(x - 18, y + 4, x - 16, y + 0, cor, 1)
reta(x - 18, y - 4, x - 16, y + 0, cor, 1)
time.sleep(0.05)

win = criar_tela()
tela_fundo()
dados = read_csv("./dados.csv")
dados_transf = transform_data_file(dados)
iconeAviao(dados_transf,win)
win.getMouse()
win = apagar_tela(win)
win.close()