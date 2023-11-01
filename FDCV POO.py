class Persona:

    def __init__(self, nombre:str, apellido:str, cedula:str, correo:str):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._correo = correo


    def __str__(self):
        return f'Persona {self.__dict__.__str__()}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo



if __name__ == '__main__':
    objPersona1 = Persona(nombre='Karen', apellido='Paez', cedula='0978759219', correo='kpaez@gmail.com')
    print(objPersona1.__str__())

class Empleado:

    contador_empleado = 0
    def __init__(self, nombre, apellido, cedula, sueldo):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._sueldo = sueldo
        Empleado.contador_empleado += 1
        self._id_empleado = Empleado.contador_empleado

    @property
    def id_empleado(self):
        return self._id_empleado

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: {self.__dict__.__str__()}'


if __name__ == '__main__':
    e1 = Empleado(nombre='Juan', apellido='Crovill', cedula='0957808181', sueldo=675)
    print(e1)
    e2 = Empleado(nombre='Yurin', apellido='Gonzales', cedula='0920077732', sueldo=800)
    print(e2)


class Cliente:

    contador_cliente = 0
    def __init__(self, nombre, apellido, fecha_registro, vip):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_registro = fecha_registro
        self._vip = vip
        Cliente.contador_cliente += 1
        self._id_cliente = Cliente.contador_cliente

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    def __str__(self):
        return f'Cliente: {self.__dict__.__str__()}'


if __name__ == '__main__':
    cli1 = Cliente(nombre='Dorys', apellido='Villao', fecha_registro='13-10-2023', vip= True)
    print(cli1)
    cli2 = Cliente(nombre='Carlos', apellido='Crofford', fecha_registro='19-10-2023', vip= False)
    print(cli2)