from .contacto import Contacto 
from .cita import Cita

class Model:   
    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id_contacto(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0

    #contacto methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        #if not self.esta_id(id_contacto)[0]: #devuelve tupla
        e, c = self.esta_id_contacto(id_contacto) #buscar id
        if not e:
            c= Contacto(id_contacto, nombre, tel, correo, dir) #despues de 3tener el contacto, se agrega a la lista
            self.contactos.append(c)
            return True, c
        return False, 0

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id_contacto(id_contacto)
        return e, c
        #e, c = self.esta_id(id_contacto)
        #if e: 
        #    return c
        #return False
                                       
    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dir):
        e, c = self.esta_id_contacto(id_contacto)
        if e:
            if n_nombre!= '':
                c.nombre = n_nombre
            if n_tel!='':
                c.tel = n_tel
            if n_correo!='':
                c.correo = n_correo
            if n_dir!='':
                c.dir = n_dir
        return False

    def borrar_contacto(self, id_contacto):
        e, c = self.esta_id_contacto(id_contacto)
        if e:
            self.contactos.remove(c)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True, c
        return False, 0    

    def leer_contactos_letra(self, letra):
    #lista =[c for c in self.contactos if c.nombre.lower().started]
        lista=[]
        for c in self.contactos:
            if c.nombre[0].lower() == letra.lower():
            #if c.nombre.lower().startwith(letra):
                lista.append(c)
        return lista
    
    def leer_todos_contactos(self):
        return self.contactos

    #########################cita methods
    
    def esta_id_cita(self, id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True, c
        return False, 0

    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        #if not self.esta_id_cita(id_cita)[0]: #devuelve tupla
        e, c = self.esta_id_cita(id_cita) #buscar id
        if not e:
            c = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto) #despues de 3tener el contacto, se agrega a la lista
            self.citas.append(c)
            return True, c
        return False,0

    def leer_cita(self, id_cita):
        e, c = self.esta_id_cita(id_cita)
        return e, c
        #if e: 
        #    return c
        #return False

    def actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, c = self.esta_id_cita(id_cita)
        if e:
            if n_id_contacto != '':
                c.id_contacto = n_id_contacto
            if n_lugar !='':
                c.lugar = n_lugar
            if n_fecha!='':
                c.fecha = n_fecha
            if n_hora !='':
                c.hora = n_hora
            if n_asunto != '':
                c.asunto = n_asunto
        return False

    def borrar_cita(self, id_cita):
        e, c = self.esta_id_cita(id_cita)
        if e:
            self.citas.remove(c)
            lista_temp = [c for c in self.citas if c.id_cita == id_cita]
            for c in lista_temp:
                self.citas.remove(c)
            return True, c
        return False, 0

        #e, c = self.esta_id_cita(id_cita)
        #if e:
        #    self.citas.remove(c)
        #    return True
        #return False

    def leer_citas_fecha(self, fecha):
        lista = []
        for c in self.citas:
            if c.fecha ==fecha:
                lista.append(c)
        return lista


#1) Actualizar solo ciertos elementos del contacto o cita

#2) Buscar contacto que empieza con una letra (pedir al usuario)
    #def esta_nom(self, nombre):
    #    inicial = input('inicial: ')
    #    for i in range(len(self.contactos)):
    #        x=self.contactos[i]
    #        if inicial in x[0]:
    #            print(x)
    #            return True
    #    return False

#3)Buscar las citas de la misma fecha (pedir al usuario)
    #def esta_fecha(self, fecha):
    #    for f in self.citas:
    #        if f.fecha == fecha:
    #            return True, f
    #    return False, 0
#
    #def buscar_fecha(self, fecha):
    #    e, f =self.esta_fecha(fecha)
    #    if e:
    #        return f
    #    return False
    #    #for f in self.citas:
    #    #    if f.fecha == fecha:
    #    #        return True
    #    #return False 