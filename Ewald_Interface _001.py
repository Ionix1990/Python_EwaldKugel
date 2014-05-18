# -*- coding: cp1252 -*-
from Tkinter import *
import tkMessageBox 
from visual import sphere,color,materials,arrow
from numpy.linalg import norm
import numpy as np

# Variablen

a1 =[]
a2 = []
a3 = []

u  = []
v  = []

radiusx=[]
radiusy=[]
radiusz=[]

b1 = []
b2 = []
b3 = []
kp = []
c  = []
a  = []

L1 =0
L2 =0
L3 =0

x=  np.zeros((L1,L2,L3))
y=  np.zeros((L1,L2,L3))
z=  np.zeros((L1,L2,L3))
x2= np.zeros((L1,L2,L3))
y2= np.zeros((L1,L2,L3))
z2= np.zeros((L1,L2,L3))

# Erzeugen des Fensters
app = Tk()
app.title("Ewald Kugel")
app.geometry('450x300+200+200')




#Funktionen:

#Diverse Funktionen die benoetigt werden

def EwaldKugel(x2,y2,z2,L1,L2,L3):
    #Muss noch schoener gemacht werden. Ausgabe des Radiusses
    radiusx.append(x2[int(s)/2,int(n)/2,int(j)/2])
    radiusy.append(y2[int(s)/2,int(n)/2,int(j)/2])
    radiusz.append(z2[int(s)/2,int(n)/2,int(j)/2])
    radiusx.append(radiusx[0]+k)
    radiusy.append(y2[int(s)/2,int(n)/2,int(j)/2])
    radiusz.append(z2[int(s)/2,int(n)/2,int(j)/2])
    radiusx.append(x2[int(s)/2,int(n)/2,int(j)/2])
    radiusy.append(y2[int(s)/2,int(n)/2,int(j)/2])
    radiusz.append(z2[int(s)/2,int(n)/2,int(j)/2])
    radiusx.append(x2[int(s)/2,int(n)/2,int(j)/2])
    radiusy.append(radiusy[0]+k )
    radiusz.append(z2[int(s)/2,int(n)/2,int(j)/2])
    radiusx.append(x2[int(s)/2,int(n)/2,int(j)/2])
    radiusy.append(y2[int(s)/2,int(n)/2,int(j)/2])
    radiusz.append(z2[int(s)/2,int(n)/2,int(j)/2])
    radiusx.append(x2[int(s)/2,int(n)/2,int(j)/2])
    radiusy.append(z2[int(s)/2,int(n)/2,int(j)/2])
    radiusz.append(radiusz[0]+k)



    Ursprungx = radiusx[4]
    Ursprungy = radiusy[4]
    Ursprungz = radiusz[4]
    sphere(pos=[Ursprungx,Ursprungy,Ursprungz],radius=k, material=materials.glass)
    Reflexx=[]
    Reflexy=[]
    Reflexz=[]

    treffer=np.zeros((100,3))
    i= 0
    for s in range(0,L1):
         for n in range(0,L2):
    
             for j in range(0,L3):
                 #if np.abs(np.sqrt((radiusx[4]-x2[s,n,j])**2+(radiusy[4]-y2[s,n,j])**2+(radiusz[4]+k-z2[s,n,j])**2)-k) < 0.01:
                 if np.abs(np.sqrt((radiusx[4]-x2[s,n,j])**2+(radiusy[4]-y2[s,n,j])**2+(radiusz[4]-z2[s,n,j])**2)-k) < 0.01:
                     treffer[i,0]= x2[s,n,j]
                     treffer[i,1]= y2[s,n,j]
                     treffer[i,2]= z2[s,n,j]
                     Reflexx.append(L1/2-s)
                     Reflexy.append(L2/2-n)
                     Reflexz.append(L3/2-j)
                     sphere(color=color.blue,pos=[x2[s,n,j],y2[s,n,j],z2[s,n,j]],radius=0.3)
                 

                     i = i +1
    return()


def Gittercalc(a1,a2,a3,L1,L2,L3):
    x=  np.zeros((L1,L2,L3))
    y=  np.zeros((L1,L2,L3))
    z=  np.zeros((L1,L2,L3))
    x2= np.zeros((L1,L2,L3))
    y2= np.zeros((L1,L2,L3))
    z2= np.zeros((L1,L2,L3))
    c1 = (cross(a2,a3))
    b1 = (divv(c1,skalar(a1,c1)))
    c=[]
    a=[]
    c2 = (cross(a3,a1))
    b2 = (divv(c2,skalar(a1,c1)))
    c=[]
    a=[]
    c3 = (cross(a1,a2))
    b3 = (divv(c3,skalar(a1,c1)))

    for s in range(0,L1):
        for n in range(0,L2):
    
           for j in range(0,L3):
               x[s,n,j] = a1[0]*n+a2[0]*j+a3[0]*s
               y[s,n,j] = a1[1]*n+a2[1]*j+a3[1]*s 
               z[s,n,j] = a1[2]*n+a2[2]*j+a3[2]*s
               x2[s,n,j]= b1[0]*n+b2[0]*j+b3[0]*s
               y2[s,n,j]= b1[1]*n+b2[1]*j+b3[1]*s
               z2[s,n,j]= b1[2]*n+b2[2]*j+b3[2]*s
               sphere(color=color.green,pos=[x[s,n,j],y[s,n,j],z[s,n,j]],radius=0.3)
               "sphere(color=color.red,pos=[x2[s,n,j],y2[s,n,j],z2[s,n,j]],radius=0.3)"
               
    return()


