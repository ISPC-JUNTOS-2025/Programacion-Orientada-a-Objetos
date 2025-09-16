"""
Tests para la clase LavaRopas
Implementados siguiendo principios de TDD (Test-Driven Development)
"""
import pytest
from datetime import datetime
from enums import ProgramaLavaRopas
from entidades.LavaRopas import LavaRopas


class TestLavaRopas:
    """Clase de tests para LavaRopas siguiendo principios TDD"""
    
    def test_lavaropas_creacion_exitosa(self):
        """Test: Una lavadora se puede crear con todos los atributos requeridos"""
        # Arrange
        id_dispositivo = 1
        nombre = "Lavadora Principal"
        marca = "Samsung"
        modelo = "WW90T5540AE"
        consumo_energetico = 300.0
        velocidad_max_centrifugado = 1400
        
        # Act
        lavadora = LavaRopas(id_dispositivo, nombre, marca, modelo, consumo_energetico, velocidad_max_centrifugado)
        
        # Assert
        assert lavadora.get_id_dispositivo() == id_dispositivo
        assert lavadora.get_nombre() == nombre
        assert lavadora.get_tipo() == "Lavadora"
        assert lavadora.get_marca() == marca
        assert lavadora.get_modelo() == modelo
        assert lavadora.get_consumo_energetico() == consumo_energetico
        assert lavadora.get_programa_actual() == ProgramaLavaRopas.LAVADO_RAPIDO
        assert lavadora.get_velocidad_centrifugado() == 0
        assert lavadora.get_velocidad_max_centrifugado() == velocidad_max_centrifugado
        assert lavadora.get_puerta_bloqueada() is False
        assert lavadora.get_estado() is False
        assert isinstance(lavadora.get_fecha_creacion(), datetime)
    
    def test_lavaropas_creacion_velocidad_default(self):
        """Test: Una lavadora se crea con velocidad máxima por defecto de 1200"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        
        # Assert
        assert lavadora.get_velocidad_max_centrifugado() == 1200
    
    def test_lavaropas_getters_basicos(self):
        """Test: Los getters básicos funcionan correctamente"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0, 1400)
        
        # Act & Assert
        assert lavadora.get_programa_actual() == ProgramaLavaRopas.LAVADO_RAPIDO
        assert lavadora.get_velocidad_centrifugado() == 0
        assert lavadora.get_velocidad_max_centrifugado() == 1400
        assert lavadora.get_puerta_bloqueada() is False
    
    def test_lavaropas_encender_apagada(self):
        """Test: encender funciona cuando la lavadora está apagada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        assert lavadora.get_estado() is False
        
        # Act
        resultado = lavadora.encender()
        
        # Assert
        assert resultado is True
        assert lavadora.get_estado() is True
    
    def test_lavaropas_encender_ya_encendida(self):
        """Test: encender retorna False cuando la lavadora ya está encendida"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        lavadora.encender()
        assert lavadora.get_estado() is True
        
        # Act
        resultado = lavadora.encender()
        
        # Assert
        assert resultado is False
        assert lavadora.get_estado() is True
    
    def test_lavaropas_apagar_encendida(self):
        """Test: apagar funciona cuando la lavadora está encendida"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        lavadora.encender()
        assert lavadora.get_estado() is True
        
        # Act
        resultado = lavadora.apagar()
        
        # Assert
        assert resultado is True
        assert lavadora.get_estado() is False
        assert lavadora.get_puerta_bloqueada() is False  # Debe desbloquear la puerta
    
    def test_lavaropas_apagar_ya_apagada(self):
        """Test: apagar retorna False cuando la lavadora ya está apagada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        assert lavadora.get_estado() is False
        
        # Act
        resultado = lavadora.apagar()
        
        # Assert
        assert resultado is False
        assert lavadora.get_estado() is False
    
    def test_lavaropas_seleccionar_programa_encendida(self):
        """Test: seleccionar_programa funciona cuando la lavadora está encendida"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        lavadora.encender()
        assert lavadora.get_estado() is True
        
        # Act
        resultado = lavadora.seleccionar_programa(ProgramaLavaRopas.LAVADO_NORMAL)
        
        # Assert
        assert resultado is True
        assert lavadora.get_programa_actual() == ProgramaLavaRopas.LAVADO_NORMAL
    
    def test_lavaropas_seleccionar_programa_apagada(self):
        """Test: seleccionar_programa retorna False cuando la lavadora está apagada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        assert lavadora.get_estado() is False
        
        # Act
        resultado = lavadora.seleccionar_programa(ProgramaLavaRopas.LAVADO_NORMAL)
        
        # Assert
        assert resultado is False
        assert lavadora.get_programa_actual() == ProgramaLavaRopas.LAVADO_RAPIDO  # No cambia
    
    def test_lavaropas_iniciar_lavado_encendida_puerta_desbloqueada(self):
        """Test: iniciar_lavado funciona cuando está encendida y puerta desbloqueada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        lavadora.encender()
        assert lavadora.get_estado() is True
        assert lavadora.get_puerta_bloqueada() is False
        
        # Act
        resultado = lavadora.iniciar_lavado()
        
        # Assert
        assert resultado is True
        assert lavadora.get_puerta_bloqueada() is True
    
    def test_lavaropas_iniciar_lavado_apagada(self):
        """Test: iniciar_lavado retorna False cuando la lavadora está apagada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        assert lavadora.get_estado() is False
        
        # Act
        resultado = lavadora.iniciar_lavado()
        
        # Assert
        assert resultado is False
        assert lavadora.get_puerta_bloqueada() is False
    
    def test_lavaropas_iniciar_lavado_puerta_bloqueada(self):
        """Test: iniciar_lavado retorna False cuando la puerta está bloqueada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        lavadora.encender()
        lavadora.iniciar_lavado()  # Bloquear puerta
        assert lavadora.get_puerta_bloqueada() is True
        
        # Act
        resultado = lavadora.iniciar_lavado()
        
        # Assert
        assert resultado is False
        assert lavadora.get_puerta_bloqueada() is True
    
    def test_lavaropas_pausar_lavado_puerta_bloqueada(self):
        """Test: pausar_lavado funciona cuando la puerta está bloqueada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        lavadora.encender()
        lavadora.iniciar_lavado()  # Bloquear puerta
        assert lavadora.get_puerta_bloqueada() is True
        
        # Act
        resultado = lavadora.pausar_lavado()
        
        # Assert
        assert resultado is True
        assert lavadora.get_puerta_bloqueada() is False
    
    def test_lavaropas_pausar_lavado_puerta_desbloqueada(self):
        """Test: pausar_lavado retorna False cuando la puerta no está bloqueada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        assert lavadora.get_puerta_bloqueada() is False
        
        # Act
        resultado = lavadora.pausar_lavado()
        
        # Assert
        assert resultado is False
        assert lavadora.get_puerta_bloqueada() is False
    
    def test_lavaropas_desbloquear_puerta_bloqueada(self):
        """Test: desbloquear_puerta funciona cuando la puerta está bloqueada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        lavadora.encender()
        lavadora.iniciar_lavado()  # Bloquear puerta
        assert lavadora.get_puerta_bloqueada() is True
        
        # Act
        resultado = lavadora.desbloquear_puerta()
        
        # Assert
        assert resultado is True
        assert lavadora.get_puerta_bloqueada() is False
    
    def test_lavaropas_desbloquear_puerta_desbloqueada(self):
        """Test: desbloquear_puerta retorna False cuando la puerta no está bloqueada"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        assert lavadora.get_puerta_bloqueada() is False
        
        # Act
        resultado = lavadora.desbloquear_puerta()
        
        # Assert
        assert resultado is False
        assert lavadora.get_puerta_bloqueada() is False
    
    def test_lavaropas_diferentes_programas(self):
        """Test: Se pueden seleccionar diferentes programas de lavado"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        lavadora.encender()
        
        # Act & Assert
        programas = [
            ProgramaLavaRopas.LAVADO_RAPIDO,
            ProgramaLavaRopas.LAVADO_NORMAL,
            ProgramaLavaRopas.LAVADO_DELICADO,
            ProgramaLavaRopas.LAVADO_ALGODON,
            ProgramaLavaRopas.LAVADO_SINTETICOS
        ]
        
        for programa in programas:
            resultado = lavadora.seleccionar_programa(programa)
            assert resultado is True
            assert lavadora.get_programa_actual() == programa
    
    def test_lavaropas_herencia_de_dispositivo(self):
        """Test: LavaRopas hereda correctamente de Dispositivo"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        
        # Act & Assert
        # Verificar que tiene todos los métodos de la clase padre
        assert hasattr(lavadora, 'get_id_dispositivo')
        assert hasattr(lavadora, 'get_nombre')
        assert hasattr(lavadora, 'get_tipo')
        assert hasattr(lavadora, 'get_marca')
        assert hasattr(lavadora, 'get_modelo')
        assert hasattr(lavadora, 'get_estado')
        assert hasattr(lavadora, 'get_consumo_energetico')
        assert hasattr(lavadora, 'get_fecha_creacion')
        assert hasattr(lavadora, 'get_automatizaciones')
        assert hasattr(lavadora, 'crear_dispositivo')
        assert hasattr(lavadora, 'buscar_por_nombre')
        assert hasattr(lavadora, 'listar_dispositivos')
        assert hasattr(lavadora, 'eliminar_por_nombre')
        assert hasattr(lavadora, 'devolver_lista_de_dispositivos')
        assert hasattr(lavadora, '__str__')
        
        # Verificar que implementa los métodos abstractos
        assert hasattr(lavadora, 'encender')
        assert hasattr(lavadora, 'apagar')
        
        # Verificar métodos específicos de LavaRopas
        assert hasattr(lavadora, 'get_programa_actual')
        assert hasattr(lavadora, 'get_velocidad_centrifugado')
        assert hasattr(lavadora, 'get_velocidad_max_centrifugado')
        assert hasattr(lavadora, 'get_puerta_bloqueada')
        assert hasattr(lavadora, 'seleccionar_programa')
        assert hasattr(lavadora, 'iniciar_lavado')
        assert hasattr(lavadora, 'pausar_lavado')
        assert hasattr(lavadora, 'desbloquear_puerta')
    
    def test_lavaropas_metodos_heredados_funcionan(self):
        """Test: Los métodos heredados de Dispositivo funcionan correctamente"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        
        # Act & Assert
        # Probar crear_dispositivo
        assert lavadora.crear_dispositivo() is True
        
        # Probar buscar_por_nombre
        assert lavadora.buscar_por_nombre("Lavadora Test") is True
        assert lavadora.buscar_por_nombre("lavadora test") is True  # Case insensitive
        assert lavadora.buscar_por_nombre("Other Device") is False
        
        # Probar listar_dispositivos
        lista = lavadora.listar_dispositivos()
        assert isinstance(lista, dict)
        assert lista['nombre'] == "Lavadora Test"
        assert lista['tipo'] == "Lavadora"
        
        # Probar eliminar_por_nombre
        assert lavadora.eliminar_por_nombre() is True
        
        # Probar devolver_lista_de_dispositivos
        lista_dispositivos = lavadora.devolver_lista_de_dispositivos()
        assert isinstance(lista_dispositivos, list)
        assert len(lista_dispositivos) == 1
    
    def test_lavaropas_str_representacion(self):
        """Test: __str__ retorna representación correcta de la lavadora"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        
        # Act
        resultado = str(lavadora)
        
        # Assert
        assert "Lavadora" in resultado
        assert "Lavadora Test" in resultado
        assert "Samsung" in resultado
        assert "WW90T5540AE" in resultado
    
    def test_lavaropas_estado_inicial_correcto(self):
        """Test: El estado inicial de la lavadora es correcto"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        
        # Assert
        assert lavadora.get_estado() is False  # Apagada
        assert lavadora.get_programa_actual() == ProgramaLavaRopas.LAVADO_RAPIDO
        assert lavadora.get_velocidad_centrifugado() == 0
        assert lavadora.get_puerta_bloqueada() is False
        assert lavadora.get_tipo() == "Lavadora"
        assert isinstance(lavadora.get_fecha_creacion(), datetime)
    
    def test_lavaropas_secuencia_lavado_completa(self):
        """Test: Secuencia completa de lavado funciona correctamente"""
        # Arrange
        lavadora = LavaRopas(1, "Lavadora Test", "Samsung", "WW90T5540AE", 300.0)
        
        # Act & Assert
        # 1. Encender lavadora
        assert lavadora.encender() is True
        assert lavadora.get_estado() is True
        assert lavadora.get_puerta_bloqueada() is False
        
        # 2. Seleccionar programa
        assert lavadora.seleccionar_programa(ProgramaLavaRopas.LAVADO_NORMAL) is True
        assert lavadora.get_programa_actual() == ProgramaLavaRopas.LAVADO_NORMAL
        
        # 3. Iniciar lavado
        assert lavadora.iniciar_lavado() is True
        assert lavadora.get_puerta_bloqueada() is True
        
        # 4. Pausar lavado
        assert lavadora.pausar_lavado() is True
        assert lavadora.get_puerta_bloqueada() is False
        
        # 5. Desbloquear puerta (redundante pero válido)
        assert lavadora.desbloquear_puerta() is False  # Ya está desbloqueada
        
        # 6. Apagar lavadora
        assert lavadora.apagar() is True
        assert lavadora.get_estado() is False
        assert lavadora.get_puerta_bloqueada() is False
