# oficina.py

class OficinaAtencionCiudadana:
    def __init__(self):
        self.pila_documentos = []

    def agregar_documento(self, documento):
        """Agrega un nuevo documento a la pila."""
        self.pila_documentos.append(documento)
        print(f"Documento agregado: {documento}")

    def revisar_documento(self):
        """Revisa (elimina) el último documento entregado."""
        if self.pila_documentos:
            doc = self.pila_documentos.pop()
            print(f"Documento revisado y eliminado: {doc}")
        else:
            print("No hay documentos para revisar.")

    def mostrar_pendientes(self):
        """Muestra los documentos pendientes de revisión."""
        if not self.pila_documentos:
            print("No hay documentos pendientes.")
        else:
            print("Documentos pendientes (del primero al último entregado):")
            for i, doc in enumerate(self.pila_documentos, 1):
                print(f"{i}. {doc}")
