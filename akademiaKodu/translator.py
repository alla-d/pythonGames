from googletrans import Translator

translator = Translator()
result = translator.translate('Mikä on nimesi', src='fi', dest='ru')

print(result.src)
print(result.dest)
print(result.text)
