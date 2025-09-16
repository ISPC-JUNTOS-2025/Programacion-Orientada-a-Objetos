"""
Tests para la clase Camara
Implementados siguiendo principios de TDD (Test-Driven Development)
"""
import pytest
from datetime import datetime
from entidades.Camara import Camara


class TestCamara:
    """Clase de tests para Camara siguiendo principios TDD"""
    
    def test_camara_creacion_exitosa(self):
        """Test: Una cámara se puede crear con todos los atributos requeridos"""
        # Arrange
        id_dispositivo = 1
        nombre = "Cámara Principal"
        marca = "Hikvision"
        modelo = "DS-2CD2143G0"
        consumo_energetico = 25.0
        resolucion = "1080p"
        vision_nocturna = True
        almacenamiento_local = True
        
        # Act
        camara = Camara(id_dispositivo, nombre, marca, modelo, consumo_energetico, 
                       resolucion, vision_nocturna, almacenamiento_local)
        
        # Assert
        assert camara.get_id_dispositivo() == id_dispositivo
        assert camara.get_nombre() == nombre
        assert camara.get_tipo() == "Cámara"
        assert camara.get_marca() == marca
        assert camara.get_modelo() == modelo
        assert camara.get_consumo_energetico() == consumo_energetico
        assert camara.get_resolucion() == resolucion
        assert camara.get_vision_nocturna() == vision_nocturna
        assert camara.get_almacenamiento_local() == almacenamiento_local
        assert camara.get_grabacion() is False
        assert camara.get_estado() is False
        assert isinstance(camara.get_fecha_creacion(), datetime)
    
    def test_camara_creacion_valores_default(self):
        """Test: Una cámara se crea con valores por defecto correctos"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        
        # Assert
        assert camara.get_resolucion() == "1080p"
        assert camara.get_vision_nocturna() is True
        assert camara.get_almacenamiento_local() is True
        assert camara.get_grabacion() is False
    
    def test_camara_getters_basicos(self):
        """Test: Los getters básicos funcionan correctamente"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0, 
                       "4K", False, False)
        
        # Act & Assert
        assert camara.get_resolucion() == "4K"
        assert camara.get_vision_nocturna() is False
        assert camara.get_almacenamiento_local() is False
        assert camara.get_grabacion() is False
    
    def test_camara_encender_apagada(self):
        """Test: encender funciona cuando la cámara está apagada"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        assert camara.get_estado() is False
        
        # Act
        resultado = camara.encender()
        
        # Assert
        assert resultado is True
        assert camara.get_estado() is True
    
    def test_camara_encender_ya_encendida(self):
        """Test: encender retorna False cuando la cámara ya está encendida"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        camara.encender()
        assert camara.get_estado() is True
        
        # Act
        resultado = camara.encender()
        
        # Assert
        assert resultado is False
        assert camara.get_estado() is True
    
    def test_camara_apagar_encendida(self):
        """Test: apagar funciona cuando la cámara está encendida"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        camara.encender()
        assert camara.get_estado() is True
        
        # Act
        resultado = camara.apagar()
        
        # Assert
        assert resultado is True
        assert camara.get_estado() is False
    
    def test_camara_apagar_ya_apagada(self):
        """Test: apagar retorna False cuando la cámara ya está apagada"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        assert camara.get_estado() is False
        
        # Act
        resultado = camara.apagar()
        
        # Assert
        assert resultado is False
        assert camara.get_estado() is False
    
    def test_camara_grabar_encendida(self):
        """Test: grabar funciona cuando la cámara está encendida"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        camara.encender()
        assert camara.get_estado() is True
        assert camara.get_grabacion() is False
        
        # Act
        resultado = camara.grabar()
        
        # Assert
        assert resultado is True
        assert camara.get_grabacion() is True
    
    def test_camara_grabar_apagada(self):
        """Test: grabar retorna False cuando la cámara está apagada"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        assert camara.get_estado() is False
        
        # Act
        resultado = camara.grabar()
        
        # Assert
        assert resultado is False
        assert camara.get_grabacion() is False
    
    def test_camara_grabar_ya_grabando(self):
        """Test: grabar retorna False cuando ya está grabando"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        camara.encender()
        camara.grabar()
        assert camara.get_grabacion() is True
        
        # Act
        resultado = camara.grabar()
        
        # Assert
        assert resultado is False
        assert camara.get_grabacion() is True
    
    def test_camara_detener_grabacion_grabando(self):
        """Test: detener_grabacion funciona cuando está grabando"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        camara.encender()
        camara.grabar()
        assert camara.get_grabacion() is True
        
        # Act
        resultado = camara.detener_grabacion()
        
        # Assert
        assert resultado is True
        assert camara.get_grabacion() is False
    
    def test_camara_detener_grabacion_no_grabando(self):
        """Test: detener_grabacion retorna False cuando no está grabando"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        assert camara.get_grabacion() is False
        
        # Act
        resultado = camara.detener_grabacion()
        
        # Assert
        assert resultado is False
        assert camara.get_grabacion() is False
    
    def test_camara_apagar_detiene_grabacion(self):
        """Test: apagar detiene la grabación automáticamente"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        camara.encender()
        camara.grabar()
        assert camara.get_grabacion() is True
        
        # Act
        resultado = camara.apagar()
        
        # Assert
        assert resultado is True
        assert camara.get_estado() is False
        assert camara.get_grabacion() is False  # Debe detener la grabación
    
    def test_camara_herencia_de_dispositivo(self):
        """Test: Camara hereda correctamente de Dispositivo"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        
        # Act & Assert
        # Verificar que tiene todos los métodos de la clase padre
        assert hasattr(camara, 'get_id_dispositivo')
        assert hasattr(camara, 'get_nombre')
        assert hasattr(camara, 'get_tipo')
        assert hasattr(camara, 'get_marca')
        assert hasattr(camara, 'get_modelo')
        assert hasattr(camara, 'get_estado')
        assert hasattr(camara, 'get_consumo_energetico')
        assert hasattr(camara, 'get_fecha_creacion')
        assert hasattr(camara, 'get_automatizaciones')
        assert hasattr(camara, 'crear_dispositivo')
        assert hasattr(camara, 'buscar_por_nombre')
        assert hasattr(camara, 'listar_dispositivos')
        assert hasattr(camara, 'eliminar_por_nombre')
        assert hasattr(camara, 'devolver_lista_de_dispositivos')
        assert hasattr(camara, '__str__')
        
        # Verificar que implementa los métodos abstractos
        assert hasattr(camara, 'encender')
        assert hasattr(camara, 'apagar')
        
        # Verificar métodos específicos de Camara
        assert hasattr(camara, 'get_resolucion')
        assert hasattr(camara, 'get_vision_nocturna')
        assert hasattr(camara, 'get_grabacion')
        assert hasattr(camara, 'get_almacenamiento_local')
        assert hasattr(camara, 'grabar')
        assert hasattr(camara, 'detener_grabacion')
    
    def test_camara_metodos_heredados_funcionan(self):
        """Test: Los métodos heredados de Dispositivo funcionan correctamente"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        
        # Act & Assert
        # Probar crear_dispositivo
        assert camara.crear_dispositivo() is True
        
        # Probar buscar_por_nombre
        assert camara.buscar_por_nombre("Cámara Test") is True
        assert camara.buscar_por_nombre("cámara test") is True  # Case insensitive
        assert camara.buscar_por_nombre("Other Device") is False
        
        # Probar listar_dispositivos
        lista = camara.listar_dispositivos()
        assert isinstance(lista, dict)
        assert lista['nombre'] == "Cámara Test"
        assert lista['tipo'] == "Cámara"
        
        # Probar eliminar_por_nombre
        assert camara.eliminar_por_nombre() is True
        
        # Probar devolver_lista_de_dispositivos
        lista_dispositivos = camara.devolver_lista_de_dispositivos()
        assert isinstance(lista_dispositivos, list)
        assert len(lista_dispositivos) == 1
    
    def test_camara_str_representacion(self):
        """Test: __str__ retorna representación correcta de la cámara"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        
        # Act
        resultado = str(camara)
        
        # Assert
        assert "Cámara" in resultado
        assert "Cámara Test" in resultado
        assert "Hikvision" in resultado
        assert "DS-2CD2143G0" in resultado
    
    def test_camara_estado_inicial_correcto(self):
        """Test: El estado inicial de la cámara es correcto"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        
        # Assert
        assert camara.get_estado() is False  # Apagada
        assert camara.get_grabacion() is False  # No grabando
        assert camara.get_resolucion() == "1080p"
        assert camara.get_vision_nocturna() is True
        assert camara.get_almacenamiento_local() is True
        assert camara.get_tipo() == "Cámara"
        assert isinstance(camara.get_fecha_creacion(), datetime)
    
    def test_camara_diferentes_configuraciones(self):
        """Test: Se pueden crear cámaras con diferentes configuraciones"""
        # Arrange & Act
        camara_basica = Camara(1, "Cámara Básica", "Hikvision", "DS-2CD2143G0", 25.0)
        camara_avanzada = Camara(2, "Cámara Avanzada", "Dahua", "IPC-HFW4431R", 30.0, 
                                "4K", True, False)
        
        # Assert
        assert camara_basica.get_resolucion() == "1080p"
        assert camara_avanzada.get_resolucion() == "4K"
        
        assert camara_basica.get_vision_nocturna() is True
        assert camara_avanzada.get_vision_nocturna() is True
        
        assert camara_basica.get_almacenamiento_local() is True
        assert camara_avanzada.get_almacenamiento_local() is False
    
    def test_camara_secuencia_grabacion_completa(self):
        """Test: Secuencia completa de grabación funciona correctamente"""
        # Arrange
        camara = Camara(1, "Cámara Test", "Hikvision", "DS-2CD2143G0", 25.0)
        
        # Act & Assert
        # 1. Encender cámara
        assert camara.encender() is True
        assert camara.get_estado() is True
        assert camara.get_grabacion() is False
        
        # 2. Iniciar grabación
        assert camara.grabar() is True
        assert camara.get_grabacion() is True
        
        # 3. Intentar grabar de nuevo (debe fallar)
        assert camara.grabar() is False
        assert camara.get_grabacion() is True
        
        # 4. Detener grabación
        assert camara.detener_grabacion() is True
        assert camara.get_grabacion() is False
        
        # 5. Apagar cámara
        assert camara.apagar() is True
        assert camara.get_estado() is False
        assert camara.get_grabacion() is False
