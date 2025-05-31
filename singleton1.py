class Configuracion:
    
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Creando nueva instancia de configuración")
            cls._instancia = super(Configuracion, cls).__new__(cls)
            cls._instancia.idioma = "Español"
            cls._instancia.tema = "Claro"
        return cls._instancia


config1 = Configuracion()


config2 = Configuracion()

print(f"Idioma (config1): {config1.idioma}")

config2.idioma = "Inglés"

print(f"Idioma (config1 después de cambiar config2): {config1.idioma}")

print("¿config1 es config2?", config1 is config2)
