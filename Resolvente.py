import math
print ("Esto es para calcular una resolvente de 2do Grado")
print("ingrese A:", end="")
A = float(input ())
print("ingrese B:", end="")
B = float(input ())
print("ingrese C:", end="")
C = float(input ())
D = (-B + math.sqrt(B*B- (4*A*C))) /(2*A)
E = (-B - math.sqrt(B*B- (4*A*C))) /(2*A)
print (D , E)