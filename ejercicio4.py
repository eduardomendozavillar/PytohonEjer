num1= int (input ("digite primer numero:  "))
num2= int (input ("digite segundo numero:  "))
operacion= int (input ("diguite para 1 suma , digite 2 para resta ,digite 3 para multiplicasion,digite 4  division "))

if operacion==1:
  print ("la suma es :",(num1+num2))
elif operacion==2:
  print ("la resta es :",(num1-num2))
elif operacion==3:
  print ("la multiplicasion es :",(num1*num2))
elif operacion==4:
  print ("la division es :",(num1/num2))
else:
  print ("porfavor digite un valor correcto para la operacion")
   
        
