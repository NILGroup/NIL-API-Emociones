def sustituir(palabra,acento,letra):
	pos = palabra.index(acento)
	pre = palabra[:pos]
	suf = palabra[pos+1:]
	sin_acento = pre+letra+suf
	return sin_acento

def traducir(palabra):
	if 'á' in palabra:
		palabra = sustituir(palabra,'á', "a")
	elif 'é' in palabra:
		palabra = sustituir(palabra,'é', "e")
	elif 'í' in palabra:
		palabra = sustituir(palabra,'í', "i")
	elif 'ó' in palabra:
		palabra = sustituir(palabra,'ó', "o")
	elif 'ú' in palabra:
		palabra = sustituir(palabra,'ú', "u")
	if 'ñ' in palabra:
		palabra = sustituir(palabra,'ñ', "ny")	
	return palabra