#Este programa es el pequeño uso de una librearia para traducir un Texto a español, básicamente lo use para traducir un archivo que es la descripción de un video de youtube.
from deep_translator import GoogleTranslator
path = r'C:\Users\SEBASTIAN\Desktop\DESARROLLO\Traducctor_Py\text_to_translate.txt'
translater = GoogleTranslator(source='en', target='es').translate_file(path)
print(translater)