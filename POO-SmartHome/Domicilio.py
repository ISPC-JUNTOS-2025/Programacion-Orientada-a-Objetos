 


class Domicilio:
    
    def __init__(self, id_domicilio: int, calle: str, numero: int, barrio: str, 
                 ciudad: str, pais: str, codigo_postal: str):
        self._id_domicilio = id_domicilio
        self._calle = calle
        self._numero = numero
        self._barrio = barrio
        self._ciudad = ciudad
        self._pais = pais
        self._codigo_postal = codigo_postal
        self._ubicaciones_casa = []
    
    def get_id_domicilio(self) -> int:
        return self._id_domicilio
    
    def get_calle(self) -> str:
        return self._calle
    
    def set_calle(self, valor: str) -> None:
        try:
            if not valor or not valor.strip():
                raise ValueError("La calle no puede estar vacía")
            self._calle = valor.strip()
        except Exception as e:
            raise ValueError(f"Error al establecer calle: {e}")
    
    def get_numero(self) -> int:
        return self._numero
    
    def set_numero(self, valor: int) -> None:
        try:
            if valor <= 0:
                raise ValueError("El número debe ser mayor a 0")
            self._numero = valor
        except Exception as e:
            raise ValueError(f"Error al establecer número: {e}")
    
    def get_barrio(self) -> str:
        return self._barrio
    
    def set_barrio(self, valor: str) -> None:
        try:
            if not valor or not valor.strip():
                raise ValueError("El barrio no puede estar vacío")
            self._barrio = valor.strip()
        except Exception as e:
            raise ValueError(f"Error al establecer barrio: {e}")
    
    def get_ciudad(self) -> str:
        return self._ciudad
    
    def set_ciudad(self, valor: str) -> None:
        try:
            if not valor or not valor.strip():
                raise ValueError("La ciudad no puede estar vacía")
            self._ciudad = valor.strip()
        except Exception as e:
            raise ValueError(f"Error al establecer ciudad: {e}")
    
    def get_pais(self) -> str:
        return self._pais
    
    def set_pais(self, valor: str) -> None:
        try:
            if not valor or not valor.strip():
                raise ValueError("El país no puede estar vacío")
            self._pais = valor.strip()
        except Exception as e:
            raise ValueError(f"Error al establecer país: {e}")
    
    def get_codigo_postal(self) -> str:
        return self._codigo_postal
    
    def set_codigo_postal(self, valor: str) -> None:
        try:
            if not valor or not valor.strip():
                raise ValueError("El código postal no puede estar vacío")
            self._codigo_postal = valor.strip()
        except Exception as e:
            raise ValueError(f"Error al establecer código postal: {e}")
    
    def get_ubicaciones_casa(self):
        return self._ubicaciones_casa.copy()
    
    def registrar_domicilio(self) -> bool:
        try:
            print(f"Domicilio registrado: {self._calle} {self._numero}, {self._barrio}")
            print(f"{self._ciudad}, {self._pais} {self._codigo_postal}")
            return True
        except Exception as e:
            print(f"Error al registrar domicilio: {e}")
            return False
    
    def eliminar_domicilio(self) -> bool:
        try:
            print(f"Domicilio eliminado: {self._calle} {self._numero}")
            return True
        except Exception as e:
            print(f"Error al eliminar domicilio: {e}")
            return False
    
    def buscar_domicilio_por_email_usuario(self, email: str) -> bool:
        try:
            print(f"Buscando domicilio para usuario con email: {email}")
            return True
        except Exception as e:
            print(f"Error en búsqueda por email: {e}")
            return False
    
    def buscar_domicilio_por_id(self, id_domicilio: int) -> bool:
        try:
            if self._id_domicilio == id_domicilio:
                print(f"Domicilio encontrado: {self._calle} {self._numero}")
                return True
            else:
                print("Domicilio no encontrado")
                return False
        except Exception as e:
            print(f"Error en búsqueda por ID: {e}")
            return False
    
    def agregar_ubicacion(self, ubicacion: 'UbicacionCasa') -> bool:
        try:
            if ubicacion not in self._ubicaciones_casa:
                self._ubicaciones_casa.append(ubicacion)
                print(f"Ubicación '{ubicacion.get_nombre()}' agregada al domicilio")
                return True
            else:
                print("La ubicación ya está asociada a este domicilio")
                return False
        except Exception as e:
            print(f"Error al agregar ubicación: {e}")
            return False
    
    def remover_ubicacion(self, ubicacion: 'UbicacionCasa') -> bool:
        try:
            if ubicacion in self._ubicaciones_casa:
                self._ubicaciones_casa.remove(ubicacion)
                print(f"Ubicación '{ubicacion.get_nombre()}' removida del domicilio")
                return True
            else:
                print("La ubicación no está asociada a este domicilio")
                return False
        except Exception as e:
            print(f"Error al remover ubicación: {e}")
            return False
    
    def obtener_direccion_completa(self) -> str:
        try:
            return f"{self._calle} {self._numero}, {self._barrio}, {self._ciudad}, {self._pais} {self._codigo_postal}"
        except Exception as e:
            print(f"Error al obtener dirección completa: {e}")
            return ""
    
    def __str__(self) -> str:
        return self.obtener_direccion_completa()


