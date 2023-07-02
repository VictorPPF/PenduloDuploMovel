from vpython import *
#Web VPython 3.2
#----------Canvas--------------#
animation = canvas(width=600, height=500, align='left')

#----------Variáveis-----------#
g = 9.81
M1 = 1 #massa da primeira esfera
M2 = 1 #massa da segunda esfera
M3 = 1 #massa do carrinho
R1 = 1 #comprimento do fio M3-M1
R2 = 1 #comprimento do fio M1-M2
X = 0 #Posição no eixo x
th = float(input("ângulo theta inicial em graus: ").replace(',', '.'))
ph = float(input("ângulo phi inicial em graus: ").replace(',', '.'))

#----------Funções do tempo-----------#
theta1 = th*pi/180 #ângulo do fio R1 em relação ao eixo y
theta1dot = 0 #derivada de theta1
theta2 = ph*pi/180 #ângulo do fio R2 em relação ao eixo y
theta2dot = 0 #derivada de theta2
Xdot = 0 #velocidade em X
Xddot = 0 #aceleração em X

#----------Objetos-----------#
#Carrinho
pivot = box(pos=vector(X,1,0), size=vector(0.5, 0.3, 0.3), color=color.blue)
seta = arrow(pos=pivot.pos, axis=vector(Xdot*1, 0, 0), color=color.red) #vetor velocidade
roda1 = cylinder(pos=vector(X + 0.2, 1 - pivot.size.y/2 - 0.04, 0.1), axis=vector(0,0,0.04), radius=0.05, color=color.purple)
roda2 = cylinder(pos=vector(X + 0.2, 1 - pivot.size.y/2 - 0.04, -0.14), axis=vector(0,0,0.04), radius=0.05, color=color.purple)
roda3 = cylinder(pos=vector(X - 0.2, 1 - pivot.size.y/2 - 0.04, -0.14), axis=vector(0,0,0.04), radius=0.05, color=color.purple)
roda4 = cylinder(pos=vector(X - 0.2, 1 - pivot.size.y/2 - 0.04, 0.1), axis=vector(0,0,0.04), radius=0.05, color=color.purple)
#Trilhos e esferas
trilho_d = box(pos=vector(X, 1 - pivot.size.y/2 - 2*roda1.radius - 0.001, 0.12), size=vector(20, 0.01, 0.02), color=color.green)
trilho_e = box(pos=vector(X, 1 - pivot.size.y/2 - 2*roda1.radius - 0.001, -0.12), size=vector(20, 0.01, 0.02), color=color.green)
m1 = sphere(pos=pivot.pos+vector(R1*sin(theta1),-R1*cos(theta1),0), radius=1/10,color=color.yellow, make_trail=False, trail_color=color.green)
m2 = sphere(pos=m1.pos+vector(R2*sin(theta2),-R2*cos(theta2),0), radius=1/10,color=color.yellow, make_trail=False)
s1=cylinder(pos=pivot.pos,axis=m1.pos-pivot.pos, radius=R1/30)
s2=cylinder(pos=m1.pos,axis=m2.pos-m1.pos, radius=R1/30)
#Esfera do centro de massa
Cm = (pivot.pos*M3+m1.pos*M1+m2.pos*M2)/(M1+M2+M3)
CM =sphere(pos=vec(Cm.x,Cm.y,1/5),radius = (0.1/5), color=color.red,make_trail=False, retain=50)


#----------Comandos-----------#
#Título e tamanho
animation.width = 600
animation.height = 500
animation.center = vector(X, 1, 0)
animation.title = "Double Pendulum with moving support"
animation.align = 'right'


#comando de pause
run = False
def pause(b):
    global run
    run = not run
    Trilha=True
    if run: b.text = 'Pause'
    else: b.text = 'Run'
button(text='Run', bind=pause, pos=print_anchor)


#comando de plotagem do gráfico
graph(scroll=True, xmin=0, xmax=5, align='left')
Etot = gcurve(color=color.black, label="E<sub>total</sub>", interval=1000)
ktot = gcurve(color=color.red, label="K<sub>total</sub>", interval=1000)
kcarro = gcurve(color=0.7*color.purple, label="K<sub>carro</sub>", interval=1000)
km1 = gcurve(color=0.7*color.green, label="K<sub>esfera1</sub>", interval=1000)
km2 = gcurve(color=0.7*color.yellow, label="K<sub>esfera2</sub>", interval=1000)
EP = gcurve(color=color.blue, label="E<sub>potencial</sub>", interval=1000)

