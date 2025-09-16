"""
Tests para la clase Automatizacion
Implementados siguiendo principios de TDD (Test-Driven Development)
"""
import pytest
from datetime import datetime
from entidades.Automatizacion import Automatizacion


class TestAutomatizacion:
    """Clase de tests para Automatizacion siguiendo principios TDD"""
    
    def test_automatizacion_creacion_exitosa(self):
        """Test: Una automatización se puede crear con todos los atributos requeridos"""
        # Arrange
        id_automatizacion = 1
        nombre = "Luz Automática"
        descripcion = "Enciende luces al detectar movimiento"
        regla = "Si hay movimiento"
        condicion = "Sensor detecta movimiento"
        accion = "Encender luces"
        
        # Act
        automatizacion = Automatizacion(id_automatizacion, nombre, descripcion, regla, condicion, accion)
        
        # Assert
        assert automatizacion.get_id_automatizacion() == id_automatizacion
        assert automatizacion.get_nombre() == nombre
        assert automatizacion.get_descripcion() == descripcion
        assert automatizacion.get_regla() == regla
        assert automatizacion.get_condicion() == condicion
        assert automatizacion.get_accion() == accion
        assert automatizacion.get_estado() is False
        assert automatizacion.get_dispositivos_controlados() == []
    
    def test_automatizacion_getters_basicos(self):
        """Test: Los getters básicos funcionan correctamente"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición", "Acción")
        
        # Act & Assert
        assert automatizacion.get_id_automatizacion() == 1
        assert automatizacion.get_nombre() == "Test"
        assert automatizacion.get_descripcion() == "Descripción"
        assert automatizacion.get_regla() == "Regla"
        assert automatizacion.get_condicion() == "Condición"
        assert automatizacion.get_accion() == "Acción"
        assert automatizacion.get_estado() is False
        assert isinstance(automatizacion.get_dispositivos_controlados(), list)
    
    def test_automatizacion_set_nombre_valido(self):
        """Test: set_nombre funciona con nombre válido"""
        # Arrange
        automatizacion = Automatizacion(1, "Nombre Viejo", "Descripción", "Regla", "Condición", "Acción")
        
        # Act
        automatizacion.set_nombre("Nombre Nuevo")
        
        # Assert
        assert automatizacion.get_nombre() == "Nombre Nuevo"
    
    def test_automatizacion_set_nombre_trim_espacios(self):
        """Test: set_nombre elimina espacios en blanco"""
        # Arrange
        automatizacion = Automatizacion(1, "Nombre Viejo", "Descripción", "Regla", "Condición", "Acción")
        
        # Act
        automatizacion.set_nombre("  Nombre Nuevo  ")
        
        # Assert
        assert automatizacion.get_nombre() == "Nombre Nuevo"
    
    def test_automatizacion_set_nombre_vacio(self):
        """Test: set_nombre lanza excepción con nombre vacío"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición", "Acción")
        
        # Act & Assert
        with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
            automatizacion.set_nombre("")
    
    def test_automatizacion_set_descripcion_valido(self):
        """Test: set_descripcion funciona con descripción válida"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción Vieja", "Regla", "Condición", "Acción")
        
        # Act
        automatizacion.set_descripcion("Descripción Nueva")
        
        # Assert
        assert automatizacion.get_descripcion() == "Descripción Nueva"
    
    def test_automatizacion_set_descripcion_trim_espacios(self):
        """Test: set_descripcion elimina espacios en blanco"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción Vieja", "Regla", "Condición", "Acción")
        
        # Act
        automatizacion.set_descripcion("  Descripción Nueva  ")
        
        # Assert
        assert automatizacion.get_descripcion() == "Descripción Nueva"
    
    def test_automatizacion_set_descripcion_vacia(self):
        """Test: set_descripcion lanza excepción con descripción vacía"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición", "Acción")
        
        # Act & Assert
        with pytest.raises(ValueError, match="La descripción no puede estar vacía"):
            automatizacion.set_descripcion("")
    
    def test_automatizacion_set_regla_valido(self):
        """Test: set_regla funciona con regla válida"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla Vieja", "Condición", "Acción")
        
        # Act
        automatizacion.set_regla("Regla Nueva")
        
        # Assert
        assert automatizacion.get_regla() == "Regla Nueva"
    
    def test_automatizacion_set_regla_trim_espacios(self):
        """Test: set_regla elimina espacios en blanco"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla Vieja", "Condición", "Acción")
        
        # Act
        automatizacion.set_regla("  Regla Nueva  ")
        
        # Assert
        assert automatizacion.get_regla() == "Regla Nueva"
    
    def test_automatizacion_set_regla_vacia(self):
        """Test: set_regla lanza excepción con regla vacía"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición", "Acción")
        
        # Act & Assert
        with pytest.raises(ValueError, match="La regla no puede estar vacía"):
            automatizacion.set_regla("")
    
    def test_automatizacion_set_condicion_valido(self):
        """Test: set_condicion funciona con condición válida"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición Vieja", "Acción")
        
        # Act
        automatizacion.set_condicion("Condición Nueva")
        
        # Assert
        assert automatizacion.get_condicion() == "Condición Nueva"
    
    def test_automatizacion_set_condicion_trim_espacios(self):
        """Test: set_condicion elimina espacios en blanco"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición Vieja", "Acción")
        
        # Act
        automatizacion.set_condicion("  Condición Nueva  ")
        
        # Assert
        assert automatizacion.get_condicion() == "Condición Nueva"
    
    def test_automatizacion_set_condicion_vacia(self):
        """Test: set_condicion lanza excepción con condición vacía"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición", "Acción")
        
        # Act & Assert
        with pytest.raises(ValueError, match="La condición no puede estar vacía"):
            automatizacion.set_condicion("")
    
    def test_automatizacion_set_accion_valido(self):
        """Test: set_accion funciona con acción válida"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición", "Acción Vieja")
        
        # Act
        automatizacion.set_accion("Acción Nueva")
        
        # Assert
        assert automatizacion.get_accion() == "Acción Nueva"
    
    def test_automatizacion_set_accion_trim_espacios(self):
        """Test: set_accion elimina espacios en blanco"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición", "Acción Vieja")
        
        # Act
        automatizacion.set_accion("  Acción Nueva  ")
        
        # Assert
        assert automatizacion.get_accion() == "Acción Nueva"
    
    def test_automatizacion_set_accion_vacia(self):
        """Test: set_accion lanza excepción con acción vacía"""
        # Arrange
        automatizacion = Automatizacion(1, "Test", "Descripción", "Regla", "Condición", "Acción")
        
        # Act & Assert
        with pytest.raises(ValueError, match="La acción no puede estar vacía"):
            automatizacion.set_accion("")
    
    def test_automatizacion_activar_encender_luces_inactiva(self):
        """Test: activar_automatizacion_encender_luces funciona cuando está inactiva"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        assert automatizacion.get_estado() is False
        
        # Act
        resultado = automatizacion.activar_automatizacion_encender_luces()
        
        # Assert
        assert resultado is True
        assert automatizacion.get_estado() is True
    
    def test_automatizacion_activar_encender_luces_ya_activa(self):
        """Test: activar_automatizacion_encender_luces retorna False cuando ya está activa"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        automatizacion.activar_automatizacion_encender_luces()
        assert automatizacion.get_estado() is True
        
        # Act
        resultado = automatizacion.activar_automatizacion_encender_luces()
        
        # Assert
        assert resultado is False
        assert automatizacion.get_estado() is True
    
    def test_automatizacion_desactivar_encender_luces_activa(self):
        """Test: desactivar_automatizacion_encender_luces funciona cuando está activa"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        automatizacion.activar_automatizacion_encender_luces()
        assert automatizacion.get_estado() is True
        
        # Act
        resultado = automatizacion.desactivar_automatizacion_encender_luces()
        
        # Assert
        assert resultado is True
        assert automatizacion.get_estado() is False
    
    def test_automatizacion_desactivar_encender_luces_ya_inactiva(self):
        """Test: desactivar_automatizacion_encender_luces retorna False cuando ya está inactiva"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        assert automatizacion.get_estado() is False
        
        # Act
        resultado = automatizacion.desactivar_automatizacion_encender_luces()
        
        # Assert
        assert resultado is False
        assert automatizacion.get_estado() is False
    
    def test_automatizacion_consultar_automatizaciones_activas(self):
        """Test: consultar_automatizaciones_activas retorna diccionario con información correcta"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        
        # Act
        resultado = automatizacion.consultar_automatizaciones_activas()
        
        # Assert
        assert isinstance(resultado, dict)
        assert resultado['id_automatizacion'] == 1
        assert resultado['nombre'] == "Luz Auto"
        assert resultado['descripcion'] == "Enciende luces"
        assert resultado['estado'] == "Inactiva"
        assert resultado['regla'] == "Si hay movimiento"
        assert resultado['condicion'] == "Sensor activo"
        assert resultado['accion'] == "Encender luces"
        assert resultado['dispositivos_controlados'] == 0
    
    def test_automatizacion_consultar_automatizaciones_activas_activa(self):
        """Test: consultar_automatizaciones_activas muestra estado correcto cuando está activa"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        automatizacion.activar_automatizacion_encender_luces()
        
        # Act
        resultado = automatizacion.consultar_automatizaciones_activas()
        
        # Assert
        assert resultado['estado'] == "Activa"
    
    def test_automatizacion_menu_automatizaciones(self):
        """Test: menu_automatizaciones no lanza excepción"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        
        # Act & Assert
        # No hay valor de retorno, solo verificar que no lanza excepción
        automatizacion.menu_automatizaciones()
        assert True  # Si llegamos aquí, no hubo excepción
    
    def test_automatizacion_agregar_dispositivo_exitoso(self):
        """Test: agregar_dispositivo funciona correctamente"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'Luz Test'})()
        
        # Act
        resultado = automatizacion.agregar_dispositivo(dispositivo_mock)
        
        # Assert
        assert resultado is True
        assert dispositivo_mock in automatizacion.get_dispositivos_controlados()
    
    def test_automatizacion_agregar_dispositivo_duplicado(self):
        """Test: agregar_dispositivo maneja dispositivo duplicado correctamente"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'Luz Test'})()
        automatizacion.agregar_dispositivo(dispositivo_mock)
        
        # Act
        resultado = automatizacion.agregar_dispositivo(dispositivo_mock)
        
        # Assert
        assert resultado is False  # No se agrega duplicado
        assert automatizacion.get_dispositivos_controlados().count(dispositivo_mock) == 1
    
    def test_automatizacion_remover_dispositivo_exitoso(self):
        """Test: remover_dispositivo funciona correctamente"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'Luz Test'})()
        automatizacion.agregar_dispositivo(dispositivo_mock)
        
        # Act
        resultado = automatizacion.remover_dispositivo(dispositivo_mock)
        
        # Assert
        assert resultado is True
        assert dispositivo_mock not in automatizacion.get_dispositivos_controlados()
    
    def test_automatizacion_remover_dispositivo_inexistente(self):
        """Test: remover_dispositivo maneja dispositivo inexistente correctamente"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'Luz Test'})()
        
        # Act
        resultado = automatizacion.remover_dispositivo(dispositivo_mock)
        
        # Assert
        assert resultado is False  # No se puede remover lo que no existe
    
    def test_automatizacion_ejecutar_automatizacion_activa_encender_luces(self):
        """Test: ejecutar_automatizacion funciona con automatización activa para encender luces"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        automatizacion.activar_automatizacion_encender_luces()
        assert automatizacion.get_estado() is True
        
        # Act
        resultado = automatizacion.ejecutar_automatizacion()
        
        # Assert
        assert resultado is True
    
    def test_automatizacion_ejecutar_automatizacion_activa_apagar_luces(self):
        """Test: ejecutar_automatizacion funciona con automatización activa para apagar luces"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Apaga luces", "Si no hay movimiento", "Sensor inactivo", "Apagar luces")
        automatizacion.activar_automatizacion_encender_luces()  # Activar primero
        assert automatizacion.get_estado() is True
        
        # Act
        resultado = automatizacion.ejecutar_automatizacion()
        
        # Assert
        assert resultado is True
    
    def test_automatizacion_ejecutar_automatizacion_inactiva(self):
        """Test: ejecutar_automatizacion retorna False cuando está inactiva"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        assert automatizacion.get_estado() is False
        
        # Act
        resultado = automatizacion.ejecutar_automatizacion()
        
        # Assert
        assert resultado is False
    
    def test_automatizacion_ejecutar_automatizacion_no_reconocida(self):
        """Test: ejecutar_automatizacion retorna False con acción no reconocida"""
        # Arrange
        automatizacion = Automatizacion(1, "Test Auto", "Test", "Regla", "Condición", "Acción no reconocida")
        automatizacion.activar_automatizacion_encender_luces()
        assert automatizacion.get_estado() is True
        
        # Act
        resultado = automatizacion.ejecutar_automatizacion()
        
        # Assert
        assert resultado is False
    
    def test_automatizacion_validar_condicion_movimiento(self):
        """Test: validar_condicion funciona con condición de movimiento"""
        # Arrange
        automatizacion = Automatizacion(1, "Test Auto", "Test", "Regla", "Detectar movimiento", "Acción")
        
        # Act & Assert
        assert automatizacion.validar_condicion(True) is True
        assert automatizacion.validar_condicion(False) is False
        assert automatizacion.validar_condicion(None) is False
    
    def test_automatizacion_validar_condicion_hora(self):
        """Test: validar_condicion funciona con condición de hora"""
        # Arrange
        automatizacion = Automatizacion(1, "Test Auto", "Test", "Regla", "A las 18:00", "Acción")
        
        # Act & Assert
        assert automatizacion.validar_condicion() is True
        assert automatizacion.validar_condicion(True) is True
        assert automatizacion.validar_condicion(False) is True
    
    def test_automatizacion_validar_condicion_temperatura(self):
        """Test: validar_condicion funciona con condición de temperatura"""
        # Arrange
        automatizacion = Automatizacion(1, "Test Auto", "Test", "Regla", "Temperatura > 25°C", "Acción")
        
        # Act & Assert
        assert automatizacion.validar_condicion() is True
        assert automatizacion.validar_condicion(True) is True
        assert automatizacion.validar_condicion(False) is True
    
    def test_automatizacion_validar_condicion_default(self):
        """Test: validar_condicion retorna True por defecto"""
        # Arrange
        automatizacion = Automatizacion(1, "Test Auto", "Test", "Regla", "Condición desconocida", "Acción")
        
        # Act & Assert
        assert automatizacion.validar_condicion() is True
        assert automatizacion.validar_condicion(True) is True
        assert automatizacion.validar_condicion(False) is True
    
    def test_automatizacion_str_representacion(self):
        """Test: __str__ retorna representación correcta de la automatización"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        
        # Act
        resultado = str(automatizacion)
        
        # Assert
        assert "Luz Auto" in resultado
        assert "Inactiva" in resultado
        assert "Enciende luces" in resultado
    
    def test_automatizacion_str_representacion_activa(self):
        """Test: __str__ muestra estado correcto cuando está activa"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        automatizacion.activar_automatizacion_encender_luces()
        
        # Act
        resultado = str(automatizacion)
        
        # Assert
        assert "Luz Auto" in resultado
        assert "Activa" in resultado
        assert "Enciende luces" in resultado
    
    def test_automatizacion_estado_inicial_correcto(self):
        """Test: El estado inicial de la automatización es correcto"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        
        # Assert
        assert automatizacion.get_estado() is False  # Inactiva
        assert automatizacion.get_dispositivos_controlados() == []
        assert automatizacion.get_nombre() == "Luz Auto"
        assert automatizacion.get_descripcion() == "Enciende luces"
        assert automatizacion.get_regla() == "Si hay movimiento"
        assert automatizacion.get_condicion() == "Sensor activo"
        assert automatizacion.get_accion() == "Encender luces"
    
    def test_automatizacion_dispositivos_controlados_copia_segura(self):
        """Test: get_dispositivos_controlados retorna una copia de la lista"""
        # Arrange
        automatizacion = Automatizacion(1, "Luz Auto", "Enciende luces", "Si hay movimiento", "Sensor activo", "Encender luces")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'Luz Test'})()
        automatizacion.agregar_dispositivo(dispositivo_mock)
        
        # Act
        dispositivos1 = automatizacion.get_dispositivos_controlados()
        dispositivos2 = automatizacion.get_dispositivos_controlados()
        
        # Assert
        assert dispositivos1 is not dispositivos2  # Diferentes objetos
        assert dispositivos1 == dispositivos2  # Mismo contenido
