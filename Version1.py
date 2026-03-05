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
    
    def ingresarPaciente(self, paciente):
        self.__registro.append(paciente)

    def verDatosPaciente(self, cedula):
        for persona in self.__registro:
            if persona.verCedula() == cedula:
                return persona
        return None

    def verNumeroPacientes(self):

        total = len(self.__registro)
        print("\nNúmero total de pacientes:", total)

def main():

    app = Sistema()

    while True:

        print("MENÚ")
        print("1. Ingresar paciente nuevo")
        print("2. Ver datos de paciente")
        print("3. Ver número de pacientes")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("REGISTRO DE PACIENTE")
            dato_nombre = input("Digite el nombre: ")
            dato_cedula = int(input("Digite la cédula: "))
            dato_genero = input("Digite el género: ")
            dato_servicio = input("Digite el servicio: ")

            nuevo = Paciente()
            nuevo.asignarNombre(dato_nombre)
            nuevo.asignarCedula(dato_cedula)
            nuevo.asignarGenero(dato_genero)
            nuevo.asignarServicio(dato_servicio)

            app.ingresarPaciente(nuevo)
            print("Paciente guardado correctamente")
        

        elif opcion == "2":
            buscar_id = int(input("Ingrese la cédula a buscar: "))
            persona = app.verDatosPaciente(buscar_id)

            if persona is not None:
                print("\nPaciente encontrado:")
                print("Nombre:", persona.verNombre())
                print("Cédula:", persona.verCedula())
                print("Género:", persona.verGenero())
                print("Servicio:", persona.verServicio())
            else:
                print("No existe un paciente con esa cédula ")

        elif opcion == "3":
            app.verNumeroPacientes()

        else:
            print("Opción inválida, intente nuevamente")
if __name__ == "__main__":
    main()