graphing = False 
def graphit(b):
    global graphing
    graphing = not graphing
    if graphing: 
        b.text = 'Pause Graph'
        Etot.data = []
        ktot.data = []
        kcarro.data = []
        km1.data = []
        km2.data = []
        EP.data = []
    else: b.text = 'Graph Energy'
button(text='Graph Energy', bind=graphit, pos=print_anchor)
wtext(text='     \n\n', pos=print_anchor)


#sliders de variação das massas e comprimentos
xmin = 1
xmax = 2
def massa1(sl):
    global xmin,xmax
    xm1_text.text = 'Cart mass = '+'{:1.2f}'.format(xm1_sl.value)+"\n\n"
    xmin = xm1_sl.value
    return
def massa2(sl):
    global xmin,xmax
    xm2_text.text = 'm1 = '+'{:1.2f}'.format(xm2_sl.value)+"\n\n"
    xmin = xm2_sl.value
    return
def massa3(sl):
    global xmin,xmax
    xm3_text.text = 'm2 = '+'{:1.2f}'.format(xm3_sl.value)+"\n\n"
    xmax = xm3_sl.value
    return
def corda1(sl):
    global xmin,xmax
    xr1_text.text = 'R1 = '+'{:1.2f}'.format(xr1_sl.value)+"\n\n"
    xmax = xr1_sl.value
    return
def corda2(sl):
    global xmin,xmax
    xr2_text.text = 'R2 = '+'{:1.2f}'.format(xr2_sl.value)+"\n\n"
    xmax = xr2_sl.value
    return
xm1_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=massa1, right=15, pos=print_anchor)
xm1_text = wtext(text='massa do carrinho = '+'{:1.2f}'.format(xm1_sl.value)+"\n\n", pos=print_anchor)
xm2_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=massa2, right=15, pos=print_anchor)
xm2_text = wtext(text='m1 = '+'{:1.2f}'.format(xm2_sl.value)+"\n\n", pos=print_anchor)
xm3_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=massa3, right=15, pos=print_anchor)
xm3_text = wtext(text='m2 = '+'{:1.2f}'.format(xm3_sl.value)+"\n\n", pos=print_anchor)
xr1_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=corda1, right=15, pos=print_anchor)
xr1_text = wtext(text='R1 = '+'{:1.2f}'.format(xr1_sl.value)+"\n\n", pos=print_anchor)
xr2_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=corda2, right=15, pos=print_anchor)
xr2_text = wtext(text='R2 = '+'{:1.2f}'.format(xr2_sl.value)+"\n\n", pos=print_anchor)

#Cor de fundo
def change_background(m):
    animation.background = menu_colors[m.index]
    my_label.background = animation.background

wtext(text="Background color = ", pos=print_anchor)
menu_text = [ "Black", "Dark blue", "Brown", "Gray", "Dark green" ]
menu_colors = [ color.black, vector(0.098, 0.098, 0.439), vector(0.2, 0.1, 0), vector(0.2,0.2,0.2), vector(0, 0.2, 0)]
bg_menu = menu(bind=change_background, choices = menu_text, pos=print_anchor)

#----------Atualização do movimento-----------#
t = 0
dt = 0.00002

