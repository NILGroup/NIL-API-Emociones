import Stemmer

stemmer = Stemmer.Stemmer('spanish')

lemas_repetidos = ['abandon', 'abej', 'abog', 'abraz', 'abuel', 'acogedor', 'acos', 'admir', 'ador', 'afect', 
'agres', 'ahog', 'alambr', 'alarm', 'alegr', 'alicat', 'amenaz', 'amig', 'amist', 'angusti', 'aplast', 'aplaus', 'aprob', 
'asesin', 'asesor', 'asfixi', 'asombr', 'asust', 'aterroriz', 'atrac', 'auxili', 'avisp', 'ayud', 'bailarin', 'beb', 
'bes', 'bot', 'brutal', 'call', 'calm', 'camarer', 'candidat', 'caprich', 'cariñ', 'carter', 'casc', 'castig', 'cazador',
'celador', 'celebr', 'cel', 'chantaj', 'chic', 'cientif', 'coaccion', 'codici', 'color', 'complac', 'compositor', 
'conden', 'conoc', 'consol', 'contamin', 'content', 'coquet', 'corredor', 'cost', 'creativ', 'cuadr', 'curander', 
'decor', 'defend', 'delincuent', 'deport', 'desafi', 'desahuci', 'descans', 'despach', 'despreci', 'dificult', 'dinam', 
'dios', 'director', 'diseñ', 'disgust', 'disminu', 'divert', 'divorci', 'doctor', 'drogadict', 'dud', 'educ', 'efect', 
'ejecut', 'ejempl', 'eleg', 'embaraz', 'emple', 'empresari', 'enamor', 'encant', 'energ', 'enfad', 'enfermer', 
'enfurec', 'engañ', 'enterr', 'entusiasm', 'escritor', 'escultor', 'espant', 'espos', 'estacion', 
'estaf', 'estall', 'estil', 'estimul', 'estudi', 'excit', 'explot', 'famos', 'fascin', 'figur', 'foc', 
'fotograf', 'fracas', 'fusil', 'ganador', 'gener', 'genial', 'golp', 'gradu', 'guant', 'guap', 'habit', 
'her', 'herman', 'hij', 'horror', 'human', 'humild', 'humill', 'ideal', 'igual', 'ilusion', 'imagin', 
'impotent', 'incendi', 'inferior', 'informat', 'ingres', 'injuri', 'inquiet', 'insegur', 'inspir', 'insult', 
'investig', 'invit', 'irrit', 'jubil', 'jug', 'ladron', 'lament', 'lanz', 'lat', 'lecher', 'lesion', 'liber', 
'licenci', 'lig', 'list', 'llam', 'logr', 'lumin', 'lun', 'maestr', 'maltrat', 'mang', 
'maravill', 'marc', 'masaj', 'masturb', 'mat', 'mecan', 'mes', 'millonari', 'mim', 'ministr', 'monj', 
'muert', 'muñec', 'mutil', 'music', 'nadador', 'niet', 'niñ', 'noved', 'novi', 'odi', 'olvid', 'orden', 
'orgull', 'panader', 'pas', 'paus', 'pec', 'pein', 'peligr', 'peluquer', 'perfum', 'period', 'pes', 
'pesim', 'pintor', 'pioj', 'pirop', 'premi', 'preocup', 'prepar', 'present', 'profesor', 'program', 
'prosper', 'proteg', 'public', 'puert', 'puñal', 'quer', 'rechaz', 'recompens', 'recuerd', 'refugi', 
'regal', 'rein', 'relaj', 'repugn', 'rescat', 'respet', 'respir', 'revolv', 'rival', 'rotul', 'salt', 
'salud', 'sangr', 'secretari', 'secuestr', 'sed', 'segur', 'soborn', 'socorr', 'sol', 'sorprend', 
'sospech', 'susurr', 'tall', 'tem', 'terror', 'tiran', 'toler', 'tont', 'torc', 'torment', 'tortur', 
'trabaj', 'traicion', 'tranquil', 'triunf', 'vel', 'venc', 'version', 'veterinari', 'victori', 'viud', 'viv',
 'voluptu']

