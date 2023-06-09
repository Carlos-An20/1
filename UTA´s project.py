from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image, ImageChops, ImageEnhance, ImageOps #llama a las imagenes
import math # librerias matematica 

### ventana principal##
ventana = Tk()
ventana.title("Movimiento Armonico Simple")
#ventana.geometry("630x450")
ventana.geometry("740x500")
#creacion de las funciones


##logo

## imagen del encabezado###

imagen=PhotoImage(file="header2.PNG")
imagen = imagen.zoom(1) #with 250,
imagen = imagen.subsample(2, 2)
Limag=Label(ventana,image=imagen).place(x=0,y=0)


Fi= Frame(ventana, width=100,highlightbackground='RED',highlightthicknes=0.5) #cuadors dentro de la ventana

Fi.grid(row=0, column=1,padx=100,pady=190,ipadx=10,ipady=53)

imagen2=PhotoImage(file="icono.png")

imagen2 = imagen2.subsample(2, 2)
Limag=Label(Fi,image=imagen2).place(x=0,y=0)


FP= Frame(ventana, width=100,highlightbackground='RED',highlightthicknes=0.5, bg='#49A') #cuadors dentro de la ventana 
FP.grid(row=0, column=0,padx=70,pady=150,ipadx=55,ipady=100)
L1=Label(FP,text="Integrantes:", fg="red",font=("Verdana",12),bg='#49A')  # plot en los ejes x y
L1.place(x=10,y=10)




L1=Label(FP,text="Domenica Montalvo",  font=("Roboto Cn",9),bg='#49A')  # plot en los ejes x y 
L1.place(x=10,y=30)
L1=Label(FP,text="Adrian Oñate",  font=("Roboto Cn",9),bg='#49A')  # plot en los ejes x y 
L1.place(x=10,y=50)
L1=Label(FP,text="Pablo Nuñez",  font=("Roboto Cn",9),bg='#49A')  # plot en los ejes x y 
L1.place(x=10,y=70)
L1=Label(FP,text="Anthony Cali",  font=("Roboto Cn",9),bg='#49A')  # plot en los ejes x y 
L1.place(x=10,y=90)
L1=Label(FP,text="Luis Paredes",  font=("Roboto Cn",9),bg='#49A')  # plot en los ejes x y 
L1.place(x=10,y=110)
L1=Label(FP,text="Erick Torres",  font=("Roboto Cn",9),bg='#49A')  # plot en los ejes x y 
L1.place(x=10,y=130)
L1=Label(FP,text="Mateo Melendez",  font=("Roboto Cn",9),bg='#49A')  # plot en los ejes x y 
L1.place(x=10,y=150)

