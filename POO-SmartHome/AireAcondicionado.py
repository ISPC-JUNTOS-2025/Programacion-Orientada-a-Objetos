from .Dispositivo import Dispositivo


class AireAcondicionado(Dispositivo):
    
    def __init__(self, id_dispositivo: int, nombre: str, marca: str, modelo: str,
                 consumo_energetico: float, temperatura_actual: int = 22):
        super().__init__(id_dispositivo, nombre, "Aire Acondicionado", marca, modelo, consumo_energetico)
        self._temperatura_actual = temperatura_actual
        self._temperatura_objetivo = temperatura_actual
        self._modo_eco = False
    
    def get_temperatura_actual(self) -> int:
        return self._temperatura_actual
    
    def get_temperatura_objetivo(self) -> int:
        return self._temperatura_objetivo
    
    def get_modo_eco(self) -> bool:
        return self._modo_eco
    
    def encender(self) -> bool:
        try:
            if not self._estado:
                self._estado = True
                print(f"Aire acondicionado {self._nombre} encendido - Temp: {self._temperatura_actual}°C")
                return True
            return False
        except Exception as e:
            print(f"Error al encender aire acondicionado: {e}")
            return False
    
    def apagar(self) -> bool:
        try:
            if self._estado:
                self._estado = False
                print(f"Aire acondicionado {self._nombre} apagado")
                return True
            return False
        except Exception as e:
            print(f"Error al apagar aire acondicionado: {e}")
            return False
    
    def establecer_temperatura(self, temp: int) -> bool:
        try:
            if 16 <= temp <= 30:
                self._temperatura_objetivo = temp
                if self._estado:
                    print(f"Temperatura objetivo de {self._nombre} establecida en {temp}°C")
                return True
            else:
                print("La temperatura debe estar entre 16°C y 30°C")
                return False
        except Exception as e:
            print(f"Error al establecer temperatura: {e}")
            return False
    
    def activar_modo_eco(self) -> bool:
        try:
            self._modo_eco = True
            print(f"Modo ecológico activado en {self._nombre}")
            return True
        except Exception as e:
            print(f"Error al activar modo eco: {e}")
            return False
