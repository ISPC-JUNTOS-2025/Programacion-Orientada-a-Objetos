from .Dispositivo import Dispositivo


class Luz(Dispositivo):
    
    def __init__(self, id_dispositivo: int, nombre: str, marca: str, modelo: str,
                 consumo_energetico: float, intensidad: int = 50, regulable: bool = True):
        super().__init__(id_dispositivo, nombre, "Luz", marca, modelo, consumo_energetico)
        self._intensidad = max(0, min(100, intensidad))
        self._regulable = regulable
    
    def get_intensidad(self) -> int:
        return self._intensidad
    
    def get_regulable(self) -> bool:
        return self._regulable
    
    def encender(self) -> bool:
        if not self._estado:
            self._estado = True
            print(f"Luz {self._nombre} encendida al {self._intensidad}%")
            return True
        return False
    
    def apagar(self) -> bool:
        if self._estado:
            self._estado = False
            print(f"Luz {self._nombre} apagada")
            return True
        return False
    
    def regular_intensidad(self, nueva_intensidad: int) -> bool:
        if not self._regulable:
            print(f"La luz {self._nombre} no es regulable")
            return False
        if 0 <= nueva_intensidad <= 100:
            self._intensidad = nueva_intensidad
            if self._estado:
                print(f"Intensidad de {self._nombre} ajustada al {nueva_intensidad}%")
            return True
        else:
            print("La intensidad debe estar entre 0 y 100")
            return False