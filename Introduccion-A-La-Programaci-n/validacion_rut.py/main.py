from py_cache import validar_rut

def main():
    rut_usuario = input("Ingrese un RUT para validar: ")
    if validar_rut(rut_usuario):
        print("El RUT ingresado es válido.")
    else:
        print("El RUT ingresado es inválido.")

    main()

    #holaaaaaaaaaaaa
    
