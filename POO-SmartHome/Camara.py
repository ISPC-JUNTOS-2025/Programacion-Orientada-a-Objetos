from .Dispositivo import Dispositivo


class Camara(Dispositivo):
    
    def __init__(self, id_dispositivo: int, nombre: str, marca: str, modelo: str,
                 consumo_energetico: float, resolucion: str = "1080p", 
                 vision_nocturna: bool = True, almacenamiento_local: bool = True):
        super().__init__(id_dispositivo, nombre, "Cámara", marca, modelo, consumo_energetico)
        self._resolucion = resolucion
        self._vision_nocturna = vision_nocturna
        self._grabacion = False
        self._almacenamiento_local = almacenamiento_local
    
    def get_resolucion(self) -> str:
        return self._resolucion
    
    def get_vision_nocturna(self) -> bool:
        return self._vision_nocturna
    
    def get_grabacion(self) -> bool:
        return self._grabacion
    
    def get_almacenamiento_local(self) -> bool:
        return self._almacenamiento_local
    
    def encender(self) -> bool:
        if not self._estado:
            self._estado = True
            print(f"Cámara {self._nombre} encendida - Resolución: {self._resolucion}")
            return True
        return False
    
    def apagar(self) -> bool:
        if self._estado:
            if self._grabacion:
                self.detener_grabacion()
            self._estado = False
            print(f"Cámara {self._nombre} apagada")
            return True
        return False
    
    def grabar(self) -> bool:
        if self._estado and not self._grabacion:
            self._grabacion = True
            print(f"Cámara {self._nombre} iniciando grabación en {self._resolucion}")
            return True
        return False
    
    def detener_grabacion(self) -> bool:
        if self._grabacion:
            self._grabacion = False
            print(f"Cámara {self._nombre} deteniendo grabación")
            return True
        return False
