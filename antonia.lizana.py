#me faltaba un ":" y estuve media hora buscando el prpoblema x un simple : ....
from random import randint
estudiante = []
alumnos = []
alumno_guardado = []
while True:
 print("***menu insituto***")
 print ("1) grabar")
 print ("2) buscar")
 print ("3) imprimir")
 print ("4) salir")
 opc = int(input("ingrese una opcion "))
 if opc == 1:

     nombre = input("ingrese un nombre: ")
     apellido = input ("ingrese un apellido: ")
     fecha = input ("ingrees una fecha de nacimiento: ")
     carrera = input ("ingrese una carrera: ")
     nota = int (input("ingrese un promedio de notas: "))
     asignatura = input ("ingrese la asignatura: ")
     numero = int (input("ingrese un numero de lista: "))
     rut = input("ingrese rut del alumno (sin guion):")
     if len(rut) ==9:
     if (rut [:8].isdigit() and rut[8:9].indigit () or (rut[:8] and rut [8:9] == "k"))
            print (f"Rut ingresado: {rut[:8]} - {rut[8:9]}")
            alumno_guardado.append (rut)
     else:
        print ("ingrese rut correcto :<")
        print ("************************")

     
     print ("los datos se han añadido ;)")
     
     for i in estudiante:
       print (f"run        :{i[0]}")
       print (f"nombre     :{i[1]}")
       print (f"apellido   :{i[2]}")
       print (f"fecha      :{i[3]}")
       print (f"carrera    :{i[4]}")
       print (f"nota       :{i[5]}")
       print (f"asignatura :{i[6]}")
       print (f"numero     :{i[7]}")
     break
 elif opc == 2:
   rut = input ("ingrese rut")
   for i in estudiante:
     if i (0) == rut:
         print ( "EL RUT NO ES ENCONTRADO :<")
         print (f"run :{i[0]}")
         print (f"nombre :{i[1]}")
         print (f"apellido :{i[2]}")
         print (f"fecha :{i[3]}")
         print (f"carrera :{i[4]}")
         print (f"nota :{i[5]}")
         print (f"asignatura :{i[6]}")
         print (f"numero :{i[7]}")
         break
     else:
         print("el estudiante no ha sido encontrado :<")   
 elif opc == 3:
  while True:
            print ("certificados")
            
            print ("1.- certificado alumno regular")
            print ("2.- certificado notas")
            print ("3.- salir de impresion")
            resp = int (input("ingrese una opcion: "))
            if resp == 1:
                print ("1.-certificado de alumno regular")
                while True:
                    rut = input ("ingrese un rut")
                    if len(rut) == 6:
                        if (rut[:4].isdigit()) or (rut[:2].isalpha() and rut [2:].isdigit ()):
                            break
                        for i in rut:
                            if i[0] == rut:
                                print ("rut no identificado")
                                print ("********************")
                                print ("certificado alumno regular")
                                print (f"run :{i[0]}")
                                print (f"carrera :{i[4]}")
                                numero = randint (1000,5000)
                                print (f"valor :${numero}")
                                break
                        else:
                            print ("estudiante no valido :<")
                    elif resp == 2:
                        print ("2- certificadp de notas")
                        while True:
                            patente = inpout ("ingrese su rut")
                            if len (rut) == 6:
                                if (rut [:4].isalpha()and rut[4:].isdigit ())
                                dsgbreak
                            for i in estudianre:
                                if i [0] == patente:
                                    print ("estudianre encontrafo :)")
                                    print ("*************************")
                                    print ("tipo de certificado: certificado de notas")
                                    print(f"asignatura : {i[6]}")
                                    print(f"promedio : {i[5]}")
                                    numero = radint (1000,5000)
                                    print (f"valor :${numero}")
                                    break
            elif resp == 3:
             print ("has salido de esta opcion")
            break
elif opc == 4:
 print ("has abandonado el menu :<")
break