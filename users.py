def run():
    admin_users()
    #celular()
    #generapuntos()

#Control de Acceso al Sistema
def admin_users() :
    crear_usuario={}
    NEGRO    =  '\033[30m'
    ROJO      =  '\033[31m'
    VERDE    =  '\033[32m'
    AMARILLO   =  '\033[33m'
    AZUL     =  '\033[34m'
    MAGENTA  =  '\033[35m'
    CIAN     =  '\033[36m'
    BLANCO    =  '\033[37m'
    RESTABLECER    =  '\033[39m'
    import os
    import getpass
    os.system("cls")
    var = 0
    while var>=0 and var<3 :
        os.system("cls")
        print("""====Bienvenido al sistema de Calle3====
    
         """)
        admin =input("Ingresa Usuario Administrador : ")
        pasw_admin=getpass.getpass("Ingresa tu contrasena : ")    
        var=var+1
        if var<3 :
            if admin =="admin" and pasw_admin=="admin" :#en este programa los datos de acceso para el administrador es proporcionado por el programador(se modificara posteriormente para que el administrador cambie su contraseña)
                os.system("cls")
                print("1.-Crear Usuario")
                print("2.-Editar Usuario")
                print("3.-Eliminar Usuario")
                print("4.-Salir del Sistema")
                opcion = int(input("Por fvr ingresar una opcion : "))
                
                if opcion == 1:
                    r="S"
                    while r =="S":
                        os.system("cls")
                        print("""====CREAR USUARIO====
                        
                        """)
                        usuario_nuevo = input("Ingresar el nombre completo del nuevo Usuario : ")

                        contrasena_nuevo = input("Ingresa tu contrasena : ")
                        crear_usuario.update({contrasena_nuevo:usuario_nuevo})
                        print("""
                        
                        """)
                        print(AMARILLO,"""LISTO USUARIO AGREGADO
                        
                        """)
                        print(RESTABLECER)
                        r=input("""Si desea ingresar otro usuario presione S, y si no presione cualquier tecla : """)
                        r=r.upper()
                print(VERDE,crear_usuario)
                var=4
                print(RESTABLECER)
            else:
                print ("Tienes ",3-var," intentos mas")
                s=input("Usuario o Contraseña incorrecto, presione cual tecla para volver a ingresar o (S) para salir: ")
                if s=="s" or s=="S":
                    exit()
        else:
            print(AMARILLO + """
            
Lo sentimos completo los tres intentos, USTED NO ESTA AUTORIZADO A INGRESAR AL SISTEMA""")
            print(RESTABLECER)      
#
def celular():
    celu = input("Ingrese el Celular del cliente : ")
    i = 0
    while i == 0:
        if len(celu) == 9: 
            tipo = celu.isdigit()
            if tipo == True:
                print("el numero " + str(celu) + " es correcto")
                print("---------------------------------------")
                print("---------------------------------------")
                print("---------------------------------------")
                i = 1    
            else:
                celu = input("El numero de celular ingresado es incorrecto vuelva ingresar :")
                i = 0
        else:
            celu = input("El numero de celular ingresado es incorrecto vuelva ingresar :")
            i = 0
            
 


def generapuntos():
    i = True
    compras = input("Ingresa monto de compra :")
    while i == True:
        c = compras.isdigit()    
        if c == True:
            r = int(compras)
            g_ptos = int(r / 10)
            if g_ptos >= 1:    
                print("usted genero " + str(g_ptos) + "  puntos por esta compra")
                print("---------------------------------------")
                print("---------------------------------------")
                print("---------------------------------------")
                i = False
            else:
                print("Lo sentimos solo se generan puntos por cada 10 soles de compra")
                print("---------------------------------------")
                print("---------------------------------------")
                print("---------------------------------------")
                i = False
        else:
            i = True
            compras = input("El monto ingresado no existe, por fvr volver a ingresar : ")


run()