while True:
  rate(100000)
  if not run: continue
  
  M3 = xm1_sl.value
  M1 = xm2_sl.value
  m1.radius = M1/10
  M2 = xm3_sl.value
  m2.radius = M2/10
  R1 = xr1_sl.value
  R2 = xr2_sl.value
  
  #Equação de X dois pontos:
  Xddot= (0.5*(-R1*M1**2*sin(theta1)*theta1dot**2 - R1*M1*M2*(sin(2*theta2 - 3*theta1) + sin(2*theta2 - theta1))*theta2dot*theta1dot/4 + 
  R1*M1*M2*(sin(2*theta2 - 3*theta1) + sin(2*theta2 - theta1))*theta1dot**2/4 - 
  R1*M1*M2*(sin(2*theta2 - theta1) + sin(2*theta2 + theta1))*theta2dot*theta1dot/4 + R1*M1*M2*sin(theta2 - theta1)*cos(theta2)*theta2dot*theta1dot - 
  R1*M1*M2*sin(theta2 - theta1)*cos(theta2)*theta1dot**2 + R1*M1*M2*sin(theta2)*cos(theta2 - theta1)*cos(theta1)**2*theta2dot*theta1dot + 
  R1*M1*M2*sin(theta1)*cos(theta2 - theta1)**2*theta1dot**2 - 
  R1*M1*M2*sin(theta1)*cos(theta2 - theta1)*cos(theta2)*cos(theta1)*theta2dot*theta1dot + 
  R1*M1*M2*sin(theta1)*cos(theta2)**2*theta2dot*theta1dot - 2.0*R1*M1*M2*sin(theta1)*theta1dot**2 - 
  R1*M2**2*(sin(2*theta2 - 3*theta1) + sin(2*theta2 - theta1))*theta2dot*theta1dot/4 + 
  R1*M2**2*(sin(2*theta2 - 3*theta1) + sin(2*theta2 - theta1))*theta1dot**2/4 - 
  R1*M2**2*(sin(2*theta2 - theta1) + sin(2*theta2 + theta1))*theta2dot*theta1dot/4 + 
  R1*M2**2*sin(theta2 - theta1)*cos(theta2)*theta2dot*theta1dot - R1*M2**2*sin(theta2 - theta1)*cos(theta2)*theta1dot**2 + 
  R1*M2**2*sin(theta2)*cos(theta2 - theta1)*cos(theta1)**2*theta2dot*theta1dot + 
  R1*M2**2*sin(theta1)*cos(theta2 - theta1)**2*theta1dot**2 - 
  R1*M2**2*sin(theta1)*cos(theta2 - theta1)*cos(theta2)*cos(theta1)*theta2dot*theta1dot + 
  R1*M2**2*sin(theta1)*cos(theta2)**2*theta2dot*theta1dot - R1*M2**2*sin(theta1)*theta1dot**2 - 
  R2*M1*M2*(-sin(theta2 - 2*theta1) + sin(theta2 + 2*theta1))*theta2dot*theta1dot/4 + 
  R2*M1*M2*sin(theta2 - theta1)*cos(theta1)*theta2dot**2 - R2*M1*M2*sin(theta2 - theta1)*cos(theta1)*theta2dot*theta1dot + 
  R2*M1*M2*sin(theta2)*cos(theta1)**2*theta2dot*theta1dot - R2*M1*M2*sin(theta2)*theta2dot**2 - 
  R2*M2**2*(-sin(theta2 - 2*theta1) + sin(theta2 + 2*theta1))*theta2dot*theta1dot/4 - R2*M2**2*(sin(theta2 - 2*theta1) + 
  sin(3*theta2 - 2*theta1))*theta2dot**2/4 + R2*M2**2*(sin(theta2 - 2*theta1) + 
  sin(3*theta2 - 2*theta1))*theta2dot*theta1dot/4 + R2*M2**2*sin(theta2 - theta1)*cos(theta1)*theta2dot**2 - 
  R2*M2**2*sin(theta2 - theta1)*cos(theta1)*theta2dot*theta1dot + R2*M2**2*sin(theta2)*cos(theta2 - theta1)**2*theta2dot**2 - 
  R2*M2**2*sin(theta2)*cos(theta2 - theta1)*cos(theta2)*cos(theta1)*theta2dot*theta1dot + 
  R2*M2**2*sin(theta2)*cos(theta1)**2*theta2dot*theta1dot - R2*M2**2*sin(theta2)*theta2dot**2 + 
  R2*M2**2*sin(theta1)*cos(theta2 - theta1)*cos(theta2)**2*theta2dot*theta1dot - g*M1**2*sin(2*theta1)/2 + 
  g*M1*M2*sin(theta2)*cos(theta2 - theta1)*cos(theta1) - g*M1*M2*sin(2*theta2)/2 + g*M1*M2*sin(theta1)*cos(theta2 - theta1)*cos(theta2) - 
  1.0*g*M1*M2*sin(2*theta1) + g*M2**2*sin(theta2)*cos(theta2 - theta1)*cos(theta1) - g*M2**2*sin(2*theta2)/2 + 
  g*M2**2*sin(theta1)*cos(theta2 - theta1)*cos(theta2) - g*M2**2*sin(2*theta1)/2)/(-0.5*M3*M1 - 0.5*M3*M2*sin(theta2)**2 + 
  1.0*M3*M2*sin(theta2)*sin(theta1)*cos(theta2 - theta1) - 0.5*M3*M2*sin(theta1)**2 - 0.5*M1**2*sin(theta1)**2 - 0.5*M1*M2*sin(theta1)**2))
  
  #Equação de Theta dois pontos:
  theta1ddot=((-0.25*R1*M3*M2*sin(2*theta2 - 2*theta1)*theta1dot**2 + 0.25*R1*M1**2*sin(2*theta1)*theta1dot**2 + 
  0.25*R1*M1*M2*sin(2*theta1)*theta1dot**2 - 0.5*R2*M3*M2*sin(theta2 - theta1)*theta2dot**2 - 0.25*R2*M1*M2*sin(theta2 - theta1)*theta2dot**2 + 
  0.25*R2*M1*M2*sin(theta2 + theta1)*theta2dot**2 + 0.5*g*M3*M1*sin(theta1) - 0.25*g*M3*M2*sin(2*theta2 - theta1) + 0.25*g*M3*M2*sin(theta1) + 
  0.5*g*M1**2*sin(theta1) + 0.5*g*M1*M2*sin(theta1))/(R1*(-0.5*M3*M1 + 0.25*M3*M2*cos(2*theta2 - 2*theta1) - 
  0.25*M3*M2 + 0.25*M1**2*cos(2*theta1) - 0.25*M1**2 + 0.25*M1*M2*cos(2*theta1) - 0.25*M1*M2)))
  
  #Equação de Phi dois pontos:
  theta2ddot=(0.5*M3*(1.0*R1*M1*sin(theta2 - theta1)*theta1dot**2 + 1.0*R1*M2*sin(theta2 - theta1)*theta1dot**2 + 
  0.5*R2*M2*sin(2*theta2 - 2*theta1)*theta2dot**2 + 0.5*g*M1*sin(theta2 - 2*theta1) + 0.5*g*M1*sin(theta2) + 
  0.5*g*M2*sin(theta2 - 2*theta1) + 0.5*g*M2*sin(theta2))/(R2*(-0.5*M3*M1 + 0.25*M3*M2*cos(2*theta2 - 2*theta1) - 
  0.25*M3*M2 + 0.25*M1**2*cos(2*theta1) - 0.25*M1**2 + 0.25*M1*M2*cos(2*theta1) - 0.25*M1*M2)))


  theta2dot = theta2dot + theta2ddot*dt
  theta1dot = theta1dot + theta1ddot*dt
  Xdot = Xdot + Xddot*dt
  theta1 = theta1 + theta1dot*dt
  theta2 = theta2 + theta2dot*dt
  X = X + Xdot*dt
  t = t + dt
  
  #Atualização da posição
  m1.pos=pivot.pos+vector(R1*sin(theta1),-R1*cos(theta1),0)
  m2.pos = m1.pos+vector(R2*sin(theta2),-R2*cos(theta2),0)
  s1.axis = m1.pos-pivot.pos
  s2.pos = m1.pos
  s1.pos = pivot.pos
  s2.axis = m2.pos - m1.pos
  seta.pos = pivot.pos
  seta.axis = vector(Xdot*0.3, 0, 0)
  roda1.pos = vector(X + 0.2, 1 - pivot.size.y/2 - roda1.radius, 0.1)
  roda2.pos = vector(X + 0.2, 1 - pivot.size.y/2 - roda2.radius, -0.14)
  roda3.pos = vector(X - 0.2, 1 - pivot.size.y/2 - roda3.radius, -0.14)
  roda4.pos = vector(X - 0.2, 1 - pivot.size.y/2 - roda4.radius, 0.1)
  Cm = (pivot.pos*M3+m1.pos*M1+m2.pos*M2)/(M1+M2+M3)
  CM.pos = vector(Cm.x,Cm.y,1/5)
  pivot.pos = vector(X, 1, 0)
  m1.make_trail=True
  m2.make_trail=True
  CM.make_trail=True
  animation.camera.follow(pivot)
  
  
  #Plotagem do gráfico
  if graphing:
      T1 = 0.5*M3*Xdot**2
      T2 = 0.5*M1*(R1**2*sin(theta1)**2*theta1dot**2 + (R1*cos(theta1)*theta1dot + Xdot)**2)
      T3 = (0.5*M2*((R1*sin(theta1)*theta1dot + R2*sin(theta2)*theta2dot)**2 + 
      (R1*cos(theta1)*theta1dot + R2*cos(theta2)*theta2dot + Xdot)**2))
      Ttotal = T1 + T2 + T3
      U = -R1*g*M1*cos(theta1) + g*M2*(-R1*cos(theta1) - R2*cos(theta2))
      Etot.plot(t, Ttotal+U)
      ktot.plot(t, Ttotal)
      kcarro.plot(t, T1)
      km1.plot(t, T2)
      km2.plot(t, T3)
      EP.plot(t, U)