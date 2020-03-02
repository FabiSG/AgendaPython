from model.model import Model
from view.view import View

class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()

        #Contacto controllers (lo que se puede hacer con los metodos)

    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)  #llamar el metodo agregar contacto de modelo
        if e:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e: 
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c) 

    def actualizar_contacto(self, id_contacto, n_nombre= '', n_tel='', n_correo='', n_dir=''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)  #e bandera
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_citas_fecha(self, fecha):
        c = self.model.leer_citas_fecha(fecha)
        self.view.mostrar_citas(c)

    ###############-- cita controller ---########################################3
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)  #llamar el metodo agregar contacto de modelo
        if e:
            self.view.agregar_cita(c)
        else:
            self.view.cita_ya_existe(c)   

    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e: 
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def actualizar_cita(self, id_cita, n_id_contacto='', n_lugar='', n_fecha='', n_hora='', n_asunto=''):
        e = self.model.actualizar_cita(id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)  #e bandera
        if e:
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def borrar_cita(self, id_cita):
        e, c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    ######################General methods
    def insertar_contactos(self):
        self.agregar_contacto(1, 'Juan Perez', '464-123-1234', 'juanp1@gmail.com', 'Zaragoza 110')
        self.agregar_contacto(2, 'Maria Lopez', '462-122-4562', 'marialz@gmail.com', 'Arteaga 55')
        self.agregar_contacto(3, 'Brenda hernandez', '456-545-7812', 'brenh@gmail.com', '5 de Mayo')

    def insertar_citas(self):
        self.agregar_cita(1, 1, 'Obregon 5', '15-04-20', '12:00', 'Corte de cabello')
        self.agregar_cita(2, 2, 'Allende 2', '6-05-20', '5:00', 'Dentista')
        self.agregar_cita(3, 1, 'zapata 13', '22-07-20', '2:00', 'curso')

    def start(self):
        #display a welcome message
        self.view.start()
        #insert in model
        self.insertar_contactos()
        self.insertar_citas()
        #shoe all contacts in DB
        self.leer_todos_contactos()
        #self.leer_contactos_letra('J')
        self.menu()

    ##############Menu
    def menu(self):
       #Display menu
       self.view.menu()
       o = input("Selecciona una opcion (1-11): ")

       if o == '1':
            id_contacto = int(input('Nuevo ID del contacto: '))
            nombre = input('Nombre: ')
            tel = input('Telefono: ')
            correo = input('Correo:')
            dir = input('Direccion: ')
            self.agregar_contacto(id_contacto, nombre, tel, correo, dir)

       elif o == '2':
           id_contacto = int(input('ID del contacto a buscar: '))
           self.leer_contacto(id_contacto)

       elif o == '3':
           id_contacto = int(input('ID del contacto a actualizar: '))
           nombre = input('Nuevo nombre: ')
           tel = input('Nuevo telefono: ')
           correo = input('Nuevo correo: ')
           dir = input('Nueva direccion: ')
           self.actualizar_contacto(id_contacto, nombre, tel, correo, dir)

       elif o == '4':
           id_contacto = int(input('ID contacto a eliminar: '))
           self.borrar_contacto(id_contacto)

       elif o == '5':
            letra = input('letra: ')
            self.leer_contactos_letra(letra)

       elif o == '6':
           self.leer_todos_contactos()

       elif o == '7':
           id_cita = int(input('ID cita: '))
           id_contacto = int(input('ID del contacto: '))
           lugar = input('Lugar de la cita: ')
           fecha = input('Fecha de la cita: ')
           hora = input('Hora de la cita: ')
           asunto = input('Asunto: ')
           self.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)

       elif o == '8':
           id_cita = int(input('ID de la cita a buscar: '))
           self.leer_cita(id_cita)

       elif o == '9':
           id_cita = int(input('ID cita a actualizar: '))
           id_contacto = int(input('ID contacto a actualizar: '))
           lugar = input('Nuevo lugar de la cita: ')
           fecha = input('Nueva fecha de la cita: ')
           hora = input('Nueva hora de la cita: ')
           asunto = input('Nuevo asunto de la cita: ')
           self.actualizar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)

       elif o == '10':
           id_cita = int(input('ID cita a eliminar: '))
           self.borrar_cita(id_cita)
     
 
       elif o == '11':
           self.view.end()
       else:
           self.view.opcion_no_valida()
    #cita controller