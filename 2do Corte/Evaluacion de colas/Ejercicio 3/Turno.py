# Importa deque, una estructura de datos eficiente para colas
from collections import deque

# Clase que gestiona los turnos de pacientes en una farmacia
class TurnoFarmacia:
    def __init__(self):
        # Crea una cola vacía para los turnos
        self.cola_turnos = deque()

    # Método para registrar un nuevo paciente
    def registrar_paciente(self, nombre, servicio):
        # Crea un diccionario con los datos del paciente
        paciente = {"nombre": nombre, "servicio": servicio}
        # Agrega al paciente al final de la cola
        self.cola_turnos.append(paciente)
        # Muestra un mensaje de confirmación
        print(f"Paciente {nombre} registrado para {servicio}.")

    # Método para atender al siguiente paciente
    def atender_paciente(self):
        # Verifica si hay pacientes en la cola
        if not self.esta_vacia():
            # Remueve y obtiene al primer paciente en la cola
            paciente = self.cola_turnos.popleft()
            print(f"Atendiendo a {paciente['nombre']} para {paciente['servicio']}.")
        else:
            print("No hay pacientes en espera.")

    # Método para mostrar los turnos pendientes
    def mostrar_turnos_pendientes(self):
        # Verifica si hay pacientes en la cola
        if not self.esta_vacia():
            print("\nTurnos pendientes:")
            # Recorre y muestra todos los pacientes en espera
            for i, paciente in enumerate(self.cola_turnos, start=1):
                print(f"{i}. {paciente['nombre']} - {paciente['servicio']}")
        else:
            print("No hay turnos pendientes.")

    # Método auxiliar que verifica si la cola está vacía
    def esta_vacia(self):
        return len(self.cola_turnos) == 0
