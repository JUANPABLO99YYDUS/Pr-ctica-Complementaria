import math
def main():
    op = ""
    figuras = []
    while op !="0" :
        
        print("1.-Crear figura \n2.-Listar una clasificacion de figuras\n3.-Listar todas las figuras\n4.-Mostrar suma de todas las areas\n5.-Mostrar suma de todos los perimetros\n6.-Limpiar lista\n0.-Salir")
        op = input("Ingresar una opcion ")
        #Opción 1
        if (op == "1"):
            def menu_figuras():
                fig= ""
                print("1.-Cuadrado\n2.-Triangulo\n3.-Circulo")
                fig = input("Ingresa una opcion de figura ")
                diccionario = ""
                

                if (fig == "1"):
                    l = int(input("Ingresa el lado del cuadrado "))
                    def crear_cuadrado(l):
                        def area_cuadrado(l):
                            a = l * l
                            return a
                        a = area_cuadrado(l)
                        def perimetro_cuadrado(l):
                           p= l * 4
                           return p
                        p = perimetro_cuadrado(l)
                        dic ={"Tipo":"Cuadrado","Area":a,"Perimetro":p}
                        return dic 
                    diccionario = crear_cuadrado(l)

                if ( fig == "2"):
                    lado_a = int(input("Ingresa el primer lado "))
                    lado_b = int(input("Ingresa el segundo lado "))
                    lado_c = int(input("Ingresa el tercer lado "))
                    def crear_triangulo(lado_a,lado_b,lado_c):
                        tip= ""
                        a = 0
                        p = 0
                        if(lado_a == lado_b and lado_b == lado_c):
                            tip = "Triangulo Equilatero"
                            def area_trianguloEquilatero(lado_a):
                                altura = (math.sqrt(3) * lado_a) / 2
                                a = (altura * lado_a)/2
                                return a
                            a= area_trianguloEquilatero(lado_a)
                            def perimetro_trianguloEquilatero(lado_a):
                                p = lado_a * 3
                                return p
                            p= perimetro_trianguloEquilatero

                        if((lado_a != lado_b and lado_a == lado_c) or (lado_a != lado_c and lado_a == lado_b) or (lado_a != lado_b and lado_b == lado_c)):
                            tip = "Triangulo Isosceles"
                            def area_trianguloIsosceles(lado_a, lado_b, lado_c):
                                a=0
                                if (lado_a != lado_b and lado_a == lado_c):
                                   altura = math.sqrt(lado_a * lado_a - (lado_b * lado_b / 4))
                                   a = (lado_b * altura)/2
                                elif (lado_a != lado_c and lado_a == lado_b):
                                    altura = math.sqrt(lado_a * lado_a - (lado_c * lado_c / 4))
                                    a = (lado_c * altura)/2
                                elif(lado_a != lado_b and lado_b == lado_c):
                                    altura = math.sqrt(lado_b * lado_b - (lado_a * lado_a / 4))
                                    a = (lado_a * altura)/2
                                return a
                            a= area_trianguloIsosceles(lado_a,lado_b,lado_c)
                            def perimetro_trianguloIsosceles(lado_a,lado_b,lado_c):
                                p = lado_a + lado_b + lado_c
                                return p
                            p= perimetro_trianguloIsosceles(lado_a,lado_b,lado_c)
                        if(lado_a != lado_b and lado_a != lado_c and lado_b != lado_c):
                            tip = "Triangulo Escaleno"
                            def area_trianguloEscaleno(lado_a,lado_b,lado_c):
                                sp = (lado_a + lado_b + lado_c) /2
                                a = math.sqrt(sp * (sp - lado_a) * (sp - lado_b) * (sp - lado_c))
                                return a
                            a = area_trianguloEscaleno(lado_a,lado_b,lado_c)
                            def perimetro_trianguloEscaleno(lado_a,lado_b,lado_c):
                                p = lado_a + lado_b + lado_c
                                return p
                            p = perimetro_trianguloEscaleno(lado_a,lado_b,lado_c)
                        dic ={"Tipo":tip,"Area":a,"Perimetro":p}
                        return dic
                    diccionario = crear_triangulo(lado_a,lado_b,lado_c)

                if(fig == "3"):
                    r = int(input("Ingresa el radio del circulo "))
                    def crear_circulo(r):
                        def area_circulo(r):
                            a = math.pi * r * r
                            return a
                        a = area_circulo(r)
                        def perimetro_circulo(r):
                            p = 2 * math.pi * r
                            return p
                        p = perimetro_circulo(r)
                        dic = {"Tipo":"Circulo","Area":a,"Perimetro":p}
                        return dic
                    diccionario= crear_circulo(r)
                return diccionario
            agregar = menu_figuras()
            figuras.append(agregar)
            
        # Opción 2
        if (op == "2"):
             print("1.Cuadrado\n2.Circulo\n3.Triangulo\n4.Salir")
             x = int(input("Ingresa una opcion: "))
             
             def listar_clasificacion(clasificar):
                count= 0
                if(x ==1):
                    for i in figuras:
                        if i.get('Tipo') == "Cuadrado":
                            count = count + 1
                            print(i)
                    if (count ==0):
                        print("La clasificación del Cuadrado está vacía")
                elif(x==2):
                    for i in figuras:
                        if i.get('Tipo') == "Circulo":
                            count = count + 1
                            print(i)
                    if (count == 0):
                        print("La clasificación del Circulo está vacía")
                elif(x==3):
                    print("1.Equilatero\n2.Isoceles\n3.Escaleno")
                    y = int(input("Elige un tipo de triangulo: "))
                    if(y==1):
                        for i in figuras:
                            if i.get('Tipo') == "Triangulo Equilatero":
                                count = count + 1
                                print(i)
                        if (count == 0):
                            print("La clasificación de Triangulo Equilatero está vacía")
                    elif(y==2):
                        for i in figuras:
                            if i.get('Tipo') == "Triangulo Isosceles":
                                count = count + 1
                                print(i)
                        if (count == 0):
                            print("La clasificación de Triangulo Isosceles está vacía")
                    elif(y==3):
                        for i in figuras:
                            if i.get('Tipo') == "Triangulo Escaleno":
                                count = count + 1
                                print(i)
                        if (count == 0):
                            print("La clasificación de Triangulo Escaleno está vacía")
                    else:
                        print("NO EXISTE ESE TRIANGULO")
                else:
                    print("NO TE MANEJO MAS OPCIONES")
             listar_clasificacion(x)
             
        #Opción 3
        if (op == "3"):
            for i in figuras:
                print(i)
        if (op == "4"):
            def sumador_areas():
                a1=0
                a2=0
                a3=0
                a4=0
                a5=0
                for i in figuras:
                    if i.get('Tipo') == "Cuadrado":
                        a1 = a1 + int(i.get('Area'))
                    if i.get('Tipo') == "Circulo":
                        a2 = a2 + int(i.get('Area'))
                    if i.get('Tipo') == "Triangulo Equilatero":
                        a3 = a3 + int(i.get('Area'))
                    if i.get('Tipo') == "Triangulo Isosceles":
                        a4 = a4 + int(i.get('Area'))
                    if i.get('Tipo') == "Triangulo Escaleno":
                        a5 = a5 + int(i.get('Area'))
                        
                print(f"La suma de todas las areas de los Cuadrados es: {a1}")
                print(f"La suma de todas las areas  de los Triangulos Equilateros es: {a2}")
                print(f"La suma de todas las areas de los Triangulos Isosceles es: {a3}")
                print(f"La suma de todas las areas  de los Triangulos Escalenos es: {a4}")
                print(f"La suma de todas las areas de los circulos es: {a5}")
            sumador_areas()
        if (op == "5"):
            def sumador_perimetros():
                p1 = 0
                p2 = 0
                p3 = 0
                p4 = 0
                p5 = 0
                for i in figuras:
                    if i.get('Tipo') == "Cuadrado":
                        p1 = p1 + int(i.get('Perimetro'))
                    if i.get('Tipo') == "Circulo":
                        p2 = p2 + int(i.get('Perimetro'))
                    if i.get('Tipo') == "Triangulo Equilatero":
                        p3 = p4 + int(i.get('Perimetro'))
                    if i.get('Tipo') == "Triangulo Isosceles":
                        p4 = p4 + int(i.get('Perimetro'))
                    if i.get('Tipo') == "Triangulo Escaleno":
                        p5 = p5 + int(i.get('Perimetro'))
                        
                print(f"La suma de todos los perimetros de los Cuadrados es: {p1}")
                print(f"La suma de todos los perimetros de los Triangulos Equilateros es: {p2}")
                print(f"La suma de todos los perimetros de los Triangulos Isosceles es: {p3}")
                print(f"La suma de todos los perimetros de los Triangulos Escalenos es: {p4}")
                print(f"La suma de todos los perimetros de los circulos es: {p5}")
                
            sumador_perimetros()
        if (op == "6"):
            figuras.clear()
            print("SE BORRÓ TODA LA LISTA")
        if (op == "0"):
            break
main()
