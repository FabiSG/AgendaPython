from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller
"""Contactos = []

c1= Contacto(1,'Juan Perez', '4641661118', 'jperez@gmail.com','Av siempre viva 113')
c2= Contacto(2,'Carlos Martinez', '6473350', 'carlos.martinez@gmail.com','Cerro Azul 201')
"""
"""print(c1.nombre)
print(c1.tel)
print(c1.correo)
print(c1.dire)
print(" ")"""

#t1= cita(1,1, 'Cerveceria Chapultepec', '26/05/20','14:30','Empedar la vida')
"""print(d.id_cita)
print(d.id_contacto)
print(d.lugar)
print(d.hora)
print(d.asunto)"""
"""Contactos.append(c1)
Contactos.append(c2)

guess = input("Ingresa un nombre: ")
"""
"""
#opcion 1
for i in range(len(Contactos)):
    if guess == Contactos[i].nombre:
        print("contacto ya existe")
        break
else
    print("no esta")
"""
"""
#opcion 2
for c in Contactos:
    if guess.lower() == c.nombre.lower():
        print('Si esta')
        break
else:
    print("no esta")
"""

m = Model()
m.agregar_contacto(1,'Juan Perez', '4641661118', 'jperez@gmail.com','Av siempre viva 113')
m.agregar_contacto(2,'Carlos Martinez', '6473350', 'carlos.martinez@gmail.com','Cerro Azul 201')
m.agregar_contacto(3,'Armando Navarro', '6473350', 'carlos.martinez@gmail.com','Cerro Azul 201')


#s = m.leer_contacto(2)
#print(s.nombre)

#m.actualizar_contacto(2,n_nombre='Jose Manuel')
#s = m.leer_contacto(2)
#print(s.nombre)

#s = m.borrar_contacto(2)
#print(s)

m.agregar_cita(1,1, 'Cerveceria Chapultepec', '26/05/20','14:30','Tomar')
m.agregar_cita(2,1, 'MCarty´s', '26/05/20','14:30','Tomar')
m.agregar_cita(3,2, 'MCarty´s', '26/05/20','14:30','Tomar')

#j = m.leer_cita(1)
#print(j.asunto)

#m.actualizar_cita(2,1, 'Fabulosas Papas', '26/05/20','14:30','Empedarnos')
#j = m.leer_cita(2)
#print(j.asunto)

#s = m.borrar_cita(1)
#print(s)

#per = m.leer_contacto_letra('A')
#for i in per:
#    print(i.nombre, i.tel)


"""per = m.cita_fecha('26/05/20')
for i in per:
    print(i.lugar, i.asunto)"""

#print("original")
#for k in m.citas:
#    print(k.lugar, k.asunto)
#print("actualizado")

#s = m.borrar_contacto_cita(2)
#for k in m.citas:
#    print(k.lugar, k.asunto)

v = View()
'''CONTACTOS
s = m.leer_todos_contactos()
v.mostrar_contactos(s)
c = m.leer_contacto(1)
v.mostrar_contacto(c)

f, c = m.borrar_contacto(1)
if f:
        v.borrar_contacto(c)
else:
        v.contacto_no_existe()
v.mostrar_contactos(s)
'''
'''44
s = m.leer_todos_citas()
v.mostrar_citas(s)
c = m.leer_cita(1)
v.mostrar_cita(c)

f, c = m.borrar_cita(1)
if f:
        v.borrar_cita(c)
else:
        v.cita_no_existe(c)
v.mostrar_citas(s)
'''

cont = Controller()
cont.start()