def cross(u,v):
    for i in range(0,3):
        if i == 0 :
            c.append((u[i+1]*v[2])-(u[2]*v[i+1]))
        if i == 1 :
            c.append((u[2]*v[0])-(u[0]*v[2]))
        if i == 2 :
            c.append((u[0]*v[i-1])-(u[i-1]*v[0]))
    return(c)



def skalar(u,v):
    sk = 0
    for i in range(0,3):
        sk = sk+(u[i]*v[i]) 
    
    return(sk)	


def divv(u,v):
    for i in range(0,3):
        a.append((2*np.pi)*u[i]/v)

    return(a)

def checktype(v1,v2,v3):
    if skalar(v1,v2)==0 and skalar(v2,v3)==0 and skalar(v1,v3)== 0:
        if norm(v1)==norm(v2) and norm(v2)==norm(v3):
            return("kubisches")
        if norm(v1)==norm(v2) and norm(v1)<>norm(v3) or norm(v2)==norm(v3) and norm(v1)<> norm(v3) or norm(v1)==norm(v3) and norm(v1)<> norm(v2) :
            return("tetragonales")
        if norm(v1)<>norm(v2)<>norm(v3):
            return("orthorombisches")
    return("")


# Funktionen der GUI Elemente


def compute():
    # Einlesen der Variablen
    
    L1= int(dim1text.get())
    L2= int(dim2text.get())
    L3= int(dim3text.get())

    a1.append(int(vec11.get()))
    a1.append(int(vec12.get()))
    a1.append(int(vec13.get()))

    a2.append(int(vec21.get()))
    a2.append(int(vec22.get()))
    a2.append(int(vec23.get()))

    a3.append(int(vec31.get()))
    a3.append(int(vec32.get()))
    a3.append(int(vec33.get()))

    Gittercalc(a1,a2,a3,L1,L2,L3)
    
    
    return()



#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#--------------------------------------GUI-----------------------------------------------------
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

#Start Button

button1 = Button(app,text= "compute!", width =20,command=compute)
button1.place(x =250, y=250)

#Wellenlänge
wellenltext = StringVar(None)
wellenl =Entry(app, textvariable= wellenltext)
wellenl.place(x= 250,y=60, width=30)

#Eingabe der Vektoren

# 1.Vektor
label1= Label(app, text ="Vek 1",height = 10)
label1.place(x=25,y= 20,width=60, height=15)


vec11= StringVar(None)
text11 =Entry(app, textvariable =vec11)
text11.place(x = 40, y = 40, width=30, height=20)
vec12= StringVar(None)
text12 =Entry(app, textvariable =vec12)
text12.place(x = 40, y = 65, width=30, height=20)
vec13= StringVar(None)
text13 =Entry(app, textvariable =vec13)
text13.place(x = 40, y = 90, width=30, height=20)

# 2.Vektor
label2 = Label(app, text ="Vek 2",height = 10)
label2.place(x=85,y= 20,width=60, height=15)


vec21= StringVar(None)
text21 =Entry(app, textvariable =vec21)
text21.place(x = 100, y = 40, width=30, height=20)
vec22= StringVar(None)
text22 =Entry(app, textvariable =vec22)
text22.place(x = 100, y = 65, width=30, height=20)
vec23= StringVar(None)
text23 =Entry(app, textvariable =vec23)
text23.place(x = 100, y = 90, width=30, height=20)

# 3.Vektor
label3 = Label(app, text ="Vek 3",height = 10)
label3.place(x=145,y= 20,width=60, height=15)


vec31= StringVar(None)
text31 =Entry(app, textvariable =vec31)
text31.place(x = 160, y = 40, width=30, height=20)
vec32= StringVar(None)
text32 =Entry(app, textvariable =vec32)
text32.place(x = 160, y = 65, width=30, height=20)
vec33= StringVar(None)
text33 =Entry(app, textvariable =vec33)
text33.place(x = 160, y = 90, width=30, height=20)

#--------Dimension des Gitters-------
label4 = Label(app, text ="Dimension des Gitters:",height = 10)
label4.place(x=20,y= 130,width=150, height=15)

dim1text= StringVar(None)
dim1 =Entry(app, textvariable =dim1text)
dim1.place(x = 35, y = 150, width=30, height=20)

dim2text= StringVar(None)
dim2 =Entry(app, textvariable =dim2text)
dim2.place(x = 90, y = 150, width=30, height=20)

dim3text= StringVar(None)
dim3 =Entry(app, textvariable =dim3text)
dim3.place(x = 150, y = 150, width=30, height=20)

label5 = Label(app, text ="x",height = 10)
label5.place(x=75,y= 150,width=5, height=15)

label6 = Label(app, text ="x",height = 10)
label6.place(x=130,y= 150,width=5, height=15)



# Checkboxen für Reziprokes Gitter sowie Ewaldkugel
checkBox1Val = IntVar()
checkBox1 = Checkbutton(app, variable=checkBox1Val, text="Ewald Kugel")
checkBox1.place(x=20, y= 200)

checkBox2Val = IntVar()
checkBox2 = Checkbutton(app, variable=checkBox2Val, text="reziprokes Gitter")
checkBox2.place(x=120, y= 200)


app.mainloop()
