class Patient:
    def __init__(self, name, service_type):
        self.name = name
        self.service_type = service_type
    
    def __str__(self):
        return f"Paciente: {self.name}, Servicio: {self.service_type}"
# Clase para la cola de turnos
class PharmacyQueue:
    def __init__(self):
        self.queue = []
    
    def add_patient(self, patient):
        self.queue.append(patient)
        print(f"{patient.name} ha sido agregado a la cola para {patient.service_type}.")
    
    def serve_next(self):
        if self.is_empty():
            return "No hay pacientes en la cola."
        patient = self.queue.pop(0)
        return f"Atendiendo a {patient.name} para {patient.service_type}."
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def show_pending(self):
        if self.is_empty():
            return "No hay turnos pendientes."
        result = "Turnos pendientes:\n"
        for i, patient in enumerate(self.queue, 1):
            result += f"{i}. {patient}\n"
        return result
