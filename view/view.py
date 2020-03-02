class View:
    def mostrar_contacto(self, contacto):
        print("********Datos del contacto*********")
        print("Nombre: ", contacto.nombre)
        print("Telefono: ", contacto.tel)
        print("Correo: ", contacto.correo)
        print("Doreccion: ", contacto.dir)
        print("*************************************")

    def mostrar_contactos(self, contactos):
        print("************Contactos****************")
        for c in contactos:
            print(c.nombre, c.tel,  c.correo, c.dir)
        print("*************************************")

    def agregar_contacto(self, contacto):
        print("****")
        print(contacto.nombre, "Se ha agregado a la base de datos")

    def borrar_contacto(self, contacto):
        #print(contacto.nombre, "Se ha borrado de la base de datos")
        print(contacto.id_contacto, "Se ha borrado de la base de datos")

    def actualizar_contacto(self, id_contacto):
        print(id_contacto, "Se ha modificado correctamente")
    
    def contacto_ya_existe(self, id_contacto):
       
        print("El contacto ", id_contacto, "Ya existe en la base de datos")

    def contacto_no_existe(self, id_contacto):
        print(id_contacto,"No existe en la base de datos")

    def start(self):
        print("-------Esto es un ejemplo de vista sencilla------- \n")

    def end(self):
        print("Hasta la vista")

    def opcion_no_valida(self):
        print('La opcion no valida!')
    
    def mostrar_cita(self, cita):
        print("********Citas del contacto*********")
        print("ID: ", cita.id_cita)
        print("Contacto", cita.id_contacto)
        print("Lugar: ", cita.lugar)
        print("Fecha: ", cita.fecha)
        print("Hora: ", cita.hora)
        print("Asunto: ", cita.asunto)
        print("*************************************")

    def mostrar_citas(self, citas):
        print("************Citas****************")
        for c in citas:
            print(c.id_cita, c. id_contacto, c.lugar, c.fecha,  c.hora, c.asunto)
        print("**********************************")

    def agregar_cita(self, cita):
        print("****")
        print(cita.fecha, cita.asunto, "Se ha agregado a la base de datos")

    def borrar_cita(self, cita):
        print(cita.fecha, cita.asunto, "Se ha borrado de la base de datos")

    #def actualizar_cita(self, cita_o, cita_n):
    #    print(cita_o.fecha, cita_o.asunto, "Se ha modificado correctamente")
    def actualizar_cita(self, id_cita):
        print(id_cita, "Se ha modificado correctamente")
    
    def cita_ya_existe(self, cita):
        print(cita.id_cita, "Ya existe la cita")

    def cita_no_existe(self, id_cita):
        print(id_cita,"No existe en la base de datos")

    def menu(self):
        print('1. Agregar contacto')
        print('2. Buscar contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Buscar por letra')
        print('6. Mostrar todos los contactos')
        print('7. Agregar cita')
        print('8. Buscar cita')
        print('9. Actualizar cita')
        print('10. Borrar cita')
        print('11. Salir')
