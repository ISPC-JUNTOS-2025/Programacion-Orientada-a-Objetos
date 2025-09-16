"""
Tests para la clase SensorMovimiento
Implementados siguiendo principios de TDD (Test-Driven Development)
"""
import pytest
from datetime import datetime
from entidades.SensorMovimiento import SensorMovimiento


class TestSensorMovimiento:
    """Clase de tests para SensorMovimiento siguiendo principios TDD"""
    
    def test_sensor_movimiento_creacion_exitosa(self):
        """Test: Un sensor de movimiento se puede crear con todos los atributos requeridos"""
        # Arrange
        id_dispositivo = 1
        nombre = "Sensor Principal"
        marca = "Hikvision"
        modelo = "DS-PIR-1"
        consumo_energetico = 15.0
        
        # Act
        sensor = SensorMovimiento(id_dispositivo, nombre, marca, modelo, consumo_energetico)
        
        # Assert
        assert sensor.get_id_dispositivo() == id_dispositivo
        assert sensor.get_nombre() == nombre
        assert sensor.get_tipo() == "Sensor de Movimiento"
        assert sensor.get_marca() == marca
        assert sensor.get_modelo() == modelo
        assert sensor.get_consumo_energetico() == consumo_energetico
        assert sensor.get_estado_activo() is False
        assert sensor.get_ultima_deteccion() is None
        assert sensor.get_registro_de_intrusos() == []
        assert sensor.get_estado() is False
        assert isinstance(sensor.get_fecha_creacion(), datetime)
    
    def test_sensor_movimiento_getters_basicos(self):
        """Test: Los getters básicos funcionan correctamente"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        
        # Act & Assert
        assert sensor.get_estado_activo() is False
        assert sensor.get_ultima_deteccion() is None
        assert isinstance(sensor.get_registro_de_intrusos(), list)
        assert len(sensor.get_registro_de_intrusos()) == 0
    
    def test_sensor_movimiento_encender_apagado(self):
        """Test: encender funciona cuando el sensor está apagado"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        assert sensor.get_estado() is False
        assert sensor.get_estado_activo() is False
        
        # Act
        resultado = sensor.encender()
        
        # Assert
        assert resultado is True
        assert sensor.get_estado() is True
        assert sensor.get_estado_activo() is True
    
    def test_sensor_movimiento_encender_ya_encendido(self):
        """Test: encender retorna False cuando el sensor ya está encendido"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        sensor.encender()
        assert sensor.get_estado() is True
        assert sensor.get_estado_activo() is True
        
        # Act
        resultado = sensor.encender()
        
        # Assert
        assert resultado is False
        assert sensor.get_estado() is True
        assert sensor.get_estado_activo() is True
    
    def test_sensor_movimiento_apagar_encendido(self):
        """Test: apagar funciona cuando el sensor está encendido"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        sensor.encender()
        assert sensor.get_estado() is True
        assert sensor.get_estado_activo() is True
        
        # Act
        resultado = sensor.apagar()
        
        # Assert
        assert resultado is True
        assert sensor.get_estado() is False
        assert sensor.get_estado_activo() is False
    
    def test_sensor_movimiento_apagar_ya_apagado(self):
        """Test: apagar retorna False cuando el sensor ya está apagado"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        assert sensor.get_estado() is False
        assert sensor.get_estado_activo() is False
        
        # Act
        resultado = sensor.apagar()
        
        # Assert
        assert resultado is False
        assert sensor.get_estado() is False
        assert sensor.get_estado_activo() is False
    
    def test_sensor_movimiento_detectar_movimiento_activo(self):
        """Test: detectar_movimiento funciona cuando el sensor está activo"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        sensor.encender()
        assert sensor.get_estado_activo() is True
        
        # Act
        resultado = sensor.detectar_movimiento(True)
        
        # Assert
        assert resultado is True
        assert sensor.get_ultima_deteccion() is not None
        assert isinstance(sensor.get_ultima_deteccion(), datetime)
    
    def test_sensor_movimiento_detectar_movimiento_inactivo(self):
        """Test: detectar_movimiento retorna False cuando el sensor está inactivo"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        assert sensor.get_estado_activo() is False
        
        # Act
        resultado = sensor.detectar_movimiento(True)
        
        # Assert
        assert resultado is False
        assert sensor.get_ultima_deteccion() is None
    
    def test_sensor_movimiento_detectar_sin_movimiento(self):
        """Test: detectar_movimiento retorna False cuando no hay movimiento"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        sensor.encender()
        assert sensor.get_estado_activo() is True
        
        # Act
        resultado = sensor.detectar_movimiento(False)
        
        # Assert
        assert resultado is False
        assert sensor.get_ultima_deteccion() is None
    
    def test_sensor_movimiento_registrar_intruso(self):
        """Test: registrar_intruso funciona correctamente"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        hora = datetime.now()
        descripcion = "Movimiento detectado en la entrada"
        
        # Act
        sensor.registrar_intruso(hora, descripcion)
        
        # Assert
        registro = sensor.get_registro_de_intrusos()
        assert len(registro) == 1
        assert registro[0]['hora'] == hora
        assert registro[0]['descripcion'] == descripcion
        assert registro[0]['sensor'] == "Sensor Test"
    
    def test_sensor_movimiento_registrar_multiples_intrusos(self):
        """Test: Se pueden registrar múltiples intrusiones"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        hora1 = datetime.now()
        hora2 = datetime.now()
        
        # Act
        sensor.registrar_intruso(hora1, "Primera intrusión")
        sensor.registrar_intruso(hora2, "Segunda intrusión")
        
        # Assert
        registro = sensor.get_registro_de_intrusos()
        assert len(registro) == 2
        assert registro[0]['descripcion'] == "Primera intrusión"
        assert registro[1]['descripcion'] == "Segunda intrusión"
    
    def test_sensor_movimiento_registrar_anomalia(self):
        """Test: registrar_anomalia funciona correctamente"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        tipo = "Falla de energía"
        descripcion = "Sensor perdió conexión"
        
        # Act
        sensor.registrar_anomalia(tipo, descripcion)
        
        # Assert
        registro = sensor.get_registro_de_intrusos()
        assert len(registro) == 1
        assert registro[0]['tipo'] == tipo
        assert registro[0]['descripcion'] == descripcion
        assert registro[0]['sensor'] == "Sensor Test"
        assert 'hora' in registro[0]
    
    def test_sensor_movimiento_enviar_alerta(self):
        """Test: enviar_alerta funciona correctamente"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        mensaje = "Intruso detectado en zona restringida"
        
        # Act
        sensor.enviar_alerta(mensaje)
        
        # Assert
        # No hay valor de retorno, solo verificar que no lanza excepción
        assert True  # Si llegamos aquí, no hubo excepción
    
    def test_sensor_movimiento_herencia_de_dispositivo(self):
        """Test: SensorMovimiento hereda correctamente de Dispositivo"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        
        # Act & Assert
        # Verificar que tiene todos los métodos de la clase padre
        assert hasattr(sensor, 'get_id_dispositivo')
        assert hasattr(sensor, 'get_nombre')
        assert hasattr(sensor, 'get_tipo')
        assert hasattr(sensor, 'get_marca')
        assert hasattr(sensor, 'get_modelo')
        assert hasattr(sensor, 'get_estado')
        assert hasattr(sensor, 'get_consumo_energetico')
        assert hasattr(sensor, 'get_fecha_creacion')
        assert hasattr(sensor, 'get_automatizaciones')
        assert hasattr(sensor, 'crear_dispositivo')
        assert hasattr(sensor, 'buscar_por_nombre')
        assert hasattr(sensor, 'listar_dispositivos')
        assert hasattr(sensor, 'eliminar_por_nombre')
        assert hasattr(sensor, 'devolver_lista_de_dispositivos')
        assert hasattr(sensor, '__str__')
        
        # Verificar que implementa los métodos abstractos
        assert hasattr(sensor, 'encender')
        assert hasattr(sensor, 'apagar')
        
        # Verificar métodos específicos de SensorMovimiento
        assert hasattr(sensor, 'get_estado_activo')
        assert hasattr(sensor, 'get_ultima_deteccion')
        assert hasattr(sensor, 'get_registro_de_intrusos')
        assert hasattr(sensor, 'detectar_movimiento')
        assert hasattr(sensor, 'registrar_intruso')
        assert hasattr(sensor, 'registrar_anomalia')
        assert hasattr(sensor, 'enviar_alerta')
    
    def test_sensor_movimiento_metodos_heredados_funcionan(self):
        """Test: Los métodos heredados de Dispositivo funcionan correctamente"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        
        # Act & Assert
        # Probar crear_dispositivo
        assert sensor.crear_dispositivo() is True
        
        # Probar buscar_por_nombre
        assert sensor.buscar_por_nombre("Sensor Test") is True
        assert sensor.buscar_por_nombre("sensor test") is True  # Case insensitive
        assert sensor.buscar_por_nombre("Other Device") is False
        
        # Probar listar_dispositivos
        lista = sensor.listar_dispositivos()
        assert isinstance(lista, dict)
        assert lista['nombre'] == "Sensor Test"
        assert lista['tipo'] == "Sensor de Movimiento"
        
        # Probar eliminar_por_nombre
        assert sensor.eliminar_por_nombre() is True
        
        # Probar devolver_lista_de_dispositivos
        lista_dispositivos = sensor.devolver_lista_de_dispositivos()
        assert isinstance(lista_dispositivos, list)
        assert len(lista_dispositivos) == 1
    
    def test_sensor_movimiento_str_representacion(self):
        """Test: __str__ retorna representación correcta del sensor"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        
        # Act
        resultado = str(sensor)
        
        # Assert
        assert "Sensor de Movimiento" in resultado
        assert "Sensor Test" in resultado
        assert "Hikvision" in resultado
        assert "DS-PIR-1" in resultado
    
    def test_sensor_movimiento_estado_inicial_correcto(self):
        """Test: El estado inicial del sensor es correcto"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        
        # Assert
        assert sensor.get_estado() is False  # Apagado
        assert sensor.get_estado_activo() is False  # Inactivo
        assert sensor.get_ultima_deteccion() is None
        assert sensor.get_registro_de_intrusos() == []
        assert sensor.get_tipo() == "Sensor de Movimiento"
        assert isinstance(sensor.get_fecha_creacion(), datetime)
    
    def test_sensor_movimiento_registro_copia_segura(self):
        """Test: get_registro_de_intrusos retorna una copia de la lista"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        sensor.registrar_intruso(datetime.now(), "Test")
        
        # Act
        registro1 = sensor.get_registro_de_intrusos()
        registro2 = sensor.get_registro_de_intrusos()
        
        # Assert
        assert registro1 is not registro2  # Diferentes objetos
        assert registro1 == registro2  # Mismo contenido
    
    def test_sensor_movimiento_secuencia_deteccion_completa(self):
        """Test: Secuencia completa de detección funciona correctamente"""
        # Arrange
        sensor = SensorMovimiento(1, "Sensor Test", "Hikvision", "DS-PIR-1", 15.0)
        
        # Act & Assert
        # 1. Encender sensor
        assert sensor.encender() is True
        assert sensor.get_estado() is True
        assert sensor.get_estado_activo() is True
        
        # 2. Detectar movimiento
        assert sensor.detectar_movimiento(True) is True
        assert sensor.get_ultima_deteccion() is not None
        
        # 3. Registrar intrusión
        sensor.registrar_intruso(sensor.get_ultima_deteccion(), "Intrusión detectada")
        assert len(sensor.get_registro_de_intrusos()) == 1
        
        # 4. Enviar alerta
        sensor.enviar_alerta("Intruso en zona restringida")
        
        # 5. Apagar sensor
        assert sensor.apagar() is True
        assert sensor.get_estado() is False
        assert sensor.get_estado_activo() is False
