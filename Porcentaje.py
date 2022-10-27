import time


def porcentaje() :
 repeat= True
 while repeat:
   print ("Te calculo el porcentaje de tu total")
   print ("total?", end=" " )                      
   A = float(input())                                     #total
   print ("porcentaje?" , end=" ")  
   B = float(input())                                    #porcentaje
   resultado = A* (B / 100)
   if A > resultado :
     print ("Esto es lo que se te descuenta" , resultado )
   else:
     A < resultado 
     print ("Esto es lo que se te recarga", resultado - A) 
     time.sleep (2)
   print ("Quieres calcular algun otro porcentaje? si/no")
   respuesta = str(input())
   if respuesta == "no":
     repeat = False
   else:
     None


   

 
porcentaje ()




