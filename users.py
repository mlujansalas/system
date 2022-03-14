def run():
    admin_users()
    


def admin_users() :
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
            if admin =="admin" and pasw_admin=="admin" :
                os.system("cls")
                print("1.-Crear Usuario")
                print("2.-Editar Usuario")
                print("3.-Eliminar Usuario")
                print("4.-Salir del Sistema")
                var=4
            else:
                print ("Tienes ",3-var," intentos mas")
                s=input("Usuario o Contraseña incorrecto, presione cual tecla para volver a ingresar o (S) para salir: ")
                if s=="s" or s=="S":
                    exit()
        else:
            print(AMARILLO + """
            
Lo sentimos completo los tres intentos, USTED NO ESTA AUTORIZADO A INGRESAR AL SISTEMA""")
            print(RESTABLECER)
           
run()