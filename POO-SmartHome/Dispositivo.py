from abc import ABC, abstractmethod
from datetime import datetime


class Dispositivo(ABC):
    
    def __init__(self, id_dispositivo: int, nombre: str, tipo: str, marca: str, 
                 modelo: str, consumo_energetico: float):
        self._id_dispositivo = id_dispositivo
        self._nombre = nombre
        self._tipo = tipo
        self._marca = marca
        self._modelo = modelo
        self._estado = False
        self._consumo_energetico = consumo_energetico
        self._fecha_creacion = datetime.now()
        self._automatizaciones = []
    
    def get_id_dispositivo(self) -> int:
        return self._id_dispositivo
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def set_nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()
    
    def get_tipo(self) -> str:
        return self._tipo
    
    def get_marca(self) -> str:
        return self._marca
    
    def get_modelo(self) -> str:
        return self._modelo
    
    def get_estado(self) -> bool:
        return self._estado
    
    def get_consumo_energetico(self) -> float:
        return self._consumo_energetico
    
    def set_consumo_energetico(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El consumo energético no puede ser negativo")
        self._consumo_energetico = valor
    
    def get_fecha_creacion(self) -> datetime:
        return self._fecha_creacion
    
    def get_automatizaciones(self):
        return self._automatizaciones.copy()
    
    @abstractmethod
    def encender(self) -> bool:
        pass
    
    @abstractmethod
    def apagar(self) -> bool:
        pass
    
    def crear_dispositivo(self) -> bool:
        try:
            print(f"Dispositivo {self._nombre} creado exitosamente")
            return True
        except Exception as e:
            print(f"Error al crear dispositivo: {e}")
            return False
    
    def buscar_por_nombre(self, nombre_buscar: str) -> bool:
        try:
            return self._nombre.lower() == nombre_buscar.lower()
        except Exception as e:
            print(f"Error al buscar por nombre: {e}")
            return False
    
    def listar_dispositivos(self):
        try:
            return {
                'id': self._id_dispositivo,
                'nombre': self._nombre,
                'tipo': self._tipo,
                'marca': self._marca,
                'modelo': self._modelo,
                'estado': 'Encendido' if self._estado else 'Apagado',
                'consumo_energetico': self._consumo_energetico,
                'fecha_creacion': self._fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            print(f"Error al listar dispositivos: {e}")
            return {}
    
    def eliminar_por_nombre(self) -> bool:
        try:
            print(f"Dispositivo {self._nombre} eliminado exitosamente")
            return True
        except Exception as e:
            print(f"Error al eliminar dispositivo: {e}")
            return False
    
    def devolver_lista_de_dispositivos(self):
        try:
            return [self.listar_dispositivos()]
        except Exception as e:
            print(f"Error al devolver lista de dispositivos: {e}")
            return []
    
    def __str__(self) -> str:
        return f"{self._tipo}: {self._nombre} ({self._marca} {self._modelo})"
