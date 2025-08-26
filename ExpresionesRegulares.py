import re # Librería necesaria para utilizar Regex

# \w = toma caracteres como letras, números o el guión bajo _
# \s = espacios en blanco
# \b = establece un límite de palabra

regularEx_1 = r"\b\w{5}\b" # Buscar una palabra que contenga la cantidad de caracteres especificada.

palabra_1 = """'Cause I'm on top of the world, 'ey
I'm on top of the world, 'ey
Waiting on this for a while now
Paying my dues to the dirt
I've been waiting to smile, 'ey
Been holding it in for a while, 'ey
Take it with me if I can
Been dreaming of this since a child
I'm on top of the world
ADD: Are we in Data Structure class?"""

resultado = re.findall(regularEx_1,palabra_1) # Comando para buscar las coincidencias del patrón especificadp dentro del texto.
print(resultado)

regularEx_2 = r"\bchild\b" # Comando para extraer una palabra especifica, 'child'

resultado = re.findall(regularEx_2,palabra_1)
print(resultado)

regularEx_3 = r"\?" # Extraer carácteres especiales

resultado = re.findall(regularEx_3,palabra_1)
print(resultado)

## Se trabajó con el texto plano Don Quijote de la Mancha.
## Se añaden números de diferentes cifras para el ejercicio ya que el texto no los contiene.
texto_1 = "DON QUIJOTE DE LA MANCHA Miguel de Cervantes Saavedra PRIMERA PARTE CAPÍTULO 1: Que trata de la condición y ejercicio del famoso hidalgo D. Quijote de la Mancha En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lentejas los viernes, consumían las 3456 partes de su hacienda, que ascendía a unas 1250 fanegas. El resto della, unas 789, concluían sayo de velarte, calzas de velludo para las fiestas con sus pantuflos de lo mismo, los días de entre semana se honraba con su vellori de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años, era de complexión recia, seco de carnes, enjuto de rostro; gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de Quijada o Quesada (que en esto hay alguna diferencia en los autores que deste caso escriben), aunque por conjeturas verosímiles se deja entender que se llama Quijana; pero esto importa poco a nuestro cuento; basta que en la narración dél no se salga un punto de la verdad. Es, pues, de saber, que este sobredicho hidalgo, los ratos que estaba ocioso (que eran los más del año, unas 300 jornadas) se daba a leer libros de caballerías con tanta afición y gusto, que olvidó casi de todo punto el ejercicio de la caza, y aun la administración de su hacienda; y llegó a tanto su curiosidad y desatino en esto, que vendió muchas hanegas de tierra de sembradura, para comprar libros de caballerías en que leer; y así llevó a su casa todos cuantos pudo haber dellos, sumando un total de 18 volúmenes; y de todos, ningunos le parecían tan bien como los 24 que compuso el famoso Feliciano de Silva: porque la claridad de su prosa, y aquellas intrincadas razones suyas, le parecían de perlas; y más cuando llegaba a leer aquellos requiebros y cartas de desafío, donde en muchas partes hallaba escrito: la razón de la sinrazón que a mi razón se hace, de tal manera mi razón enflaquece, que con razón me quejo de la vuestra fermosura, y también cuando leía: los altos cielos que de vuestra divinidad divinamente con las estrellas se fortifican, y os hacen merecedora del merecimiento que merece la vuestra grandeza. Con estas y semejantes razones perdía el pobre caballero el juicio, y desvelábase por entenderlas, y desentrañarles el sentido, que no se lo sacara, ni las entendiera el mismo Aristóteles, si resucitara para sólo ello. No estaba muy bien con las heridas que don Belianis daba y recibía, que sumaban 42 en un solo capítulo, porque se imaginaba que por grandes maestros que le hubiesen curado, no dejaría de tener el rostro y todo el cuerpo lleno de cicatrices y señales; pero con todo alababa en su autor aquel acabar su libro con la promesa de aquella inacabable aventura, y muchas veces le vino deseo de tomar la pluma, y darle fin al pie de la letra como allí se promete; y sin duda alguna lo hiciera, y aun saliera con ello, si otros mayores y continuos pensamientos no se lo estorbaran. Su obsesión era tal que podía pasar 1500 horas en su biblioteca, sin apenas probar bocado."

regularEx_4 = r"\b\w{4}\b" # Extraer palabras de cuatro caracteres
resultado = re.findall(regularEx_4,texto_1)
print(resultado)

regularEx_5 = r"\d{4}" # Extraer numeros de 4 dígitos
resultado = re.findall(regularEx_5,texto_1)
print(resultado)
