# servidor.py

from pysimplesoap.server import SoapDispatcher, SOAPHandler
from http.server import HTTPServer

# Crear el dispatcher SOAP
dispatcher = SoapDispatcher(
    name="Calculadora",
    location="http://localhost:8000/",
    action='http://localhost:8000/',  # SOAPAction
    namespace="http://example.com/calculadora/",
    prefix="ns0",
    trace=True,
    ns=True
)

# Definir las operaciones de la calculadora
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        # Lanzar una excepción para manejar la división por cero
        raise ValueError("Error: División por cero no está permitida.")
    return a / b

# Registrar las funciones en el dispatcher
dispatcher.register_function(
    'suma',
    suma,
    returns={'resultado': float},
    args={'a': float, 'b': float}
)

dispatcher.register_function(
    'resta',
    resta,
    returns={'resultado': float},
    args={'a': float, 'b': float}
)

dispatcher.register_function(
    'multiplicacion',
    multiplicacion,
    returns={'resultado': float},
    args={'a': float, 'b': float}
)

dispatcher.register_function(
    'division',
    division,
    returns={'resultado': float},
    args={'a': float, 'b': float}
)

# Definir el handler SOAP
class SimpleSOAPHandler(SOAPHandler):
    pass  # No es necesario asignar el dispatcher aquí

if __name__ == '__main__':
    # Crear una instancia del servidor HTTP
    server = HTTPServer(('0.0.0.0', 8000), SimpleSOAPHandler)
    
    # Asignar el dispatcher al servidor
    server.dispatcher = dispatcher

    print("Servidor SOAP de la Calculadora está corriendo en http://localhost:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        server.server_close()