derivadas = ['abandonado', 'abejas', 'abogada', 'abrazar', 'abuela', 'acogedora', 'acosar', 'admirar', 
'adorable', 'afectar', 'agresividad', 'ahogarse', 'alambrada', 'alarmar', 'alegre', 'alicatar', 'amenazado', 'amigable',
'amistoso', 'angustiado', 'aplastado', 'aplausos', 'aprobación', 'asesina', 'asesora', 'asfixiarse', 'asombrado', 
'asustado', 'aterrorizado', 'atracador', 'auxiliar', 'avispado', 'ayuda', 'bailarina', 
'bebida', 'besar', 'bota', 'brutalidad', 'callado', 'calmado', 'camarera', 'candidata', 'caprichoso', 'cariñoso', 
'carterista','cascada', 'castigar', 'cazadora', 'celadora', 'celebración', 'celos', 'chantajista', 'chica', 'científica', 
'coaccionar','codicioso', 'colorado', 'complacido', 'compositora', 'condenado', 'conocimiento', 'consolado', 'contaminación',
'contentar', 'coquetear', 'corredora', 'costa', 'creatividad', 'cuadro', 'curandera', 'decorar', 'defendido',
'delincuencia', 'deportes', 'desafiar', 'desahuciar', 'descansar', 'despachar', 'despreciar', 'dificultad',
'dinámica', 'diosa', 'directora', 'diseñador', 'disgustado', 'disminuido', 'divertido', 'divorciado', 
'doctora', 'drogadicta', 'dudar', 'educador', 'efectivo', 'ejecutivo', 'ejemplar', 'elegante', 
'embarazada', 'emplear', 'empresaria', 'enamorado', 'encantar', 'enérgico', 'enfadado', 
'enfermera', 'enfurecido', 'engañar', 'enterrador', 'entusiasmar', 'escritora', 'escultora', 
'espantar', 'esposa', 'estacionar', 'estafa', 'estallar', 'estilista', 'estimulación', 'estudiar', 'excitado', 
'explotación', 'famosa', 'fascinación', 'figurar', 'foca', 'fotógrafo', 'fracasado', 
'fusil', 'ganador', 'generador', 'genial', 'golpe', 'graduada', 'guante', 'guapa', 'habitación', 'herido', 
'hermana', 'hija', 'horror', 'humanidad', 'humildad', 'humillación', 'ideal', 'igual', 'ilusionar', 
'imaginación', 'impotencia', 'incendiar', 'inferior', 'informática', 'ingresar', 'injuria', 'inquietar', 'inseguridad', 
'inspirado', 'insultado', 'investigador', 'invitación', 'irritación', 'jubilado', 'jugar', 'ladrona', 
'lamentar', 'lanza', 'lata', 'lechera', 'lesionar', 'liberación', 'licenciada', 'liga', 'lista', 
'llamada', 'lograr', 'luminosidad', 'lunar', 'maestra', 'maltratar', 'manga', 'maravilla', 
'marcar', 'masaje', 'masturbación', 'matar', 'mecanismo', 'mes', 'millonaria', 'mimado', 
'ministra', 'monja', 'muerte', 'muñeca', 'mutilación', 'música', 'nadador', 'nieta', 'niña', 'novedad', 
'novia', 'odiar', 'olvidar', 'ordenado', 'orgullo', 'panadera', 'pasear', 'pausa', 'pecado', 'peinar', 'peligrar',
'peluquera', 'perfumado', 'periodista', 'pesado', 'pesimismo', 'pintor', 'piojo', 'piropear', 'premiar', 
'preocupación', 'preparado', 'presentador', 'profesor', 'programa', 'prosperar', 'proteger', 
'publicidad', 'puerta', 'puñal', 'querida', 'rechazado', 'recompensa', 'recuerdo', 'refugiada', 
'regalar', 'reina', 'relajación', 'repugnancia', 'rescatar', 'respetar', 'respiración', 'revolver', 
'rivalidad', 'rotulador', 'salto', 'salud', 'sangrar', 'secretaria', 'secuestrador', 'sed', 
'seguridad', 'sobornar', 'socorrer', 'sol', 'sorprender', 'sospecha', 'susurrar', 'talla', 'temer', 'terrorismo', 
'tiranía', 'tolerancia', 'tontería', 'torcer', 'tormenta', 'tortura', 'trabajador', 
'traicionar', 'tranquilidad', 'triunfar', 'vela', 'vencer', 'versionar', 'veterinaria', 'victoria', 'viuda', 
'vivir', 'voluptuosidad']

