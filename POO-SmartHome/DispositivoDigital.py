from .Dispositivo import Dispositivo
from enums import TipoDispositivoDigital


class DispositivoDigital(Dispositivo):
    
    def __init__(self, id_dispositivo: int, nombre: str, marca: str, modelo: str,
                 consumo_energetico: float, tipo_dispositivo: TipoDispositivoDigital):
        super().__init__(id_dispositivo, nombre, "Dispositivo Digital", marca, modelo, consumo_energetico)
        self._tipo_dispositivo = tipo_dispositivo
    
    def get_tipo_dispositivo(self) -> TipoDispositivoDigital:
        return self._tipo_dispositivo
    
    def encender(self) -> bool:
        try:
            if not self._estado:
                self._estado = True
                print(f"{self._nombre} encendido")
                return True
            return False
        except Exception as e:
            print(f"Error al encender dispositivo digital: {e}")
            return False
    
    def apagar(self) -> bool:
        try:
            if self._estado:
                self._estado = False
                print(f"{self._nombre} apagado")
                return True
            return False
        except Exception as e:
            print(f"Error al apagar dispositivo digital: {e}")
            return False
    
    def reiniciar(self) -> bool:
        try:
            if self._estado:
                print(f"Reiniciando {self._nombre}...")
                self.apagar()
                self.encender()
                return True
            return False
        except Exception as e:
            print(f"Error al reiniciar dispositivo digital: {e}")
            return False
    
    def ver_informacion(self) -> str:
        try:
            return f"""
        Dispositivo Digital: {self._nombre}
        Tipo: {self._tipo_dispositivo.value}
        Marca: {self._marca}
        Modelo: {self._modelo}
        Estado: {'Encendido' if self._estado else 'Apagado'}
        Consumo: {self._consumo_energetico}W
        """
        except Exception as e:
            print(f"Error al ver información: {e}")
            return ""
