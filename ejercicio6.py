# -*- coding: cp1252 -*-
edad=int(input( "digite su edad "))

genero=input("digite su sexo , H para hombre , M para mujer ")

if edad>=18:
    
    if genero in  'Hh':
        print (" Se�or , Usted Es Mayor De Edad ")
    elif genero in  'Mm' :
        print (" So�orita , Usted Es Mayor De Edad ")
    else:
        print("dato inorrecto solo mayusculas")
        
else:
    
    if genero in 'Mm':
        print (" Se�ora , Usted Es Menor De Edad ")
    elif genero in  'Hh' :
        print (" So�or , Usted Es Menor De Edad ")
    else:
        print("dato inorrecto solo mayusculas")
        