class UbicacionCasa:
    
    def __init__(self, id_ubicacion: int, nombre: str, descripcion: str):
        self._id_ubicacion = id_ubicacion
        self._nombre = nombre
        self._descripcion = descripcion
        self._dispositivos = []
    
    def get_id_ubicacion(self) -> int:
        return self._id_ubicacion
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def set_nombre(self, valor: str) -> None:
        try:
            if not valor or not valor.strip():
                raise ValueError("El nombre no puede estar vacío")
            self._nombre = valor.strip()
        except Exception as e:
            raise ValueError(f"Error al establecer nombre: {e}")
    
    def get_descripcion(self) -> str:
        return self._descripcion
    
    def set_descripcion(self, valor: str) -> None:
        try:
            if not valor or not valor.strip():
                raise ValueError("La descripción no puede estar vacía")
            self._descripcion = valor.strip()
        except Exception as e:
            raise ValueError(f"Error al establecer descripción: {e}")
    
    def get_dispositivos(self):
        return self._dispositivos.copy()
    
    def crear_ubicacion(self) -> bool:
        try:
            print(f"Ubicación '{self._nombre}' creada exitosamente")
            print(f"Descripción: {self._descripcion}")
            return True
        except Exception as e:
            print(f"Error al crear ubicación: {e}")
            return False
    
    def leer_ubicacion(self) -> dict:
        try:
            return {
                'id_ubicacion': self._id_ubicacion,
                'nombre': self._nombre,
                'descripcion': self._descripcion,
                'cantidad_dispositivos': len(self._dispositivos)
            }
        except Exception as e:
            print(f"Error al leer ubicación: {e}")
            return {}
    
    def actualizar_ubicacion(self, nuevo_nombre: str = None, nueva_descripcion: str = None) -> bool:
        try:
            if nuevo_nombre:
                self.set_nombre(nuevo_nombre)
            if nueva_descripcion:
                self.set_descripcion(nueva_descripcion)
            
            print(f"Ubicación actualizada: {self._nombre}")
            return True
        except Exception as e:
            print(f"Error al actualizar ubicación: {e}")
            return False
    
    def eliminar_ubicacion(self) -> bool:
        try:
            print(f"Ubicación '{self._nombre}' eliminada exitosamente")
            return True
        except Exception as e:
            print(f"Error al eliminar ubicación: {e}")
            return False
    
    def agregar_dispositivo(self, dispositivo: Any) -> bool:
        try:
            if dispositivo not in self._dispositivos:
                self._dispositivos.append(dispositivo)
                print(f"Dispositivo '{dispositivo.get_nombre()}' agregado a '{self._nombre}'")
                return True
            else:
                print("El dispositivo ya está en esta ubicación")
                return False
        except Exception as e:
            print(f"Error al agregar dispositivo: {e}")
            return False
    
    def remover_dispositivo(self, dispositivo: Any) -> bool:
        try:
            if dispositivo in self._dispositivos:
                self._dispositivos.remove(dispositivo)
                print(f"Dispositivo '{dispositivo.get_nombre()}' removido de '{self._nombre}'")
                return True
            else:
                print("El dispositivo no está en esta ubicación")
                return False
        except Exception as e:
            print(f"Error al remover dispositivo: {e}")
            return False
    
    def listar_dispositivos(self):
        try:
            return [dispositivo.listar_dispositivos() for dispositivo in self._dispositivos]
        except Exception as e:
            print(f"Error al listar dispositivos: {e}")
            return []
    
    def __str__(self) -> str:
        return f"{self._nombre}: {self._descripcion}"
