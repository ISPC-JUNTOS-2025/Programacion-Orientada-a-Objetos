"""
Tests para la clase DispositivoDigital
Implementados siguiendo principios de TDD (Test-Driven Development)
"""
import pytest
from datetime import datetime
from enums import TipoDispositivoDigital
from entidades.DispositivoDigital import DispositivoDigital


class TestDispositivoDigital:
    """Clase de tests para DispositivoDigital siguiendo principios TDD"""
    
    def test_dispositivo_digital_creacion_exitosa(self):
        """Test: Un dispositivo digital se puede crear con todos los atributos requeridos"""
        # Arrange
        id_dispositivo = 1
        nombre = "Smart TV"
        marca = "Samsung"
        modelo = "QLED 55"
        consumo_energetico = 150.5
        tipo_dispositivo = TipoDispositivoDigital.TELEVISION
        
        # Act
        dispositivo = DispositivoDigital(id_dispositivo, nombre, marca, modelo, 
                                       consumo_energetico, tipo_dispositivo)
        
        # Assert
        assert dispositivo.get_id_dispositivo() == id_dispositivo
        assert dispositivo.get_nombre() == nombre
        assert dispositivo.get_tipo() == "Dispositivo Digital"
        assert dispositivo.get_marca() == marca
        assert dispositivo.get_modelo() == modelo
        assert dispositivo.get_consumo_energetico() == consumo_energetico
        assert dispositivo.get_tipo_dispositivo() == tipo_dispositivo
        assert dispositivo.get_estado() is False
        assert isinstance(dispositivo.get_fecha_creacion(), datetime)
    
    def test_dispositivo_digital_get_tipo_dispositivo(self):
        """Test: get_tipo_dispositivo retorna el tipo correcto"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        
        # Act
        tipo = dispositivo.get_tipo_dispositivo()
        
        # Assert
        assert tipo == TipoDispositivoDigital.TELEVISION
    
    def test_dispositivo_digital_encender_apagado(self):
        """Test: encender funciona cuando el dispositivo está apagado"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        assert dispositivo.get_estado() is False
        
        # Act
        resultado = dispositivo.encender()
        
        # Assert
        assert resultado is True
        assert dispositivo.get_estado() is True
    
    def test_dispositivo_digital_encender_ya_encendido(self):
        """Test: encender retorna False cuando el dispositivo ya está encendido"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        dispositivo.encender()
        assert dispositivo.get_estado() is True
        
        # Act
        resultado = dispositivo.encender()
        
        # Assert
        assert resultado is False
        assert dispositivo.get_estado() is True
    
    def test_dispositivo_digital_apagar_encendido(self):
        """Test: apagar funciona cuando el dispositivo está encendido"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        dispositivo.encender()
        assert dispositivo.get_estado() is True
        
        # Act
        resultado = dispositivo.apagar()
        
        # Assert
        assert resultado is True
        assert dispositivo.get_estado() is False
    
    def test_dispositivo_digital_apagar_ya_apagado(self):
        """Test: apagar retorna False cuando el dispositivo ya está apagado"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        assert dispositivo.get_estado() is False
        
        # Act
        resultado = dispositivo.apagar()
        
        # Assert
        assert resultado is False
        assert dispositivo.get_estado() is False
    
    def test_dispositivo_digital_reiniciar_encendido(self):
        """Test: reiniciar funciona cuando el dispositivo está encendido"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        dispositivo.encender()
        assert dispositivo.get_estado() is True
        
        # Act
        resultado = dispositivo.reiniciar()
        
        # Assert
        assert resultado is True
        assert dispositivo.get_estado() is True  # Debe quedar encendido después del reinicio
    
    def test_dispositivo_digital_reiniciar_apagado(self):
        """Test: reiniciar retorna False cuando el dispositivo está apagado"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        assert dispositivo.get_estado() is False
        
        # Act
        resultado = dispositivo.reiniciar()
        
        # Assert
        assert resultado is False
        assert dispositivo.get_estado() is False
    
    def test_dispositivo_digital_ver_informacion_apagado(self):
        """Test: ver_informacion retorna información correcta cuando está apagado"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        
        # Act
        info = dispositivo.ver_informacion()
        
        # Assert
        assert isinstance(info, str)
        assert "Dispositivo Digital: Smart TV" in info
        assert "Tipo: TELEVISION" in info
        assert "Marca: Samsung" in info
        assert "Modelo: QLED 55" in info
        assert "Estado: Apagado" in info
        assert "Consumo: 150.5W" in info
    
    def test_dispositivo_digital_ver_informacion_encendido(self):
        """Test: ver_informacion retorna información correcta cuando está encendido"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        dispositivo.encender()
        
        # Act
        info = dispositivo.ver_informacion()
        
        # Assert
        assert isinstance(info, str)
        assert "Estado: Encendido" in info
    
    def test_dispositivo_digital_herencia_de_dispositivo(self):
        """Test: DispositivoDigital hereda correctamente de Dispositivo"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        
        # Act & Assert
        # Verificar que tiene todos los métodos de la clase padre
        assert hasattr(dispositivo, 'get_id_dispositivo')
        assert hasattr(dispositivo, 'get_nombre')
        assert hasattr(dispositivo, 'get_tipo')
        assert hasattr(dispositivo, 'get_marca')
        assert hasattr(dispositivo, 'get_modelo')
        assert hasattr(dispositivo, 'get_estado')
        assert hasattr(dispositivo, 'get_consumo_energetico')
        assert hasattr(dispositivo, 'get_fecha_creacion')
        assert hasattr(dispositivo, 'get_automatizaciones')
        assert hasattr(dispositivo, 'crear_dispositivo')
        assert hasattr(dispositivo, 'buscar_por_nombre')
        assert hasattr(dispositivo, 'listar_dispositivos')
        assert hasattr(dispositivo, 'eliminar_por_nombre')
        assert hasattr(dispositivo, 'devolver_lista_de_dispositivos')
        assert hasattr(dispositivo, '__str__')
        
        # Verificar que implementa los métodos abstractos
        assert hasattr(dispositivo, 'encender')
        assert hasattr(dispositivo, 'apagar')
        
        # Verificar métodos específicos de DispositivoDigital
        assert hasattr(dispositivo, 'get_tipo_dispositivo')
        assert hasattr(dispositivo, 'reiniciar')
        assert hasattr(dispositivo, 'ver_informacion')
    
    def test_dispositivo_digital_diferentes_tipos(self):
        """Test: Se pueden crear dispositivos digitales de diferentes tipos"""
        # Arrange & Act
        tv = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                              150.5, TipoDispositivoDigital.TELEVISION)
        tablet = DispositivoDigital(2, "Tablet", "Apple", "iPad Pro", 
                                  50.0, TipoDispositivoDigital.TABLET)
        smartphone = DispositivoDigital(3, "Smartphone", "Samsung", "Galaxy S21", 
                                      25.0, TipoDispositivoDigital.SMARTPHONE)
        
        # Assert
        assert tv.get_tipo_dispositivo() == TipoDispositivoDigital.TELEVISION
        assert tablet.get_tipo_dispositivo() == TipoDispositivoDigital.TABLET
        assert smartphone.get_tipo_dispositivo() == TipoDispositivoDigital.SMARTPHONE
    
    def test_dispositivo_digital_ver_informacion_con_diferentes_tipos(self):
        """Test: ver_informacion muestra el tipo correcto para diferentes dispositivos"""
        # Arrange
        tv = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                              150.5, TipoDispositivoDigital.TELEVISION)
        tablet = DispositivoDigital(2, "Tablet", "Apple", "iPad Pro", 
                                  50.0, TipoDispositivoDigital.TABLET)
        
        # Act
        info_tv = tv.ver_informacion()
        info_tablet = tablet.ver_informacion()
        
        # Assert
        assert "Tipo: TELEVISION" in info_tv
        assert "Tipo: TABLET" in info_tablet
    
    def test_dispositivo_digital_reiniciar_secuencia_completa(self):
        """Test: reiniciar ejecuta la secuencia completa de apagar y encender"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        dispositivo.encender()
        assert dispositivo.get_estado() is True
        
        # Act
        resultado = dispositivo.reiniciar()
        
        # Assert
        assert resultado is True
        # El dispositivo debe quedar encendido después del reinicio
        assert dispositivo.get_estado() is True
    
    def test_dispositivo_digital_metodos_heredados_funcionan(self):
        """Test: Los métodos heredados de Dispositivo funcionan correctamente"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        
        # Act & Assert
        # Probar crear_dispositivo
        assert dispositivo.crear_dispositivo() is True
        
        # Probar buscar_por_nombre
        assert dispositivo.buscar_por_nombre("Smart TV") is True
        assert dispositivo.buscar_por_nombre("smart tv") is True  # Case insensitive
        assert dispositivo.buscar_por_nombre("Other Device") is False
        
        # Probar listar_dispositivos
        lista = dispositivo.listar_dispositivos()
        assert isinstance(lista, dict)
        assert lista['nombre'] == "Smart TV"
        assert lista['tipo'] == "Dispositivo Digital"
        
        # Probar eliminar_por_nombre
        assert dispositivo.eliminar_por_nombre() is True
        
        # Probar devolver_lista_de_dispositivos
        lista_dispositivos = dispositivo.devolver_lista_de_dispositivos()
        assert isinstance(lista_dispositivos, list)
        assert len(lista_dispositivos) == 1
    
    def test_dispositivo_digital_str_representacion(self):
        """Test: __str__ retorna representación correcta del dispositivo digital"""
        # Arrange
        dispositivo = DispositivoDigital(1, "Smart TV", "Samsung", "QLED 55", 
                                       150.5, TipoDispositivoDigital.TELEVISION)
        
        # Act
        resultado = str(dispositivo)
        
        # Assert
        assert "Dispositivo Digital" in resultado
        assert "Smart TV" in resultado
        assert "Samsung" in resultado
        assert "QLED 55" in resultado
