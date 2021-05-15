#Este programa es el pequeño uso de una librearia para traducir un Texto a español, básicamente lo use para traducir un archivo que es la descripción de un video de youtube.
import os.path
from deep_translator import GoogleTranslator


#En la variable Path escribir la ruta completa de donde se encuentra el archivo.

# La variable File tiene dos parametros, si queremos sobreescribir el archivo traduccion debemos poner A si queremos eliminarlo y escribir la nueva traduccion usaremos W.

path = r'C:\Users\User\text_to_translate.txt'
def translate_file(path):
    if os.path.isfile(path):
        translater = GoogleTranslator(source='en', target='es').translate_file(path)
        print(translater)
        file = open("traduccion.txt", "w")
        file.write(translater)
    else:
        print("Save the file in folder")

translate_file(path)

