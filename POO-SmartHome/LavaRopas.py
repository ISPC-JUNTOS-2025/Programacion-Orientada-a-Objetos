from .Dispositivo import Dispositivo
from ..enums import ProgramaLavaRopas


class LavaRopas(Dispositivo):
    
    def __init__(self, id_dispositivo: int, nombre: str, marca: str, modelo: str,
                 consumo_energetico: float, velocidad_max_centrifugado: int = 1200):
        super().__init__(id_dispositivo, nombre, "Lavadora", marca, modelo, consumo_energetico)
        self._programa_actual = ProgramaLavaRopas.LAVADO_RAPIDO
        self._velocidad_centrifugado = 0
        self._velocidad_max_centrifugado = velocidad_max_centrifugado
        self._puerta_bloqueada = False
    
    def get_programa_actual(self) -> ProgramaLavaRopas:
        return self._programa_actual
    
    def get_velocidad_centrifugado(self) -> int:
        return self._velocidad_centrifugado
    
    def get_velocidad_max_centrifugado(self) -> int:
        return self._velocidad_max_centrifugado
    
    def get_puerta_bloqueada(self) -> bool:
        return self._puerta_bloqueada
    
    def encender(self) -> bool:
        try:
            if not self._estado:
                self._estado = True
                print(f"Lavadora {self._nombre} encendida - Programa: {self._programa_actual.value}")
                return True
            return False
        except Exception as e:
            print(f"Error al encender lavadora: {e}")
            return False
    
    def apagar(self) -> bool:
        try:
            if self._estado:
                self._estado = False
                self._puerta_bloqueada = False
                print(f"Lavadora {self._nombre} apagada")
                return True
            return False
        except Exception as e:
            print(f"Error al apagar lavadora: {e}")
            return False
    
    def seleccionar_programa(self, programa: ProgramaLavaRopas) -> bool:
        try:
            if not self._estado:
                print("La lavadora debe estar encendida para seleccionar programa")
                return False
            
            self._programa_actual = programa
            print(f"Programa {programa.value} seleccionado en {self._nombre}")
            return True
        except Exception as e:
            print(f"Error al seleccionar programa: {e}")
            return False
    
    def iniciar_lavado(self) -> bool:
        try:
            if not self._estado:
                print("La lavadora debe estar encendida para iniciar lavado")
                return False
            
            if self._puerta_bloqueada:
                print("No se puede iniciar lavado con la puerta bloqueada")
                return False
            
            self._puerta_bloqueada = True
            print(f"Iniciando lavado con programa {self._programa_actual.value} en {self._nombre}")
            return True
        except Exception as e:
            print(f"Error al iniciar lavado: {e}")
            return False
    
    def pausar_lavado(self) -> bool:
        try:
            if self._puerta_bloqueada:
                self._puerta_bloqueada = False
                print(f"Lavado pausado en {self._nombre}")
                return True
            return False
        except Exception as e:
            print(f"Error al pausar lavado: {e}")
            return False
    
    def desbloquear_puerta(self) -> bool:
        try:
            if self._puerta_bloqueada:
                self._puerta_bloqueada = False
                print(f"Puerta de {self._nombre} desbloqueada")
                return True
            return False
        except Exception as e:
            print(f"Error al desbloquear puerta: {e}")
            return False
