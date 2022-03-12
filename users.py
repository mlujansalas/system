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
    if admin =="admin" and pasw_admin=="admin" :

        os.system("cls")
        print("1.-Crear Usuario")
        print("2.-Editar Usuario")
        print("3.-Eliminar Usuario")
        print("4.-Salir del Sistema")
        var=4
    else :
        print ("Tienes ",2-var," intentos mas")
        s=input("Usuario o Contraseña incorrecto, presione cual tecla para volver a ingresar o (S) para salir: ")
        if s=="s" or s=="S":
            exit()
        else :
            var=var+1
