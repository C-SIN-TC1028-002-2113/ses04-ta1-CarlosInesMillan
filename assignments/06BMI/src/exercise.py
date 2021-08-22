def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    imc = peso/altura**2 
    if altura<=0 or peso<=0:
        print("Revisa tus datos, alguno de ellos es erróneo.")
    elif imc<20:
        print("PESO BAJO")
    elif 20<=imc and imc<25:
        print("NORMAL")
    elif 25<=imc and imc<30:
        print("SOBREPESO")
    elif 30<=imc and imc<40:
        print("OBESIDAD")
    elif imc>=40:
        print("OBESIDAD MORBIDA")

if __name__=='__main__':
    main()