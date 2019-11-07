print("###############################################################CREACION...1-10 ")
#creacion
d=dict()
d1=dict()
d2={}
d3={}
d4=dict(y=80)
d5={1:"terricola",2:"mundo",3:"perdido"}
d6={"c":"plan a","a":"original","w":"salir de inmediato"}
d7=dict({"hola":"peruano"})
d8=dict({1:"preguntar"})
p=["estrella","planeta"]
q=[1,2,3,6]
print(p,q)
d9=dict(zip(p,q))
print(d,d1,d2,d3,d4,d5,d6,d7,d8,d9)
print("###############################################################PERTENENCIA...2 ")
#pertenencia
print("#####################2.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
diccionario1={1:"pago",2:"salir",3:"lanzar",123:"parada"}
print(diccionario,diccionario1)

print("#####################2.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)

print("#####################2.3")
vuelo={4:"trujillo",58:"lima"}
nombre={4:"luis",58:"carlos"}
print(vuelo,nombre)

print("#####################2.4")
nota={"erica":00,"pedro":12,"carlos":14}
cursos={"mate":4,"algebra":4,"analisis":3}
print(nota,cursos)

print("#####################2.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
lugar={1:"cutervo",2:"chota"}
print(cuentas,lugar)

print("#####################2.6")
ms={12:"hola",25:"venir ya"}
hora={1:"almorzar",12:"dormir"}
print(ms,hora)

print("#####################2.7")
errores={123:"lista1",2:"lista13"}
calificacion={15:"andres",13:"tocas"}
print(errores,calificacion)

print("#####################2.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
edad={20:"jose",23:"jorge",18:"pedro"}
print(canciones,edad)

print("#####################2.9")
alumnos={145:"eduardo",589:"marcos"}
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(alumnos,profesor)

print("#####################2.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
conocidos=dict(einer=0)
print(candidatos,conocidos)

print("###############################################################COMPARACION...3 ")
#COMPARACION
print("#####################3.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
diccionario1={1:"pago",2:"salir",3:"lanzar",123:"parada"}
print(diccionario,diccionario1)
print(diccionario==diccionario1)

print("#####################3.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)
print(saludo==saludo)

print("#####################3.3")
vuelo={4:"trujillo",58:"lima"}
nombre={4:"luis",58:"carlos"}
print(vuelo,nombre)
print(vuelo!=nombre)

print("#####################3.4")
nota={"erica":00,"pedro":12,"carlos":14}
cursos={"mate":4,"algebra":4,"analisis":3}
print(nota,cursos)
print(nota==cursos)

print("#####################3.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
lugar={1:"cutervo",2:"chota"}
print(cuentas,lugar)
print(cuentas!=lugar)

print("#####################3.6")
ms={12:"hola",25:"venir ya"}
hora={1:"almorzar",12:"dormir"}
print(ms,hora)
print(ms!=hora)

print("#####################3.7")
errores={123:"lista1",2:"lista13"}
calificacion={15:"andres",13:"tocas"}
print(errores,calificacion)
print(errores==calificacion)

print("#####################3.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
edad={20:"jose",23:"jorge",18:"pedro"}
print(canciones,edad)
print(candidatos==edad)

print("#####################3.9")
alumnos={145:"eduardo",589:"marcos"}
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(alumnos,profesor)
print(alumnos==profesor)

print("#####################3.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
conocidos=dict(einer=0)
print(candidatos,conocidos)
print(candidatos!=conocidos)


print("############################################################### INDEXACION...5 ")
#INDEXACION
print("#####################5.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
diccionario1={1:"pago",2:"salir",3:"lanzar",123:"parada"}
print(diccionario,diccionario1)
print(diccionario["mundo"])
print(diccionario1[3])

print("#####################5.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)
print(saludo[1])

print("#####################5.3")
vuelo={4:"trujillo",58:"lima"}
nombre={4:"luis",58:"carlos"}
print(vuelo,nombre)
print(vuelo[4])
print(nombre[58])

print("#####################5.4")
nota={"erica":00,"pedro":12,"carlos":14}
cursos={"mate":4,"algebra":4,"analisis":3}
print(nota,cursos)
print(nota["erica"])
print(cursos["mate"])

print("#####################5.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
print(cuentas["marco"])

print("#####################5.6")
ms={12:"hola",25:"venir ya"}
hora={1:"almorzar",12:"dormir"}
print(ms,hora)
print(ms[12])
print(hora[12])

print("#####################5.7")
errores={123:"lista1",2:"lista13"}
calificacion={15:"andres",13:"tocas"}
print(errores,calificacion)
print(errores[123])
print(calificacion[15])

print("#####################5.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
edad={20:"jose",23:"jorge",18:"pedro"}
print(canciones,edad)
print(canciones[389])
print(edad[23])

print("#####################5.9")
alumnos={145:"eduardo",589:"marcos"}
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(alumnos,profesor)
print(alumnos[589])
print(profesor["ingles"])

print("#####################5.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos,conocidos)
print(candidatos[8])


print("############################################################### LONGITUD...7 ")
#LONGITUD
print("#####################7.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
diccionario1={1:"pago",2:"salir",3:"lanzar",123:"parada"}
print(diccionario,diccionario1)
print(len(diccionario))
print(len(diccionario1[3]))

print("#####################7.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)
print(len(saludo))

print("#####################7.3")
vuelo={4:"trujillo",58:"lima"}
nombre={4:"luis",58:"carlos"}
print(vuelo,nombre)
print(len(vuelo))
print(len(nombre))

print("#####################7.4")
nota={"erica":00,"pedro":12,"carlos":14}
cursos={"mate":4,"algebra":4,"analisis":3}
print(nota,cursos)
print(len(nota))
print(len(cursos))

print("#####################7.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
print(len(cuentas))

print("#####################7.6")
ms={12:"hola",25:"venir ya"}
hora={1:"almorzar",12:"dormir"}
print(ms,hora)
print(len(ms))
print(len(hora))

print("#####################7.7")
errores={123:"lista1",2:"lista13"}
calificacion={15:"andres",13:"tocas"}
print(errores,calificacion)
print(len(errores))
print(len(calificacion))

print("#####################7.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
edad={20:"jose",23:"jorge",18:"pedro"}
print(canciones,edad)
print(len(canciones))
print(len(edad))

print("#####################7.9")
alumnos={145:"eduardo",589:"marcos"}
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(alumnos,profesor)
print(len(alumnos))
print(len(profesor))

print("#####################7.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos,conocidos)
print(len(candidatos))


print("############################################################### LONGITUD...7 ")
#LONGITUD
print("#####################7.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
diccionario1={1:"pago",2:"salir",3:"lanzar",123:"parada"}
print(diccionario,diccionario1)
print(len(diccionario))
print(len(diccionario1[3]))

print("#####################7.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)
print(len(saludo))

print("#####################7.3")
vuelo={4:"trujillo",58:"lima"}
nombre={4:"luis",58:"carlos"}
print(vuelo,nombre)
print(len(vuelo))
print(len(nombre))

print("#####################7.4")
nota={"erica":00,"pedro":12,"carlos":14}
cursos={"mate":4,"algebra":4,"analisis":3}
print(nota,cursos)
print(len(nota))
print(len(cursos))

print("#####################7.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
print(len(cuentas))

print("#####################7.6")
ms={12:"hola",25:"venir ya"}
hora={1:"almorzar",12:"dormir"}
print(ms,hora)
print(len(ms))
print(len(hora))

print("#####################7.7")
errores={123:"lista1",2:"lista13"}
calificacion={15:"andres",13:"tocas"}
print(errores,calificacion)
print(len(errores))
print(len(calificacion))

print("#####################7.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
edad={20:"jose",23:"jorge",18:"pedro"}
print(canciones,edad)
print(len(canciones))
print(len(edad))

print("#####################7.9")
alumnos={145:"eduardo",589:"marcos"}
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(alumnos,profesor)
print(len(alumnos))
print(len(profesor))

print("#####################7.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
print(len(candidatos))


print("############################################################### ITERACION...8 ")
#ITERACION
print("#####################8.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}

print(diccionario,diccionario1)
for key in diccionario:
    print(diccionario[key])

print("#####################8.2")
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo)
for key in saludo:
    print(saludo[key])

print("#####################8.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
for k in nombre:
    print(nombre[k])

print("#####################8.4")
nota={"erica":00,"pedro":12,"carlos":14}
cursos={"mate":4,"algebra":4,"analisis":3}
print(nota,cursos)
for i in cursos:
    print(cursos[i])
for k in nota:
    print(nota[k])

print("#####################8.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
for key,value in cuentas.items():
 print(key,value)

print("#####################8.6")
ms={12:"hola",25:"venir ya"}
print(ms)
for k,v in ms.items():
    print(k,v)


print("#####################8.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
for k,v in calificacion.items():
    print(k,v)

print("#####################8.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
for k,v in canciones.items():
    print(k,v)

print("#####################8.9")
alumnos={145:"eduardo",589:"marcos"}
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(alumnos,profesor)
for k,v in profesor.items():
    print(k,v)
for i in alumnos:
    print(alumnos[i])

print("#####################8.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos,conocidos)
for y in candidatos:
    print(candidatos[y])


print("###############################################################BUSQUEDA...9 ")
#BUSQUEDA
print("#####################9.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
print(diccionario.get(616))


print("#####################9.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)
print(saludo.get(2))

print("#####################9.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
print(nombre.get(4))

print("#####################9.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
print(cursos.get("mate"))

print("#####################9.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
print(cuentas.get("marco"))

print("#####################9.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
print(hora.get(12))

print("#####################9.7")
calificacion={15:"andres",13:"tocas"}
print(errores,calificacion)
print(calificacion.get(15))

print("#####################9.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
print(canciones.get(389))


print("#####################9.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
print(profesor.get("analisis"))

print("#####################9.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
print(candidatos.get(17))

print("###############################################################ELIMINACION...13")
#ELIMINACION
print("#####################13.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
del diccionario


print("#####################13.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)
del saludo

print("#####################13.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
del nombre

print("#####################13.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
del cursos

print("#####################13.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
del cuentas

print("#####################13.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
del hora

print("#####################13.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
del calificacion

print("#####################13.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
del canciones


print("#####################13.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
del profesor

print("#####################13.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
del candidatos


print("###############################################################BUSQUEDA...14 ")
#BUSQUEDA
print("#####################14.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
diccionario["hola peru"]=6
print(diccionario)


print("#####################14.2")
saludo={2:"buenos dias",1:"buenos dias"}

print(saludo)
saludo[67]="buenas noches"
print(saludo)

print("#####################14.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
nombre[55]="juliana"
print(nombre)

print("#####################14.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
cursos["fisica"]=3
print(cursos)

print("#####################14.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
cuentas["cesar"]=657
print(cuentas)

print("#####################14.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
hora[8]="salir"
print(hora)

print("#####################14.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
calificacion[18]="einer"
print(calificacion)

print("#####################14.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
canciones[87]="sanjuanera"
print(canciones)

print("#####################14.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
profesor["circuitos"]="llecys"
print(profesor)

print("#####################14.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
candidatos[7]="parker"
print(candidatos)

print("###############################################################AGREGADO....15 ")
#AGREGADO
print("#####################15.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
diccionario.setdefault(1,"peruanos de corazon")
print(diccionario)


print("#####################15.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)
saludo.setdefault(2,"todos saludamos")
print(saludo)

print("#####################15.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
nombre.setdefault("azul",96)
print(nombre)

print("#####################15.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
cursos.setdefault(25,"sistemas digitrales")
print(cursos)

print("#####################15.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
cuentas.setdefault("german",629)
print(cuentas)

print("#####################15.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
hora.setdefault(98,"despertar")
print(hora)

print("#####################15.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
calificacion.setdefault(16,"rosa")
print(calificacion)

print("#####################15.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
canciones.setdefault(798,"rock")
print(canciones)

print("#####################15.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
profesor.setdefault("identidad","floress")
print(profesor)

print("#####################15.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
candidatos.setdefault(15,"rubi")
print(candidatos)


print("############################################################### ANULACION...16 ")
#ANULACION
print("#####################16.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
diccionario1={1:"pago",2:"salir",3:"lanzar",123:"parada"}
print(diccionario,diccionario1)
diccionario.clear()
diccionario1.clear()
print(diccionario)
print(diccionario1)

print("#####################16.2")
saludo={2:"buenos dias",1:"buenos dias"}
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo,saludo)
saludo.clear()
print(saludo)

print("#####################16.3")
vuelo={4:"trujillo",58:"lima"}
nombre={4:"luis",58:"carlos"}
print(vuelo,nombre)
vuelo.clear()
nombre .clear()
print(vuelo)
print(nombre)

print("#####################16.4")
nota={"erica":00,"pedro":12,"carlos":14}
cursos={"mate":4,"algebra":4,"analisis":3}
print(nota,cursos)
nota.clear()
cursos.clear()
print(nota)
print(cursos)

print("#####################16.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
cuentas.clear()
print(cuentas)

print("#####################16.6")
ms={12:"hola",25:"venir ya"}
hora={1:"almorzar",12:"dormir"}
print(ms,hora)
ms.clear()
hora.clear()
print(ms)
print(hora)

print("#####################16.7")
errores={123:"lista1",2:"lista13"}
calificacion={15:"andres",13:"tocas"}
print(errores,calificacion)
errores.clear()
calificacion.clear()
print(errores)
print(calificacion)

print("#####################16.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
edad={20:"jose",23:"jorge",18:"pedro"}
print(canciones,edad)
canciones.clear()
edad.clear()
print(canciones)
print(edad)

print("#####################16.9")
alumnos={145:"eduardo",589:"marcos"}
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(alumnos,profesor)
alumnos.clear()
profesor.clear()
print(alumnos)
print(profesor)

print("#####################16.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
candidatos.clear()
print(candidatos)

print("###########################################################clonado...17")

##############
print("#############17.1")
utiles1={128:"goma",111:"tijera",77:"folder"}
x=utiles1.copy()
print(utiles1)
print(x)


print("#############17.2")
vegetales={"a":"lechuga","b":"rabanito","c":"coliflor"}
y=vegetales.copy()
print(vegetales)
print(y)

print("###############17.3")
galletas={"rojo":"soda","amarillo":"vainilla","chocolate":"rellenita"}
rico=galletas.copy()
print(galletas)
print(rico)

print("###############17.4")
frutas={"p":"piña","f":"fresa","per":"pera","n":"naranja"}
i=frutas.copy()
print(frutas)
print(i)

print("###############17.5")
region={"2300msnm":"quechua",1523:"yunga",478:"chala"}
o=region.copy()
print(region)
print(o)

print("###############17.6")
listasss={1:"atender","ganar":"dos",33:"oro"}
i=listasss.copy()
print(listasss)
print(i)

print("###############17.7")
li={1111:"hola",22:"llegas temprano",3:"tarde",4:"no deviste venir"}
y=li.copy()
print(li)
print(y)


print("###############17.8")
prom={15:"yeri",19:"jose",12:"jan",18:"einer 2",16:"inga"}
promedio= prom.copy()
print(prom)
print(promedio)

print("###############17.9")
numeros={145:25,12:25,56:48,89:96,10:387,20:6972}
i=numeros.copy()



print(numeros)
print(i)

print("###############17.10")
lisa={"r":"roolo","e":"elefante","w":"wuilder","u":"vaca"}
t=lisa.copy()
print(lisa)
print(t)

print("###############################################################INSERCION...19 ")
#INSERCION
print("#####################19.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
diccionario["hola peru"]=6
print(diccionario)


print("#####################19.2")
saludo={2:"buenos dias",1:"buenos dias"}

print(saludo)
saludo[67]="hasta pronto"
print(saludo)

print("#####################19.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
nombre[55]="yulissa"
print(nombre)

print("#####################19.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
cursos["fisica"]=6
print(cursos)

print("#####################19.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
cuentas["cesar"]=8967
print(cuentas)

print("#####################19.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
hora[8]="correr"
print(hora)

print("#####################19.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
calificacion[18]="julian"
print(calificacion)

print("#####################19.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
canciones[87]="baladas"
print(canciones)

print("#####################19.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
profesor["circuitos"]="gastulo"
print(profesor)

print("#####################19.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
candidatos[7]="herrera"
print(candidatos)


print("###############################################################EXTRACCION...20 ")
#EXTRACCION
print("#####################20.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
x=diccionario.pop("mundo")
print(diccionario)
print(x)


print("#####################20.2")
saludo={2:"buenos dias",1:"buenos dias"}

print(saludo)
x=saludo.pop(2)
print(saludo)
print(x)
print("#####################20.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
x=nombre.pop(4)
print(nombre)
print(x)

print("#####################20.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
x=cursos.pop("mate")
print(cursos)
print(x)

print("#####################20.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
x=cuentas.pop("marco")
print(cuentas)
print(x)

print("#####################20.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
x=hora.pop(1)
print(hora)
print(x)

print("#####################20.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
x=calificacion.pop(13)
print(calificacion)
print(x)

print("#####################20.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
x=canciones.pop(59)
print(canciones)
print(x)

print("#####################20.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
x=profesor.pop("ingles")
print(profesor)
print(x)

print("#####################20.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
x=candidatos.pop(8)
print(candidatos)
print(x)


print("###############################################################VER CLAVES...24 ")
#VER CLAVES
print("#####################24.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
print(diccionario.keys())


print("#####################24.2")
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo)
print(saludo.keys())

print("#####################24.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
print(nombre.keys())

print("#####################24.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
print(cursos.keys())

print("#####################24.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
print(cuentas.keys())

print("#####################24.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
print(hora.keys())

print("#####################24.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
print(calificacion.keys())

print("#####################24.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
print(canciones.keys())

print("#####################24.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
print(profesor.keys())

print("#####################24.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
print(candidatos.keys())


print("###############################################################VER CLAVES...25 ")
#VER CLAVES
print("#####################25.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
print(diccionario.values())


print("#####################25.2")
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo)
print(saludo.values())

print("#####################25.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
print(nombre.values())

print("#####################25.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
print(cursos.values())

print("#####################25.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
print(cuentas.values())

print("#####################25.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
print(hora.values())

print("#####################25.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
print(calificacion.values())

print("#####################25.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
print(canciones.values())

print("#####################25.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
print(profesor.values())

print("#####################25.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
print(candidatos.values())


print("###############################################################VER CONVERSION...26 ")
#CONVERSION
print("#####################26.1")
diccionario={"mundo":"terricolas",123:"parada",616:"horda"}
print(diccionario)
l=list(diccionario)
print(diccionario)
print(l)

print("#####################26.2")
saludo={2:"buenos dias",1:"buenos dias"}
print(saludo)
l=list(saludo)
print(saludo)
print(l)

print("#####################26.3")
nombre={4:"luis",58:"carlos"}
print(nombre)
t=tuple(nombre)
print(nombre)
print(t)

print("#####################26.4")
cursos={"mate":4,"algebra":4,"analisis":3}
print(cursos)
t=tuple(cuentas)
print(cursos)
print(t)

print("#####################26.5")
cuentas={"marco":25,"alonso":869,"alfredo":570}
print(cuentas)
s=set(cuentas)
print(cuentas)
print(s)

print("#####################26.6")
hora={1:"almorzar",12:"dormir"}
print(hora)
s=set(hora)
print(hora)
print(s)

print("#####################26.7")
calificacion={15:"andres",13:"tocas"}
print(calificacion)
l=list(calificacion.values())
print(calificacion)
print(l)

print("#####################26.8")
canciones={8:"guayno",59:"regueton",389:"tomorrowland"}
print(canciones)
t=tuple(canciones.values())
print(canciones)
print(t)

print("#####################26.9")
profesor={"ingles":"clarita","mate":"alejandra","analisis":"doris"}
print(profesor)
s=set(profesor.values())
print(profesor)
print(s)

print("#####################26.10")
candidatos={8:"toledo",17:"maria",61:"maria"}
print(candidatos)
t=tuple(candidatos.values())
print(candidatos)
print(t)



