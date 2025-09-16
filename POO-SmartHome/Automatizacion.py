 


class Automatizacion:
    
    def __init__(self, id_automatizacion: int, nombre: str, descripcion: str, 
                 regla: str, condicion: str, accion: str):
        self._id_automatizacion = id_automatizacion
        self._nombre = nombre
        self._descripcion = descripcion
        self._estado = False
        self._regla = regla
        self._condicion = condicion
        self._accion = accion
        self._dispositivos_controlados = []
    
    def get_id_automatizacion(self) -> int:
        return self._id_automatizacion
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def set_nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()
    
    def get_descripcion(self) -> str:
        return self._descripcion
    
    def set_descripcion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La descripción no puede estar vacía")
        self._descripcion = valor.strip()
    
    def get_estado(self) -> bool:
        return self._estado
    
    def get_regla(self) -> str:
        return self._regla
    
    def set_regla(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La regla no puede estar vacía")
        self._regla = valor.strip()
    
    def get_condicion(self) -> str:
        return self._condicion
    
    def set_condicion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La condición no puede estar vacía")
        self._condicion = valor.strip()
    
    def get_accion(self) -> str:
        return self._accion
    
    def set_accion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La acción no puede estar vacía")
        self._accion = valor.strip()
    
    def get_dispositivos_controlados(self):
        return self._dispositivos_controlados.copy()
    
    def activar_automatizacion_encender_luces(self) -> bool:
        try:
            if not self._estado:
                self._estado = True
                print(f"Automatización '{self._nombre}' activada para encender luces")
                
                luces = [d for d in self._dispositivos_controlados if hasattr(d, 'regular_intensidad')]
                
                if luces:
                    for luz in luces:
                        if hasattr(luz, 'encender'):
                            luz.encender()
                            if hasattr(luz, 'regular_intensidad'):
                                luz.regular_intensidad(80)
                    print(f"Se encendieron {len(luces)} luces")
                else:
                    print("No hay luces configuradas en esta automatización")
                
                return True
            else:
                print("La automatización ya está activa")
                return False
        except Exception as e:
            print(f"Error al activar automatización: {e}")
            return False
    
    def desactivar_automatizacion_encender_luces(self) -> bool:
        try:
            if self._estado:
                self._estado = False
                print(f"Automatización '{self._nombre}' desactivada")
                
                luces = [d for d in self._dispositivos_controlados if hasattr(d, 'regular_intensidad')]
                
                if luces:
                    for luz in luces:
                        if hasattr(luz, 'apagar'):
                            luz.apagar()
                    print(f"Se apagaron {len(luces)} luces")
                
                return True
            else:
                print("La automatización ya está desactivada")
                return False
        except Exception as e:
            print(f"Error al desactivar automatización: {e}")
            return False
    
    def consultar_automatizaciones_activas(self) -> dict:
        try:
            return {
                'id_automatizacion': self._id_automatizacion,
                'nombre': self._nombre,
                'descripcion': self._descripcion,
                'estado': 'Activa' if self._estado else 'Inactiva',
                'regla': self._regla,
                'condicion': self._condicion,
                'accion': self._accion,
                'dispositivos_controlados': len(self._dispositivos_controlados)
            }
        except Exception as e:
            print(f"Error al consultar automatizaciones activas: {e}")
            return {}
    
    def menu_automatizaciones(self) -> None:
        try:
            print("\n=== MENÚ DE AUTOMATIZACIONES ===")
            print(f"Automatización: {self._nombre}")
            print(f"Estado: {'Activa' if self._estado else 'Inactiva'}")
            print(f"Descripción: {self._descripcion}")
            print(f"Regla: {self._regla}")
            print(f"Condición: {self._condicion}")
            print(f"Acción: {self._accion}")
            print(f"Dispositivos controlados: {len(self._dispositivos_controlados)}")
            
            if self._dispositivos_controlados:
                print("\nDispositivos controlados:")
                for i, dispositivo in enumerate(self._dispositivos_controlados, 1):
                    print(f"  {i}. {dispositivo.get_nombre()} ({dispositivo.get_tipo()})")
        except Exception as e:
            print(f"Error al mostrar menú de automatizaciones: {e}")
    
    def agregar_dispositivo(self, dispositivo: Any) -> bool:
        try:
            if dispositivo not in self._dispositivos_controlados:
                self._dispositivos_controlados.append(dispositivo)
                print(f"Dispositivo '{dispositivo.get_nombre()}' agregado a la automatización")
                return True
            else:
                print("El dispositivo ya está en esta automatización")
                return False
        except Exception as e:
            print(f"Error al agregar dispositivo: {e}")
            return False
    
    def remover_dispositivo(self, dispositivo: Any) -> bool:
        try:
            if dispositivo in self._dispositivos_controlados:
                self._dispositivos_controlados.remove(dispositivo)
                print(f"Dispositivo '{dispositivo.get_nombre()}' removido de la automatización")
                return True
            else:
                print("El dispositivo no está en esta automatización")
                return False
        except Exception as e:
            print(f"Error al remover dispositivo: {e}")
            return False
    
    def ejecutar_automatizacion(self) -> bool:
        try:
            if not self._estado:
                print("La automatización está desactivada")
                return False
            
            print(f"Ejecutando automatización: {self._nombre}")
            print(f"Regla: {self._regla}")
            print(f"Condición: {self._condicion}")
            print(f"Acción: {self._accion}")
            
            if "encender" in self._accion.lower() and "luz" in self._accion.lower():
                return self.activar_automatizacion_encender_luces()
            elif "apagar" in self._accion.lower() and "luz" in self._accion.lower():
                return self.desactivar_automatizacion_encender_luces()
            else:
                print("Tipo de automatización no reconocido")
                return False
        except Exception as e:
            print(f"Error al ejecutar automatización: {e}")
            return False
    
    def validar_condicion(self, valor_sensor: Any = None) -> bool:
        try:
            if "movimiento" in self._condicion.lower():
                return valor_sensor is not None and valor_sensor
            elif "hora" in self._condicion.lower():
                return True
            elif "temperatura" in self._condicion.lower():
                return True
            else:
                return True
        except Exception as e:
            print(f"Error al validar condición: {e}")
            return False
    
    def __str__(self) -> str:
        estado_str = "Activa" if self._estado else "Inactiva"
        return f"{self._nombre} ({estado_str}) - {self._descripcion}"
