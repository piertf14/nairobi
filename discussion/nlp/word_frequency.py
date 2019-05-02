palabras = []
bd_palabras = []
frecuencia = []

base_datos_aprobados = ["excelente curso aprendi mucho",
                        "este curso es demasiado bueno",
                        "felicitaciones y gracias por el curso",
                        "estuvo bueno el curso",
                        "un exelente curso consejos que no tienen precio",
                        "estoy encantada de realizar este breve pero intenso curso con el que estoy aprendiendo mucho",
                        "dar gracias por este gran curso",
                        "exelente curso tiene muy buenas tecnicas sobre retoque fotografico me encanto",
                        "sinceramente este curso me encanto gracias",
                        "excelente mi llave gracias",
                        "el curso en general me esta gustando mucho y me esta siendo muy util",
                        "a pesar de que trabajo con el programa regularmente, estoy aprendiendo muchas cosas nuevas que poder aplicar en mi trabajo",
                        "excelente curso gracias Daniel por compartir tu experiencia",
                        "esperaba tanto un curso como este lo adquiri sin pensarlo dos veces",
                        "super emocionada de aprender este nuevo curso y compartir mi proyecto final",
                        "excelente tutorial el contenido entregado fue muy nutritivo para mi cerebro"
                        ]


base_datos_desaprobados = ["no me deja utilizar el mental ray",
                           "sale en negro y sin audio",
                           "no puedo mover la imagen",
                           "en el video de estructura basica 1 creo que hay un error",
                           "no me carga el modulo",
                           "el audio muy bajo",
                           "archivo adjunto no abre",
                           "el video no tiene audio explicativo",
                           "este curso esta incompleto  faltan unos temas",
                           "mucha teoria me desanima el curso",
                           "no hay recursos faltan overlays",
                           "muestran plataformas que nos pueden ayudar en nuestro trabajo pero no dan un pdf que se pueda descargar",
                           "en el módulo 5 se repiten los videos",
                           "cada explicación deberia tener ejemplos o imágenes",
                           "en el módulo 3 no se ve la parte 2",
                           "no puedo bajar los adjuntos",
                           "el vídeo 21 globos texto y efectos esta cortado",
                           "como descargo los archivos adjuntos en el curso",
                           "como se corresponden los archivos de video con los de audio",
                           "el curso muy malo no enseña nada solo dice esta herramienta sirve para esto y se pone a jugar con las cosas",
                           "quisiera saber si existe algun inconveniente con la plataforma ya que llevo varios días sin poder subir mi proyecto",
                           "no me aparece la barra de menus",
                           "subi mi proyecto y aún no tengo la valoración del instructor",
                           "me hubiera encantado encontrar en los adjuntos  las definiciones de las técnicas y herramientas y no solo la bibliografía",
                           "seria bueno poner en el titulo del curso que en realidad no es desde cero",
                           "Revisen mi proyecto para que me den el feedback",
                           "no puedo utilizar los presets que me enviaron",
                           "no abre la paleta de colores no se si es que no es compatible he hecho todo el proceso y nada",
                           "tengo un problema con las selecciones no me deja seleccionar una de las coordenadas",
                           "he descargado los archivos adjuntos pero no los puedo abrir",
                           "hice mi ilustracion pero la plataforma no me deja subirlo se queda cargando",
                           "es un enrededo la explicacion sobre los tipos de concordancia deben hacerlo mas consiso",
                           "al intentar descargar los ficheros adjuntos me muestra una pagina con codigo HTML y me da un error",
                           "malisimo el audio",
                           ]

positivas = open('palabras_positivas/positivas.txt', 'r')
mensaje1 = positivas.read()
positivas.close()

negativas = open('palabras_negativas/negativas.txt', 'r')
mensaje2 = negativas.read()
negativas.close()

bd_pos = mensaje1.split(",")
bd_neg = mensaje2.split(",")

print(bd_neg)
print(bd_pos)
