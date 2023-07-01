from vpython import *
#Web VPython 3.2
 
#Variáveis
g = 9.81
M1 = 1
M2 = 1
M3 = 5
R1 = 1
R2 = 1
X = 0
#Funções
theta1 = 90*pi/180
theta1dot = 0
theta2 = 45*pi/180
theta2dot = 0
Xdot = 0
Xddot = 0
#Objetos
pivot = box(pos=vector(X,1,0), size=vector(0.5, 0.3, 0.3), color=color.blue)
seta = arrow(pos=pivot.pos, axis=vector(Xdot*1, 0, 0), color=color.red)
roda1 = cylinder(pos=vector(X + 0.2, 1 - pivot.size.y/2 - 0.04, 0.1), axis=vector(0,0,0.04), radius=0.05, color=color.purple)
roda2 = cylinder(pos=vector(X + 0.2, 1 - pivot.size.y/2 - 0.04, -0.14), axis=vector(0,0,0.04), radius=0.05, color=color.purple)
roda3 = cylinder(pos=vector(X - 0.2, 1 - pivot.size.y/2 - 0.04, -0.14), axis=vector(0,0,0.04), radius=0.05, color=color.purple)
roda4 = cylinder(pos=vector(X - 0.2, 1 - pivot.size.y/2 - 0.04, 0.1), axis=vector(0,0,0.04), radius=0.05, color=color.purple)
trilho_d = box(pos=vector(X, 1 - pivot.size.y/2 - 2*roda1.radius - 0.001, 0.12), size=vector(20, 0.01, 0.02), color=color.green) #Mudei o tamanho do trilho
trilho_e = box(pos=vector(X, 1 - pivot.size.y/2 - 2*roda1.radius - 0.001, -0.12), size=vector(20, 0.01, 0.02), color=color.green)
m1 = sphere(pos=pivot.pos+vector(R1*sin(theta1),-R1*cos(theta1),0), radius=R1/10,color=color.yellow, make_trail=False, trail_color=color.green)
m2 = sphere(pos=m1.pos+vector(R2*sin(theta2),-R2*cos(theta2),0), radius=R1/10,color=color.yellow, make_trail=False)
s1=cylinder(pos=pivot.pos,axis=m1.pos-pivot.pos, radius=R1/30)
s2=cylinder(pos=m1.pos,axis=m2.pos-m1.pos, radius=R1/30)
Cm = (pivot.pos*M3+m1.pos*M1+m2.pos*M2)/(M1+M2+M3)

CM =sphere(pos=vec(Cm.x,Cm.y,1/5),radius = (0.1/5), color=color.red,make_trail=False, retain=50)

run = False
def pause(b):
    global run
    run = not run
    Trilha=True
    if run: b.text = 'Pause'
    else: b.text = 'Run'
button(text='Run',pos=scene.title_anchor, bind=pause)



graphing = False 
tstart = 0
def graphit(b):
    global graphing, tstart, instructions
    graphing = not graphing
    if graphing: 
        instructions.text = ''
        b.text = 'Pause Graph'
        energy.data = []
        ktrans.data = []
        krot.data = []
        PE.data = []
    else: b.text = 'Graph Energy'
wtext(text='     ')
button(text='Graph Energy', bind=graphit)


xmin = 1
xmax = 3

def massa1(sl):
    global xmin,xmax
    xm1_text.text = 'massa do carrinho = '+'{:1.2f}'.format(xm1_sl.value)+"\n\n"
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

xm1_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=massa1, right=15)
xm1_text = wtext(text='massa do carrinho = '+'{:1.2f}'.format(xm1_sl.value)+"\n\n")
xm2_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=massa2, right=15)
xm2_text = wtext(text='m1 = '+'{:1.2f}'.format(xm2_sl.value)+"\n\n")
xm3_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=massa3, right=15)
xm3_text = wtext(text='m2 = '+'{:1.2f}'.format(xm3_sl.value)+"\n\n")
xr1_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=corda1, right=15)
xr1_text = wtext(text='R1 = '+'{:1.2f}'.format(xr1_sl.value)+"\n\n")
xr2_sl = slider(min=xmin, max=xmax, value=xmin, length=220, bind=corda2, right=15)
xr2_text = wtext(text='R2 = '+'{:1.2f}'.format(xr2_sl.value)+"\n\n")


def change_background(m):
    scene.background = menu_colors[m.index]
    my_label.background = scene.background

