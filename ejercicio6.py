# -*- coding: cp1252 -*-
edad=int(input( "digite su edad "))

genero=input("digite su sexo , H para hombre , M para mujer ")

if edad>=18:
    
    if genero in  'Hh':
        print (" Señor , Usted Es Mayor De Edad ")
    elif genero in  'Mm' :
        print (" Soñorita , Usted Es Mayor De Edad ")
    else:
        print("dato inorrecto solo mayusculas")
        
else:
    
    if genero in 'Mm':
        print (" Señora , Usted Es Menor De Edad ")
    elif genero in  'Hh' :
        print (" Soñor , Usted Es Menor De Edad ")
    else:
        print("dato inorrecto solo mayusculas")
        
