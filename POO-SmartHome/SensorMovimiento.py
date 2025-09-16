from .Dispositivo import Dispositivo
from datetime import datetime


class SensorMovimiento(Dispositivo):
    
    def __init__(self, id_dispositivo: int, nombre: str, marca: str, modelo: str,
                 consumo_energetico: float):
        super().__init__(id_dispositivo, nombre, "Sensor de Movimiento", marca, modelo, consumo_energetico)
        self._estado_activo = False
        self._ultima_deteccion = None
        self._registro_de_intrusos = []
    
    def get_estado_activo(self) -> bool:
        return self._estado_activo
    
    def get_ultima_deteccion(self):
        return self._ultima_deteccion
    
    def get_registro_de_intrusos(self):
        return self._registro_de_intrusos.copy()
    
    def encender(self) -> bool:
        try:
            if not self._estado:
                self._estado = True
                self._estado_activo = True
                print(f"Sensor {self._nombre} activado")
                return True
            return False
        except Exception as e:
            print(f"Error al encender sensor: {e}")
            return False
    
    def apagar(self) -> bool:
        try:
            if self._estado:
                self._estado = False
                self._estado_activo = False
                print(f"Sensor {self._nombre} desactivado")
                return True
            return False
        except Exception as e:
            print(f"Error al apagar sensor: {e}")
            return False
    
    def detectar_movimiento(self, deteccion: bool) -> bool:
        try:
            if not self._estado_activo:
                return False
            if deteccion:
                self._ultima_deteccion = datetime.now()
                print(f"Movimiento detectado por {self._nombre}")
                return True
            return False
        except Exception as e:
            print(f"Error al detectar movimiento: {e}")
            return False
    
    def registrar_intruso(self, hora: datetime, descripcion: str) -> None:
        try:
            registro = {
                'hora': hora,
                'descripcion': descripcion,
                'sensor': self._nombre
            }
            self._registro_de_intrusos.append(registro)
            print(f"Intrusión registrada: {descripcion} a las {hora.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"Error al registrar intruso: {e}")
    
    def registrar_anomalia(self, tipo: str, descripcion: str) -> None:
        try:
            registro = {
                'hora': datetime.now(),
                'tipo': tipo,
                'descripcion': descripcion,
                'sensor': self._nombre
            }
            self._registro_de_intrusos.append(registro)
            print(f"Anomalía registrada: {tipo} - {descripcion}")
        except Exception as e:
            print(f"Error al registrar anomalía: {e}")
    
    def enviar_alerta(self, mensaje: str) -> None:
        try:
            print(f"ALERTA DE SEGURIDAD - {self._nombre}: {mensaje}")
        except Exception as e:
            print(f"Error al enviar alerta: {e}")