wtext(text="Background color = ")
menu_text = [ "Preto", "Roxo", "Ciano", "Laranja", "Branco" ]
menu_colors = [ color.black, color.magenta, color.cyan, color.orange, color.white]
bg_menu = menu(bind=change_background, choices = menu_text)

#Movimento
t = 0
dt = 0.0001

while True:
  rate(100000)
  
  if not run:continue
  
  M3 = xm1_sl.value
  M1 = xm2_sl.value
  M2 = xm3_sl.value
  R1 = xr1_sl.value
  R2 = xr2_sl.value
  
  #Equacao de X dois pontos:
  Xddot=0.5*(-R1*M1**2*sin(theta1)*theta1dot**2 - R1*M1*M2*(sin(2*theta2 - 3*theta1) + sin(2*theta2 - theta1))*theta2dot*theta1dot/4 + R1*M1*M2*(sin(2*theta2 - 3*theta1) + sin(2*theta2 - theta1))*theta1dot**2/4 - R1*M1*M2*(sin(2*theta2 - theta1) + sin(2*theta2 + theta1))*theta2dot*theta1dot/4 + R1*M1*M2*sin(theta2 - theta1)*cos(theta2)*theta2dot*theta1dot - R1*M1*M2*sin(theta2 - theta1)*cos(theta2)*theta1dot**2 + R1*M1*M2*sin(theta2)*cos(theta2 - theta1)*cos(theta1)**2*theta2dot*theta1dot + R1*M1*M2*sin(theta1)*cos(theta2 - theta1)**2*theta1dot**2 - R1*M1*M2*sin(theta1)*cos(theta2 - theta1)*cos(theta2)*cos(theta1)*theta2dot*theta1dot + R1*M1*M2*sin(theta1)*cos(theta2)**2*theta2dot*theta1dot - 2.0*R1*M1*M2*sin(theta1)*theta1dot**2 - R1*M2**2*(sin(2*theta2 - 3*theta1) + sin(2*theta2 - theta1))*theta2dot*theta1dot/4 + R1*M2**2*(sin(2*theta2 - 3*theta1) + sin(2*theta2 - theta1))*theta1dot**2/4 - R1*M2**2*(sin(2*theta2 - theta1) + sin(2*theta2 + theta1))*theta2dot*theta1dot/4 + R1*M2**2*sin(theta2 - theta1)*cos(theta2)*theta2dot*theta1dot - R1*M2**2*sin(theta2 - theta1)*cos(theta2)*theta1dot**2 + R1*M2**2*sin(theta2)*cos(theta2 - theta1)*cos(theta1)**2*theta2dot*theta1dot + R1*M2**2*sin(theta1)*cos(theta2 - theta1)**2*theta1dot**2 - R1*M2**2*sin(theta1)*cos(theta2 - theta1)*cos(theta2)*cos(theta1)*theta2dot*theta1dot + R1*M2**2*sin(theta1)*cos(theta2)**2*theta2dot*theta1dot - R1*M2**2*sin(theta1)*theta1dot**2 - R2*M1*M2*(-sin(theta2 - 2*theta1) + sin(theta2 + 2*theta1))*theta2dot*theta1dot/4 + R2*M1*M2*sin(theta2 - theta1)*cos(theta1)*theta2dot**2 - R2*M1*M2*sin(theta2 - theta1)*cos(theta1)*theta2dot*theta1dot + R2*M1*M2*sin(theta2)*cos(theta1)**2*theta2dot*theta1dot - R2*M1*M2*sin(theta2)*theta2dot**2 - R2*M2**2*(-sin(theta2 - 2*theta1) + sin(theta2 + 2*theta1))*theta2dot*theta1dot/4 - R2*M2**2*(sin(theta2 - 2*theta1) + sin(3*theta2 - 2*theta1))*theta2dot**2/4 + R2*M2**2*(sin(theta2 - 2*theta1) + sin(3*theta2 - 2*theta1))*theta2dot*theta1dot/4 + R2*M2**2*sin(theta2 - theta1)*cos(theta1)*theta2dot**2 - R2*M2**2*sin(theta2 - theta1)*cos(theta1)*theta2dot*theta1dot + R2*M2**2*sin(theta2)*cos(theta2 - theta1)**2*theta2dot**2 - R2*M2**2*sin(theta2)*cos(theta2 - theta1)*cos(theta2)*cos(theta1)*theta2dot*theta1dot + R2*M2**2*sin(theta2)*cos(theta1)**2*theta2dot*theta1dot - R2*M2**2*sin(theta2)*theta2dot**2 + R2*M2**2*sin(theta1)*cos(theta2 - theta1)*cos(theta2)**2*theta2dot*theta1dot - g*M1**2*sin(2*theta1)/2 + g*M1*M2*sin(theta2)*cos(theta2 - theta1)*cos(theta1) - g*M1*M2*sin(2*theta2)/2 + g*M1*M2*sin(theta1)*cos(theta2 - theta1)*cos(theta2) - 1.0*g*M1*M2*sin(2*theta1) + g*M2**2*sin(theta2)*cos(theta2 - theta1)*cos(theta1) - g*M2**2*sin(2*theta2)/2 + g*M2**2*sin(theta1)*cos(theta2 - theta1)*cos(theta2) - g*M2**2*sin(2*theta1)/2)/(-0.5*M3*M1 - 0.5*M3*M2*sin(theta2)**2 + 1.0*M3*M2*sin(theta2)*sin(theta1)*cos(theta2 - theta1) - 0.5*M3*M2*sin(theta1)**2 - 0.5*M1**2*sin(theta1)**2 - 0.5*M1*M2*sin(theta1)**2)
  
  #Equacao de Theta dois pontos:
  theta1ddot=(-0.25*R1*M3*M2*sin(2*theta2 - 2*theta1)*theta1dot**2 + 0.25*R1*M1**2*sin(2*theta1)*theta1dot**2 + 0.25*R1*M1*M2*sin(2*theta1)*theta1dot**2 - 0.5*R2*M3*M2*sin(theta2 - theta1)*theta2dot**2 - 0.25*R2*M1*M2*sin(theta2 - theta1)*theta2dot**2 + 0.25*R2*M1*M2*sin(theta2 + theta1)*theta2dot**2 + 0.5*g*M3*M1*sin(theta1) - 0.25*g*M3*M2*sin(2*theta2 - theta1) + 0.25*g*M3*M2*sin(theta1) + 0.5*g*M1**2*sin(theta1) + 0.5*g*M1*M2*sin(theta1))/(R1*(-0.5*M3*M1 + 0.25*M3*M2*cos(2*theta2 - 2*theta1) - 0.25*M3*M2 + 0.25*M1**2*cos(2*theta1) - 0.25*M1**2 + 0.25*M1*M2*cos(2*theta1) - 0.25*M1*M2))
  
  #Equacaod e Phi dois pontos:
  theta2ddot=0.5*M3*(1.0*R1*M1*sin(theta2 - theta1)*theta1dot**2 + 1.0*R1*M2*sin(theta2 - theta1)*theta1dot**2 + 0.5*R2*M2*sin(2*theta2 - 2*theta1)*theta2dot**2 + 0.5*g*M1*sin(theta2 - 2*theta1) + 0.5*g*M1*sin(theta2) + 0.5*g*M2*sin(theta2 - 2*theta1) + 0.5*g*M2*sin(theta2))/(R2*(-0.5*M3*M1 + 0.25*M3*M2*cos(2*theta2 - 2*theta1) - 0.25*M3*M2 + 0.25*M1**2*cos(2*theta1) - 0.25*M1**2 + 0.25*M1*M2*cos(2*theta1) - 0.25*M1*M2))



  theta2dot = theta2dot + theta2ddot*dt
  theta1dot = theta1dot + theta1ddot*dt
  Xdot = Xdot + Xddot*dt
  theta1 = theta1 + theta1dot*dt
  theta2 = theta2 + theta2dot*dt
  X = X + Xdot*dt
  t = t + dt
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
  
  
  
  scene.camera.follow(pivot)
  T = .5*M1*R1**2*theta1dot**2 +.5*M2*(R2**2*theta2dot**2+2*R1*R2*theta1dot*theta2dot*cos(theta1-theta2)+R1**2*theta1dot**2)
  U = -(M1+M2)*g*R1*cos(theta1)-M2*g*R2*cos(theta2)
  if graphing:
        dpos1 = bar1.pos-pos1
        dpos2 = bar2.pos-pos2
        Ktrans1 = .5*M1*mag2(dpos1/dt)
        Ktrans2 = .5*M2*mag2(dpos2/dt)
        Krot1 = .5*I1*thetadot1**2
        Krot2 = .5*I2*thetadot2**2
        PE1 = M1*g*(bar1.pos.y-y1)
        PE2 = M2*g*(bar2.pos.y-y2)
        total = Ktrans1+Ktrans2+Krot1+Krot2+PE1+PE2
        energy.plot(t, total)
        krot.plot(t,Krot1+Krot2)
        ktrans.plot(t,Ktrans1+Ktrans2)
        PE.plot(t,PE1+PE2)