def calculos():   
    
    FP.grid_forget()
    F1= Frame(ventana, width=100,highlightbackground='GRAY',highlightthicknes=0.5) #cuadors dentro de la ventana 
    F1.grid(row=0, column=0,padx=10,pady=190,ipadx=35,ipady=50)
    L1=Label(F1,text="Calculos",  font=("Roboto Cn",10))  # plot en los ejes x y 
    L1.place(x=10,y=10)
    
    valores=['Posicion','Velocidad Angular','Frecuencia','Periodo','Velocidad','Velocidad Max','Aceleracion','Aceleracion Max', 'Fuerza', 'Constante','Energia Potencial','Energia Cinetica','Energia Mecanica']

    combobox = ttk.Combobox(F1, width='20',values=valores,state='readonly')

    combobox.place(x=20,y=35)
    
    def posicion(event=None):  # cambiar nombre 

        #Calculo de Posicion
        if combobox.get() == valores[0]:  ## ayuda de amigo                    
            
            F2= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5) # cuadro mas grande ### 
            F2.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)

            name=Label(F2,text=" Calculo de la Posicion", font=("Roboto Cn",10)) #titulo..change
            name.place(x=90,y=10)

            #ajustarpos
            L2=Label(F2,text="Amplitud")
            L2.place(x=20,y=35)
            E2=Entry(F2,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F2,text="Velocidad Angular")
            L3.place(x=220,y=35)
            E3=Entry(F2,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)

            L4=Label(F2,text="Tiempo")
            L4.place(x=20,y=110)
            E4=Entry(F2,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=20,y=130)
            
            L5=Label(F2,text="Desface")
            L5.place(x=220,y=110)
            E5=Entry(F2,relief="ridge", font=("Roboto Cn",10))
            E5.place(x=220,y=130)            
            
            #ajustar pos
            L6=Label(F2,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L6.place(x=20,y=255)
            E6=Entry(F2,relief="ridge", font=("Roboto Cn",10))  ###solo es el output
            E6.place(x=20,y=280)
            
            def cal():
                
                valor1= int(E2.get()) #aceleracion
                valor2= int(E3.get())   #vel A
                valor3= int(E4.get())   #Time
                valor4= int(E5.get())   #desface
                ##valor5= int(E6.get()) ##### RESULTADO ##### output
                

                x= valor1 * math.cos ((valor2*valor3)+ valor4)
                print('Calculo de la posicion realizado')

                
                    
                E6.delete(0,END)
                E6.insert(0,round(x,2))   # con dos decimales
        

            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                E5.delete(0,END)
                E6.delete(0,END)               
                ### E5.delete(0,END)


            boton1 = Button(F2, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F2, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)




        #calculo de Velocidad Angular                       
        elif combobox.get() == valores[1]:
            F2= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5) # cuadro mas grande ### 
            F2.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)

            name=Label(F2,text=" Calculo de la Velocidad Angular", font=("Roboto Cn",10)) #titulo..change
            name.place(x=90,y=10)

            #ajustarpos
            L2=Label(F2,text="Periodo")
            L2.place(x=20,y=35)
            E2=Entry(F2,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            #ajustar pos
            L6=Label(F2,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L6.place(x=20,y=230)
            E6=Entry(F2,relief="ridge", font=("Roboto Cn",10))  ###solo es el output
            E6.place(x=20,y=255)
            
            def cal2():
                
                val= int(E2.get()) #aceleracion
                x = (2 * 3.141598)  / val
                print('Calculo velocidad Angular')
      
                E6.delete(0,END)
                E6.insert(0,round(x,2))   # con dos decimales
        

            def clearTextInput():##borrar 

                E2.delete(0,END)

                E6.delete(0,END)               
                ### E5.delete(0,END)


            boton1 = Button(F2, text="Calcular",bd=1,command=cal2, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F2, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)

        ##### Calculo Frecuencia  #####                       
        elif combobox.get() == valores[2]:
            F4= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F4.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F4,text=" Calculo de la Frecuencia", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F4,text="Velocidad Angular") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F4,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

                
            L4=Label(F4,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L4.place(x=150,y=140)
            E4=Entry(F4,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=120,y=165)
            
            def cal():
        
                val2= int(E2.get())

 
                x = val2 * (2*3.1416)
                print('Calculo de frecuencia')
      
                E4.delete(0,END)
                E4.insert(0,round(x,2))   # con dos decimales
                

            def clearTextInput():##borrar 

                E2.delete(0,END)

                E4.delete(0,END)
                ####
                ### E5.delete(0,END)


            boton1 = Button(F4, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F4, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)



        


        #Calculo de:PERIODO
        elif combobox.get() == valores[3]:
            F5= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F5.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F5,text=" Calculo del Periodo ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F5,text="Masa") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F5,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F5,text="Constante")
            L3.place(x=222,y=35)
            E3=Entry(F5,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)

            L4=Label(F5,text="Longitud") ####esta en la mismo pos que L3 and E3   tienes que cambiar la pos
            L4.place(x=165,y=110)
            E4=Entry(F5,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=120,y=130)

                
            L5=Label(F5,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L5.place(x=20,y=255)
            E5=Entry(F5,relief="ridge", font=("Roboto Cn",10))
            E5.place(x=20,y=280)
            
            def cal():
        
                v1= int(E2.get()) #masa
                v2= int(E3.get()) # k constante
                v3= int(E4.get())#Longitud????
                ##la es la grabedad

                #just masa and k
                if ( v3 == 0):
                    x1 = (2*3.1416)* math.sqrt(v1/v2)
                    E5.delete(0,END)
                    E5.insert(0,round(x1,2))   # con dos decimales

                #just long and grabe
                elif(v2 == 0 and v1 == 0):
                    x2 = (2*3.1416)* math.sqrt(v3/9.8)
                    E5.delete(0,END)
                    E5.insert(0,round(x2,2))   # con dos decimales

            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                E5.delete(0,END) 
                ####
                ### E5.delete(0,END)


            boton1 = Button(F5, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F5, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)           
  

        ####calculo de: VELOCIDAD
        elif combobox.get() == valores[4]:
            F6= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F6.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F6,text=" Calculo Velocidad ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F6,text="Velocidad Angular") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F6,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F6,text="Amplitud")
            L3.place(x=220,y=35)
            E3=Entry(F6,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)

            L4=Label(F6,text="Desface") ####esta en la mismo pos que L3 and E3   tienes que cambiar la pos
            L4.place(x=220,y=110)
            E4=Entry(F6,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=220,y=130)
            
           

            L6=Label(F6,text="Tiempo") ####esta en la mismo pos que L3 and E3   tienes que cambiar la pos
            L6.place(x=20,y=110)
            E6=Entry(F6,relief="ridge", font=("Roboto Cn",10))
            E6.place(x=20,y=130)                

            L7=Label(F6,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L7.place(x=20,y=255)
            E7=Entry(F6,relief="ridge", font=("Roboto Cn",10))
            E7.place(x=20,y=280)
            
            def cal():
        
                va1= int(E2.get()) #vel angular 
                va2= int(E3.get()) # acele
                va3= int(E4.get())#### desf
                va5= int(E6.get())# time

                x = (-(va1))*va2*math.sin(va1*va5 + va3)

                E7.delete(0,END)
                E7.insert(0,round(x,2))   # con dos decimales

            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)

                E6.delete(0,END)
                E7.delete(0,END)                
                ### E5.delete(0,END)


            boton1 = Button(F6, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F6, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)


            
        ### calculo de: Velocidad Maxima
        elif combobox.get() == valores[5]:
            F7= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F7.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F7,text=" Calculo Velocidad Maxima ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F7,text="Amplitud") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F7,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F7,text="Velocidad angular")
            L3.place(x=220,y=35)
            E3=Entry(F7,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)
                
            L4=Label(F7,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L4.place(x=20,y=140)
            E4=Entry(F7,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=20,y=165)
            
            def cal():
        
                a1= int(E2.get()) ## acele
                a2= int(E3.get()) # vel ang

                x = a1 * a2

                E4.delete(0,END)
                E4.insert(0,round(x,2))   # con dos decimales


            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)



            boton1 = Button(F7, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F7, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)
        
        
        ## calulo de :Aceleracion
        elif combobox.get() == valores[6]:
            F8= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F8.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F8,text=" Calculo de la Aceleracion ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F8,text="Velocidad Angular") #ajustar o a;adir labels and Entrys
            L2.place(x=17,y=35)
            E2=Entry(F8,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F8,text="Amplitud")
            L3.place(x=230,y=35)
            E3=Entry(F8,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=230,y=60)

            L4=Label(F8,text="Tiempo") ####esta en la mismo pos que L3 and E3   tienes que cambiar la pos
            L4.place(x=230,y=110)
            E4=Entry(F8,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=230,y=130)

            L6=Label(F8,text="Desface") ####esta en la mismo pos que L3 and E3   tienes que cambiar la pos
            L6.place(x=20,y=110)
            E6=Entry(F8,relief="ridge", font=("Roboto Cn",10))
            E6.place(x=20,y=130)                

            L7=Label(F8,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L7.place(x=20,y=255)
            E7=Entry(F8,relief="ridge", font=("Roboto Cn",10))
            E7.place(x=20,y=280)
            
            def cal():
        
                e1= int(E2.get()) ##vel an ***elevar al cuadrado
                e2= int(E3.get()) # aceleracion 
                e3= int(E4.get())####time
                e4= int(E6.get())#desface
             ## ya se tiene la vel angu

                x =  (-(pow(e1,2)))* e2 * math.cos(e1*e3+e4)


                E7.delete(0,END)
                E7.insert(0,round(x,2))   # con dos decimales


            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)

                E6.delete(0,END)
                E7.delete(0,END)                
                ### E5.delete(0,END)


            boton1 = Button(F8, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F8, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)            

### Calculo de: Aceleracion Maxima 
        elif combobox.get() == valores[7]:
            F9= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F9.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F9,text=" Calculo Aceleracion Maxima ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F9,text="Amplitud") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F9,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F9,text="Velocidad angular")
            L3.place(x=210,y=35)
            E3=Entry(F9,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)
                
            L4=Label(F9,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L4.place(x=20,y=140)
            E4=Entry(F9,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=20,y=165)
            
            def cal():
        
                r1= int(E2.get())
                r2= int(E3.get())

                x =  r1 *(pow(r2,2))

                E4.delete(0,END)
                E4.insert(0,round(x,2))   # con dos decimales

                
            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                ####
                ### E5.delete(0,END)


            boton1 = Button(F9, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F9, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)

#### Calculo de la Fuerza ###      
        elif combobox.get() == valores[8]:
            F10= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F10.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F10,text=" Calculo de Fuerza ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F10,text="Constante") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F10,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F10,text="Posicion")
            L3.place(x=210,y=35)
            E3=Entry(F10,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)
                
            L4=Label(F10,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L4.place(x=20,y=140)
            E4=Entry(F10,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=20,y=165)
            
            def cal():
        
                g1= int(E2.get()) #costa
                g2= int(E3.get()) #pos


                x =  -(g1)*g2

                E4.delete(0,END)
                E4.insert(0,round(x,2))   # con dos decimales



            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                ####
                ### E5.delete(0,END)


            boton1 = Button(F10, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F10, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)
            
#### Calculo Constante ####
        elif combobox.get() == valores[9]:
            F11= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F11.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F11,text=" Calculo Constante ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F11,text="Masa") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F11,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F11,text="Velocidad Angular")
            L3.place(x=220,y=35)
            E3=Entry(F11,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)
                
            L4=Label(F11,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L4.place(x=20,y=140)
            E4=Entry(F11,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=20,y=165)
            
            def cal():
        
                q1= int(E2.get())#masa
                q2= int(E3.get())#vel


                x =  q1 * (pow(q2,2))

                E4.delete(0,END)
                E4.insert(0,round(x,2))   # con dos decimales


            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                ####
                ### E5.delete(0,END)


            boton1 = Button(F11, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F11, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)        
            
####Calculo Energia Potencial ###
        elif combobox.get() == valores[10]:
            F12= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F12.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F12,text=" Calculo Energia Potencial ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F12,text="Constante") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F12,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F12,text="Posicion")
            L3.place(x=220,y=35)
            E3=Entry(F12,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)
                
            L4=Label(F12,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L4.place(x=20,y=140)
            E4=Entry(F12,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=20,y=165)
            
            def cal():
        
                z1= int(E2.get())
                z2= int(E3.get())

                x = (0.5 * z1)*(pow(z2,2))
                    
                E4.delete(0,END)
                E4.insert(0,round(x,2))   # con dos decimales
  


            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                ####
                ### E5.delete(0,END)


            boton1 = Button(F12, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F12, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)
            
#### Calculo Energia Cinetica ####
        elif combobox.get() == valores[11]:
            F13= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F13.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F13,text=" Calculo Energia Cinetica ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F13,text="Masa") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F13,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F13,text="Velocidad")
            L3.place(x=220,y=35)
            E3=Entry(F13,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)
                
            L4=Label(F13,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L4.place(x=20,y=140)
            E4=Entry(F13,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=20,y=165)
            
            def cal():
        
                t1= int(E2.get())
                t2= int(E3.get())


                x = (0.5 * t1)*(pow(t2,2))
                    
                E4.delete(0,END)
                E4.insert(0,round(x,2))   # con dos decimales
  

            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                ####
                ### E5.delete(0,END)


            boton1 = Button(F13, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F13, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)

        ### energia mecanica
        elif combobox.get() == valores[12]:
            F13= Frame(ventana, width=10,highlightbackground='GRAY',highlightthicknes=0.5)
            F13.grid(row=0, column=1,padx=20,pady=140,ipadx=200,ipady=160)
            name=Label(F13,text=" Calculo Energia Mecanica ", font=("Roboto Cn",10)) #cambiar el nombre por  el sig 
            name.place(x=120,y=10)

            L2=Label(F13,text="Constante") #ajustar o a;adir labels and Entrys
            L2.place(x=20,y=35)
            E2=Entry(F13,relief="ridge", font=("Roboto Cn",10))
            E2.place(x=20,y=60)

            L3=Label(F13,text="Amplitud")
            L3.place(x=220,y=35)
            E3=Entry(F13,relief="ridge", font=("Roboto Cn",10))
            E3.place(x=220,y=60)
                
            L4=Label(F13,text="Resultado", width=10, bd=1, relief="ridge", font=("Roboto Cn",10))
            L4.place(x=20,y=140)
            E4=Entry(F13,relief="ridge", font=("Roboto Cn",10))
            E4.place(x=20,y=165)
            
            def cal():
        
                b1= int(E2.get())
                b2= int(E3.get())


                x = (0.5 * b1)*(pow(b2,2))
                    
                E4.delete(0,END)
                E4.insert(0,round(x,2))   # con dos decimales
  

            def clearTextInput():##borrar 

                E2.delete(0,END)
                E3.delete(0,END)
                E4.delete(0,END)
                ####
                ### E5.delete(0,END)


            boton1 = Button(F13, text="Calcular",bd=1,command=cal, relief="ridge", font=("Roboto Cn",10))
            boton2 = Button(F13, text="Limpiar",bd=1,command=clearTextInput, relief="ridge", font=("Roboto Cn",10))
            boton1.place(x=250,y=280)
            boton2.place(x=330,y=280)
            
    
    combobox.bind('<<ComboboxSelected>>', posicion)





mi_menu = Menu(ventana, background='blue', fg='white')
#mi_menu.add_command(label='Principal', command=principal) ### a;adir algo en prini
mi_menu.add_command(label='Calculos', command=calculos) # comando llama a una funcion


#########Salir
def salir():
    salir=messagebox.askquestion("Salir","Desea salir de la Interfaz?")
    if salir == "yes":
        ventana.quit()
        ventana.destroy()

mi_menu.add_command(label='Salir', command=salir)
######end salir
 

ventana.config(menu=mi_menu)
ventana['bg'] = '#49A'


ventana.mainloop()




























