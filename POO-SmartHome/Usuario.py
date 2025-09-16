from datetime import datetime, date
from enums import Rol
from utilidades.utilidades import verificar_email, encriptar_contraseña, desencriptar_contraseña, validar_fecha_nacimiento

lista_de_usuarios = []

class Usuario:
    def __init__(self, id_usuario: int, nombre: str, apellido: str, email: str, 
                 contraseña: str, telefono: str, rol: Rol, fecha_nacimiento: date):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contraseña = contraseña
        self.__telefono = telefono
        self.__rol = rol
        self.__fecha_creacion = datetime.now()
        self.__fecha_nacimiento = fecha_nacimiento
        self.__lista_de_domicilios = []
    
    def get_id_usuario(self): 
        return self.__id_usuario
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre.strip()
    
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, apellido):
        self.__apellido = apellido.strip()
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def set_contraseña(self, contraseña):
        self.__contraseña = contraseña.strip()

    def get_contraseña(self):
        return self.__contraseña
    
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def get_rol(self):
        return self.__rol

    def set_rol(self, rol: Rol):
        self.__rol = rol
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    
    def get_lista_de_domicilios(self):
        return self.__lista_de_domicilios

    def set_lista_de_domicilios(self, nuevo_domicilio):
        self.__lista_de_domicilios.append(nuevo_domicilio)

    
    def registrar_usuario(self, nombre, apellido, email, contraseña, telefono, fecha_nacimiento):
        try:
            if nombre == " " or nombre == "":
                raise ValueError("El nombre no puede estar vacio")
            if apellido == " " or apellido == "":
                raise ValueError("El apellido no puede estar vacio")
            if contraseña == " " or contraseña == "":
                raise ValueError("La contraseña no puede estar vacia")
            if telefono == " " or telefono == "":
                raise ValueError("El telefono no puede estar vacio")
            if fecha_nacimiento == " " or fecha_nacimiento == "":
                raise ValueError("La fecha de nacimiento no puede estar vacia")
            
            validar_fecha_nacimiento(fecha_nacimiento)
            verificar_email(email)

            contraseña_encriptada = encriptar_contraseña(contraseña)

            self.set_nombre(nombre)
            self.set_apellido(apellido)
            self.set_email(email)
            self.set_contraseña(contraseña_encriptada)
            self.set_telefono(telefono)
            self.set_fecha_nacimiento(fecha_nacimiento)
            self.set_rol(Rol.USUARIO)

            usuario = {
                "nombre": self.get_nombre(),
                "apellido": self.get_apellido(),
                "email": self.get_email(),
                "telefono": self.get_telefono(),
                "rol": self.get_rol(),
                "fecha_nacimiento": self.get_fecha_nacimiento(),
                "fecha_creacion": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "direcciones": []
            }
            print(f"Usuario registrado exitosamente: {usuario['nombre']} {usuario['apellido']}")
            lista_de_usuarios.append(usuario)
            return usuario
        except ValueError as error:
            raise error


    def iniciar_sesion(self, email: str, contraseña: str):
        try:
            if contraseña == ' ' or email == '':
                raise ValueError("El email o la contraseña no pueden estar vacíos.")
            
            verificar_email(email)
            
            if email != self.__email:
                raise ValueError("Email o contraseña incorrectos")
            
            contraseña_encriptada_ingresada = encriptar_contraseña(contraseña)
            
            if self.__contraseña != contraseña_encriptada_ingresada:
                raise ValueError("Email o contraseña incorrectos")
            
            print(f"Inicio de sesión exitoso. Bienvenido, {self.get_nombre()}.")
            return {
                'nombre': self.get_nombre(),
                'apellido': self.get_apellido(),
                'email': self.get_email(),
                'rol': self.get_rol().value,
                'fecha_creacion': self.__fecha_creacion.strftime("%d-%m-%Y %H:%M:%S"),
                'direcciones': self.get_lista_de_domicilios()
            }
        except ValueError as error:
            raise error
        except Exception as e:
            raise Exception(f"Error al iniciar sesión: {e}")
    

    def consultar_datos_personales(self):
        try:
            print("\n--- DATOS PERSONALES ---")
            print(f"Nombre: {self.get_nombre()}")
            print(f"Apellido: {self.get_apellido()}")
            print(f"Email: {self.get_email()}")
            print(f"Telefono: {self.get_telefono()}")
            print(f"Fecha de nacimiento: {self.get_fecha_nacimiento().strftime('%d-%m-%Y')}")
            
            if self.get_lista_de_domicilios() and len(self.get_lista_de_domicilios()) > 0:
                print("\n--- DIRECCIONES ---")
                for domicilio in self.get_lista_de_domicilios():
                    print(f"• {domicilio}")
            else:
                print("\n--- DIRECCIONES ---")
                print("No tiene direcciones registradas")
            
            return {
                'nombre': self.get_nombre(),
                'apellido': self.get_apellido(),
                'email': self.get_email(),
                'telefono': self.get_telefono(),
                'fecha_nacimiento': self.get_fecha_nacimiento().strftime('%d-%m-%Y'),
                'direcciones': self.get_lista_de_domicilios()
            }
        except Exception as e:
            raise Exception(f"Error al consultar datos personales: {e}")
    
    def cambiar_rol_de_usuario(self, nuevo_rol: Rol):
        try:
            if nuevo_rol is None:
                raise ValueError("El nuevo rol no puede ser nulo")
            
            rol_anterior = self.get_rol()
            self.set_rol(nuevo_rol)
            
            print(f"{self.get_nombre()} ahora es {nuevo_rol.value}")
            return True
        except ValueError as error:
            raise error
        except Exception as e:
            raise Exception(f"Error al cambiar rol: {e}")
    
    def agregar_domicilio(self, domicilio):
        try:
            if domicilio is None:
                raise ValueError("El domicilio no puede ser nulo")
            
            if domicilio in self.get_lista_de_domicilios():
                print("El usuario ya tiene asignada esta dirección")
                return True
            
            self.set_lista_de_domicilios(domicilio)
            print(f"Dirección agregada exitosamente")
            return True
        except ValueError as error:
            raise error
        except Exception as e:
            raise Exception(f"Error al agregar domicilio: {e}")
    
    def remover_domicilio(self, domicilio):
        try:
            if domicilio is None:
                raise ValueError("El domicilio no puede ser nulo")
            
            if domicilio not in self.get_lista_de_domicilios():
                print("El usuario no tiene asignada esta dirección")
                return True
            
            self.get_lista_de_domicilios().remove(domicilio)
            print(f"Dirección removida exitosamente")
            return True
        except ValueError as error:
            raise error
        except Exception as e:
            raise Exception(f"Error al remover domicilio: {e}")
    
    def consultar_direcciones_usuario(self):
        try:
            if not self.get_lista_de_domicilios() or len(self.get_lista_de_domicilios()) == 0:
                print("No tiene direcciones asignadas")
                return
            
            print(f"\n--- DIRECCIONES ---")
            for domicilio in self.get_lista_de_domicilios():
                print(f"Dirección: {domicilio}")
                print("-" * 30)
                
        except Exception as e:
            raise Exception(f"Error al consultar direcciones: {e}")
    
    def __str__(self) -> str:
        try:
            return f"{self.get_nombre()} {self.get_apellido()} ({self.get_rol().value})"
        except Exception as e:
            return f"Error al obtener representación del usuario: {e}"
