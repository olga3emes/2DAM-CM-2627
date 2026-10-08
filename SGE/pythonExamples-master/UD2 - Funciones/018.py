#Funciones de orden superior
def saludar(lang):
    def saludar_es():
        print ("Hola")
    def saludar_en():
        print ("Hello" )
    def saludar_fr():
        print ("Salut")
    lang_func ={"es":saludar_es,
    "en":saludar_en,
    "fr":saludar_fr}
    return lang_func[lang]

f = saludar("es")
f()  # Llama a la función de saludo en español
f = saludar("en")
f()  # Llama a la función de saludo en inglés
f = saludar("fr")
f()  # Llama a la función de saludo en francés

