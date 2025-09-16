"""
Tests para la clase Luz
Implementados siguiendo principios de TDD (Test-Driven Development)
"""
import pytest
from datetime import datetime
from entidades.Luz import Luz


class TestLuz:
    """Clase de tests para Luz siguiendo principios TDD"""
    
    def test_luz_creacion_exitosa(self):
        """Test: Una luz se puede crear con todos los atributos requeridos"""
        # Arrange
        id_dispositivo = 1
        nombre = "Luz Sala"
        marca = "Philips"
        modelo = "Hue"
        consumo_energetico = 50.0
        intensidad = 75
        regulable = True
        
        # Act
        luz = Luz(id_dispositivo, nombre, marca, modelo, consumo_energetico, intensidad, regulable)
        
        # Assert
        assert luz.get_id_dispositivo() == id_dispositivo
        assert luz.get_nombre() == nombre
        assert luz.get_tipo() == "Luz"
        assert luz.get_marca() == marca
        assert luz.get_modelo() == modelo
        assert luz.get_consumo_energetico() == consumo_energetico
        assert luz.get_intensidad() == intensidad
        assert luz.get_regulable() == regulable
        assert luz.get_estado() is False
        assert isinstance(luz.get_fecha_creacion(), datetime)
    
    def test_luz_creacion_intensidad_default(self):
        """Test: Una luz se crea con intensidad por defecto de 50"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0)
        
        # Assert
        assert luz.get_intensidad() == 50
    
    def test_luz_creacion_regulable_default(self):
        """Test: Una luz se crea como regulable por defecto"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0)
        
        # Assert
        assert luz.get_regulable() is True
    
    def test_luz_creacion_intensidad_limite_inferior(self):
        """Test: Una luz se crea con intensidad mínima de 0"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, -10)
        
        # Assert
        assert luz.get_intensidad() == 0
    
    def test_luz_creacion_intensidad_limite_superior(self):
        """Test: Una luz se crea con intensidad máxima de 100"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 150)
        
        # Assert
        assert luz.get_intensidad() == 100
    
    def test_luz_getters_basicos(self):
        """Test: Los getters básicos funcionan correctamente"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75, True)
        
        # Act & Assert
        assert luz.get_intensidad() == 75
        assert luz.get_regulable() is True
    
    def test_luz_encender_apagado(self):
        """Test: encender funciona cuando la luz está apagada"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75)
        assert luz.get_estado() is False
        
        # Act
        resultado = luz.encender()
        
        # Assert
        assert resultado is True
        assert luz.get_estado() is True
    
    def test_luz_encender_ya_encendida(self):
        """Test: encender retorna False cuando la luz ya está encendida"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75)
        luz.encender()
        assert luz.get_estado() is True
        
        # Act
        resultado = luz.encender()
        
        # Assert
        assert resultado is False
        assert luz.get_estado() is True
    
    def test_luz_apagar_encendida(self):
        """Test: apagar funciona cuando la luz está encendida"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75)
        luz.encender()
        assert luz.get_estado() is True
        
        # Act
        resultado = luz.apagar()
        
        # Assert
        assert resultado is True
        assert luz.get_estado() is False
    
    def test_luz_apagar_ya_apagada(self):
        """Test: apagar retorna False cuando la luz ya está apagada"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75)
        assert luz.get_estado() is False
        
        # Act
        resultado = luz.apagar()
        
        # Assert
        assert resultado is False
        assert luz.get_estado() is False
    
    def test_luz_regular_intensidad_valida(self):
        """Test: regular_intensidad funciona con intensidad válida"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 50, True)
        
        # Act
        resultado = luz.regular_intensidad(80)
        
        # Assert
        assert resultado is True
        assert luz.get_intensidad() == 80
    
    def test_luz_regular_intensidad_minima(self):
        """Test: regular_intensidad acepta intensidad mínima (0)"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 50, True)
        
        # Act
        resultado = luz.regular_intensidad(0)
        
        # Assert
        assert resultado is True
        assert luz.get_intensidad() == 0
    
    def test_luz_regular_intensidad_maxima(self):
        """Test: regular_intensidad acepta intensidad máxima (100)"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 50, True)
        
        # Act
        resultado = luz.regular_intensidad(100)
        
        # Assert
        assert resultado is True
        assert luz.get_intensidad() == 100
    
    def test_luz_regular_intensidad_muy_baja(self):
        """Test: regular_intensidad retorna False con intensidad muy baja"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 50, True)
        
        # Act
        resultado = luz.regular_intensidad(-10)
        
        # Assert
        assert resultado is False
        assert luz.get_intensidad() == 50  # No cambia
    
    def test_luz_regular_intensidad_muy_alta(self):
        """Test: regular_intensidad retorna False con intensidad muy alta"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 50, True)
        
        # Act
        resultado = luz.regular_intensidad(150)
        
        # Assert
        assert resultado is False
        assert luz.get_intensidad() == 50  # No cambia
    
    def test_luz_regular_intensidad_no_regulable(self):
        """Test: regular_intensidad retorna False cuando no es regulable"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 50, False)
        
        # Act
        resultado = luz.regular_intensidad(80)
        
        # Assert
        assert resultado is False
        assert luz.get_intensidad() == 50  # No cambia
    
    def test_luz_regular_intensidad_encendida(self):
        """Test: regular_intensidad funciona cuando está encendida"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 50, True)
        luz.encender()
        
        # Act
        resultado = luz.regular_intensidad(80)
        
        # Assert
        assert resultado is True
        assert luz.get_intensidad() == 80
    
    def test_luz_regular_intensidad_apagada(self):
        """Test: regular_intensidad funciona cuando está apagada"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 50, True)
        
        # Act
        resultado = luz.regular_intensidad(80)
        
        # Assert
        assert resultado is True
        assert luz.get_intensidad() == 80
    
    def test_luz_herencia_de_dispositivo(self):
        """Test: Luz hereda correctamente de Dispositivo"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75, True)
        
        # Act & Assert
        # Verificar que tiene todos los métodos de la clase padre
        assert hasattr(luz, 'get_id_dispositivo')
        assert hasattr(luz, 'get_nombre')
        assert hasattr(luz, 'get_tipo')
        assert hasattr(luz, 'get_marca')
        assert hasattr(luz, 'get_modelo')
        assert hasattr(luz, 'get_estado')
        assert hasattr(luz, 'get_consumo_energetico')
        assert hasattr(luz, 'get_fecha_creacion')
        assert hasattr(luz, 'get_automatizaciones')
        assert hasattr(luz, 'crear_dispositivo')
        assert hasattr(luz, 'buscar_por_nombre')
        assert hasattr(luz, 'listar_dispositivos')
        assert hasattr(luz, 'eliminar_por_nombre')
        assert hasattr(luz, 'devolver_lista_de_dispositivos')
        assert hasattr(luz, '__str__')
        
        # Verificar que implementa los métodos abstractos
        assert hasattr(luz, 'encender')
        assert hasattr(luz, 'apagar')
        
        # Verificar métodos específicos de Luz
        assert hasattr(luz, 'get_intensidad')
        assert hasattr(luz, 'get_regulable')
        assert hasattr(luz, 'regular_intensidad')
    
    def test_luz_metodos_heredados_funcionan(self):
        """Test: Los métodos heredados de Dispositivo funcionan correctamente"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75, True)
        
        # Act & Assert
        # Probar crear_dispositivo
        assert luz.crear_dispositivo() is True
        
        # Probar buscar_por_nombre
        assert luz.buscar_por_nombre("Luz Sala") is True
        assert luz.buscar_por_nombre("luz sala") is True  # Case insensitive
        assert luz.buscar_por_nombre("Other Device") is False
        
        # Probar listar_dispositivos
        lista = luz.listar_dispositivos()
        assert isinstance(lista, dict)
        assert lista['nombre'] == "Luz Sala"
        assert lista['tipo'] == "Luz"
        
        # Probar eliminar_por_nombre
        assert luz.eliminar_por_nombre() is True
        
        # Probar devolver_lista_de_dispositivos
        lista_dispositivos = luz.devolver_lista_de_dispositivos()
        assert isinstance(lista_dispositivos, list)
        assert len(lista_dispositivos) == 1
    
    def test_luz_str_representacion(self):
        """Test: __str__ retorna representación correcta de la luz"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75, True)
        
        # Act
        resultado = str(luz)
        
        # Assert
        assert "Luz" in resultado
        assert "Luz Sala" in resultado
        assert "Philips" in resultado
        assert "Hue" in resultado
    
    def test_luz_rango_intensidades_completo(self):
        """Test: regular_intensidad funciona en todo el rango válido"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 0, True)
        
        # Act & Assert - Probar todo el rango válido
        for intensidad in range(0, 101):
            resultado = luz.regular_intensidad(intensidad)
            assert resultado is True
            assert luz.get_intensidad() == intensidad
    
    def test_luz_estado_inicial_correcto(self):
        """Test: El estado inicial de la luz es correcto"""
        # Arrange
        luz = Luz(1, "Luz Sala", "Philips", "Hue", 50.0, 75, True)
        
        # Assert
        assert luz.get_estado() is False  # Apagada
        assert luz.get_intensidad() == 75
        assert luz.get_regulable() is True
        assert luz.get_tipo() == "Luz"
        assert isinstance(luz.get_fecha_creacion(), datetime)
    
    def test_luz_diferentes_configuraciones(self):
        """Test: Se pueden crear luces con diferentes configuraciones"""
        # Arrange & Act
        luz_regulable = Luz(1, "Luz Regulable", "Philips", "Hue", 50.0, 75, True)
        luz_fija = Luz(2, "Luz Fija", "Osram", "LED", 30.0, 100, False)
        
        # Assert
        assert luz_regulable.get_regulable() is True
        assert luz_fija.get_regulable() is False
        
        # La luz regulable puede cambiar intensidad
        assert luz_regulable.regular_intensidad(50) is True
        
        # La luz fija no puede cambiar intensidad
        assert luz_fija.regular_intensidad(50) is False
