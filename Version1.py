class Paciente:

    def __init__(self):
        self.__nom = ""
        self.__id = 0
        self.__sex = ""
        self.__area = ""


    def verNombre(self):
        return self.__nom

    def verCedula(self):
        return self.__id

    def verGenero(self):
        return self.__sex

    def verServicio(self):
        return self.__area


    def asignarNombre(self, nombre):
        self.__nom = nombre

    def asignarCedula(self, cedula):
        self.__id = cedula

    def asignarGenero(self, genero):
        self.__sex = genero

    def asignarServicio(self, servicio):
        self.__area = servicio

class Sistema:

    def __init__(self):
        self.__registro = []

    def ingresarPaciente(self):

        print("registro de paciente")

        dato_nombre = input("Digite el nombre: ")
        dato_cedula = int(input("Digite la cédula: "))
        dato_genero = input("Digite el género: ")
        dato_servicio = input("Digite el servicio: ")

        nuevo = Paciente()

        nuevo.asignarNombre(dato_nombre)
        nuevo.asignarCedula(dato_cedula)
        nuevo.asignarGenero(dato_genero)
        nuevo.asignarServicio(dato_servicio)

        self.__registro.append(nuevo)

        print("Paciente guardado correctamente ")


    def verDatosPaciente(self):

        print("consultar paciente")

        buscar_id = int(input("Ingrese la cédula a buscar: "))

        for persona in self.__registro:
            if persona.verCedula() == buscar_id:

                print("\nPaciente encontrado:")
                print("Nombre:", persona.verNombre())
                print("Cédula:", persona.verCedula())
                print("Género:", persona.verGenero())
                print("Servicio:", persona.verServicio())
                return

        print("No existe un paciente con esa cédula ")


    def verNumeroPacientes(self):

        total = len(self.__registro)
        print("\nNúmero total de pacientes:", total)

app = Sistema()

while True:

    print("MENÚ")
    print("1. Ingresar paciente nuevo")
    print("2. Ver datos de paciente")
    print("3. Ver número de pacientes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        app.ingresarPaciente()

    elif opcion == "2":
        app.verDatosPaciente()

    elif opcion == "3":
        app.verNumeroPacientes()

    else:
        print("Opción inválida, intente nuevamente")