opciones = ['abandono', 'abeja', 'abogado', 'abrazo', 'abuelo', 'acogedor', 'acoso', 'admiración', 
'adoración', 'afecto', 'agresivo', 'ahogar', 'alambre', 'alarma', 'alegría', 'alicates', 
'amenaza', 'amigo', 'amistad', 'angustia', 'aplastar', 'aplauso', 'aprobar', 'asesinar', 'asesor', 'asfixiar', 
'asombrar', 'asustar', 'aterrorizar', 'atracar', 'auxilio', 'avispa', 'ayudar', 'bailarín', 'bebé', 'beso', 
'bote', 'brutal', 'calle', 'calma', 'camarero', 'candidato', 'capricho', 'cariño', 'cartera', 'casco', 'castigo', 
'cazador', 'celador', 'celebrar', 'celo', 'chantaje', 'chico', 'científico', 'coacción', 'codicia', 'color', 'complacer',
'compositor', 'condena', 'conocer', 'consolador', 'contaminar', 'contento', 'coqueto', 'corredor', 'costo', 'creativo', 
'cuadrado', 'curandero', 'decoro', 'defender', 'delincuente', 'deportista', 'desafío', 'desahucio', 'descanso', 
'despacho', 'desprecio', 'dificultar', 'dinámico', 'dios', 'director', 'diseño', 'disgusto', 
'disminución', 'divertir', 'divorcio', 'doctor', 'drogadicto', 'duda', 'educación', 'efecto', 
'ejecutar', 'ejemplo', 'elegir', 'embarazo', 'empleo', 'empresario', 'enamorar', 'encanto', 'energía', 
'enfadar', 'enfermero', 'enfurecer', 'engaño', 'enterrar', 'entusiasmo', 'escritor', 'escultor', 'espantoso', 'esposo', 
'estación', 'estafador', 'estallido', 'estilo', 
'estímulo', 'estudioso', 'excitar', 'explotador', 'famoso', 'fascinante', 'figura', 'foco', 
'fotografía', 'fracaso', 'fusilar', 'ganadora', 'generoso', 'genialidad', 'golpear', 'graduado', 
'guantes', 'guapo', 'habitante', 'herir', 'hermano', 'hijo', 'horroroso', 'humanismo', 'humilde', 'humillar', 
'idealismo', 'igualar', 'ilusión', 'imaginar', 'impotente', 'incendio', 'inferioridad', 'informático', 
'ingreso', 'injuriar', 'inquieto', 'inseguro', 'inspirar', 'insulto', 'investigadora', 'invitada', 'irritar',
'jubiloso', 'jugo', 'ladrón', 'lamento', 'lanzar', 'latido', 'lechero', 'lesión', 'liberar', 
'licenciado', 'ligar', 'listo', 'llama', 'logro', 'luminoso', 'luna', 'maestro', 
'maltrato', 'mango', 'maravilloso', 'marco', 'masajista', 'masturbarse', 'mate', 'mecánica',
'mesa', 'millonario', 'mimo', 'ministro', 'monje', 'muerto', 'muñeco', 'mutilar', 'músico', 'nadadora', 
'nieto', 'niño', 'novedoso', 'novio', 'odio', 'olvido', 'ordenador', 'orgulloso', 'panadero', 'pase', 'pausado', 
'peca', 'peine', 'peligro', 'peluquero', 'perfume', 'periódico', 'pesar', 'pesimista', 
'pintora', 'piojos', 'piropo', 'premio', 'preocupar', 'preparar', 'presente', 'profesora', 'programar', 
'prosperidad', 'protegido', 'publicista', 'puerto', 'puñalada', 'querido', 'rechazo', 'recompensar', 
'recuerdos', 'refugiado', 'regalo', 'reinar', 'relajado', 'repugnante', 'rescate', 'respeto', 'respirar', 
'revólver', 'rival', 'rotular', 'saltear', 'saludar', 'sangre', 'secretario', 'secuestro', 'seda', 
'seguro', 'soborno', 'socorro', 'solar', 'sorprendido', 'sospechoso', 'susurro', 'talle', 'tema', 'terrorista', 'tirano',
'tolerante', 'tonto', 'torcido', 'tormento', 'torturar', 'trabajar', 'traición', 'tranquilo',
'triunfo', 'velas', 'vencido', 'versión', 'veterinario', 'victorioso', 'viudo', 'vivo', 'voluptuoso']

for i in range(len(opciones)):
	print("----------------------")
	print(opciones[i])
	lema = stemmer.stemWord(opciones[i])
	if (lema == lemas_repetidos[i]):
		print("OK")
		if stemmer.stemWord(derivadas[i]) == lemas_repetidos[i]:
			print("OK")
		else:
			print(derivadas[i])
	else:
		print(lemas_repetidos[i])
		print(derivadas[i])
	print("----------------------")