# Definimos la clase Singleton llamada Configuracion
class Configuracion:
    # Atributo de clase privado que almacenará la única instancia de Configuracion
    _instancia = None

    # Método especial que controla la creación de instancias (antes de __init__)
    def __new__(cls):
        # Si aún no se ha creado la instancia...
        if cls._instancia is None:
            print("Creando nueva instancia de configuración")
            # Creamos la nueva instancia usando la clase base
            cls._instancia = super(Configuracion, cls).__new__(cls)
            # Inicializamos los atributos de configuración por única vez
            cls._instancia.idioma = "Español"
            cls._instancia.tema = "Claro"
        # Retornamos la instancia existente (nueva o ya creada)
        return cls._instancia

# Prueba del Singleton

# Creamos la primera instancia (esto activará el print y la inicialización)
config1 = Configuracion()

# Intentamos crear otra instancia (se reutiliza la misma, no se vuelve a crear)
config2 = Configuracion()

# Mostramos el valor del atributo 'idioma' desde la primera instancia
print(f"Idioma (config1): {config1.idioma}")

# Cambiamos el idioma desde la segunda "instancia"
config2.idioma = "Inglés"

# Verificamos si el cambio también afectó a la primera (debería, ya que es la misma instancia)
print(f"Idioma (config1 después de cambiar config2): {config1.idioma}")

# Comprobamos si ambas variables apuntan a la misma instancia (debería imprimir True)
print("¿config1 es config2?", config1 is config2)