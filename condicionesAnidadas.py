# Condiciones anidadas Elif

sensornivelAgua=int(input("Dijite el nivel de agua actual: "))

if(sensornivelAgua>=0 and sensornivelAgua<20):
    print(f'PELIGRO! EL NIVEL  {sensornivelAgua} ES PELIGROSO')
elif(sensornivelAgua>=20  and sensornivelAgua<400):
    print(f'Hidroituando funciona OK! {sensornivelAgua}')
elif(sensornivelAgua>=400):
    print(f'PELIGRO! EL NIVEL  {sensornivelAgua} ES PELIGROSO')
else:
    print("El nivel del agua no es valido")

#ESTACIONES

estacionesdelaño=int(input('Dijite el mes del año: '))

