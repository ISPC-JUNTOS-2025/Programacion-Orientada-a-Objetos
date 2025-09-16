"""
Tests para la clase Domicilio y UbicacionCasa
Implementados siguiendo principios de TDD (Test-Driven Development)
"""
import pytest
from entidades.Domicilio import Domicilio, UbicacionCasa


class TestDomicilio:
    """Clase de tests para Domicilio siguiendo principios TDD"""
    
    def test_domicilio_creacion_exitosa(self):
        """Test: Un domicilio se puede crear con todos los atributos requeridos"""
        # Arrange
        id_domicilio = 1
        calle = "Calle Test"
        numero = 123
        barrio = "Centro"
        ciudad = "Buenos Aires"
        pais = "Argentina"
        codigo_postal = "1000"
        
        # Act
        domicilio = Domicilio(id_domicilio, calle, numero, barrio, ciudad, pais, codigo_postal)
        
        # Assert
        assert domicilio.get_id_domicilio() == id_domicilio
        assert domicilio.get_calle() == calle
        assert domicilio.get_numero() == numero
        assert domicilio.get_barrio() == barrio
        assert domicilio.get_ciudad() == ciudad
        assert domicilio.get_pais() == pais
        assert domicilio.get_codigo_postal() == codigo_postal
        assert domicilio.get_ubicaciones_casa() == []
    
    def test_domicilio_getters_basicos(self):
        """Test: Los getters básicos funcionan correctamente"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        assert domicilio.get_id_domicilio() == 1
        assert domicilio.get_calle() == "Calle Test"
        assert domicilio.get_numero() == 123
        assert domicilio.get_barrio() == "Centro"
        assert domicilio.get_ciudad() == "Buenos Aires"
        assert domicilio.get_pais() == "Argentina"
        assert domicilio.get_codigo_postal() == "1000"
        assert isinstance(domicilio.get_ubicaciones_casa(), list)
    
    def test_domicilio_set_calle_valido(self):
        """Test: set_calle funciona con calle válida"""
        # Arrange
        domicilio = Domicilio(1, "Calle Vieja", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_calle("Calle Nueva")
        
        # Assert
        assert domicilio.get_calle() == "Calle Nueva"
    
    def test_domicilio_set_calle_trim_espacios(self):
        """Test: set_calle elimina espacios en blanco"""
        # Arrange
        domicilio = Domicilio(1, "Calle Vieja", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_calle("  Calle Nueva  ")
        
        # Assert
        assert domicilio.get_calle() == "Calle Nueva"
    
    def test_domicilio_set_calle_vacia(self):
        """Test: set_calle lanza excepción con calle vacía"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        with pytest.raises(ValueError, match="La calle no puede estar vacía"):
            domicilio.set_calle("")
    
    def test_domicilio_set_calle_solo_espacios(self):
        """Test: set_calle lanza excepción con solo espacios"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        with pytest.raises(ValueError, match="La calle no puede estar vacía"):
            domicilio.set_calle("   ")
    
    def test_domicilio_set_numero_valido(self):
        """Test: set_numero funciona con número válido"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_numero(456)
        
        # Assert
        assert domicilio.get_numero() == 456
    
    def test_domicilio_set_numero_cero(self):
        """Test: set_numero lanza excepción con número cero"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        with pytest.raises(ValueError, match="El número debe ser mayor a 0"):
            domicilio.set_numero(0)
    
    def test_domicilio_set_numero_negativo(self):
        """Test: set_numero lanza excepción con número negativo"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        with pytest.raises(ValueError, match="El número debe ser mayor a 0"):
            domicilio.set_numero(-5)
    
    def test_domicilio_set_barrio_valido(self):
        """Test: set_barrio funciona con barrio válido"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_barrio("Nuevo Barrio")
        
        # Assert
        assert domicilio.get_barrio() == "Nuevo Barrio"
    
    def test_domicilio_set_barrio_trim_espacios(self):
        """Test: set_barrio elimina espacios en blanco"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_barrio("  Nuevo Barrio  ")
        
        # Assert
        assert domicilio.get_barrio() == "Nuevo Barrio"
    
    def test_domicilio_set_barrio_vacio(self):
        """Test: set_barrio lanza excepción con barrio vacío"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        with pytest.raises(ValueError, match="El barrio no puede estar vacío"):
            domicilio.set_barrio("")
    
    def test_domicilio_set_ciudad_valido(self):
        """Test: set_ciudad funciona con ciudad válida"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_ciudad("Córdoba")
        
        # Assert
        assert domicilio.get_ciudad() == "Córdoba"
    
    def test_domicilio_set_ciudad_trim_espacios(self):
        """Test: set_ciudad elimina espacios en blanco"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_ciudad("  Córdoba  ")
        
        # Assert
        assert domicilio.get_ciudad() == "Córdoba"
    
    def test_domicilio_set_ciudad_vacia(self):
        """Test: set_ciudad lanza excepción con ciudad vacía"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        with pytest.raises(ValueError, match="La ciudad no puede estar vacía"):
            domicilio.set_ciudad("")
    
    def test_domicilio_set_pais_valido(self):
        """Test: set_pais funciona con país válido"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_pais("Uruguay")
        
        # Assert
        assert domicilio.get_pais() == "Uruguay"
    
    def test_domicilio_set_pais_trim_espacios(self):
        """Test: set_pais elimina espacios en blanco"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_pais("  Uruguay  ")
        
        # Assert
        assert domicilio.get_pais() == "Uruguay"
    
    def test_domicilio_set_pais_vacio(self):
        """Test: set_pais lanza excepción con país vacío"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        with pytest.raises(ValueError, match="El país no puede estar vacío"):
            domicilio.set_pais("")
    
    def test_domicilio_set_codigo_postal_valido(self):
        """Test: set_codigo_postal funciona con código válido"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_codigo_postal("2000")
        
        # Assert
        assert domicilio.get_codigo_postal() == "2000"
    
    def test_domicilio_set_codigo_postal_trim_espacios(self):
        """Test: set_codigo_postal elimina espacios en blanco"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        domicilio.set_codigo_postal("  2000  ")
        
        # Assert
        assert domicilio.get_codigo_postal() == "2000"
    
    def test_domicilio_set_codigo_postal_vacio(self):
        """Test: set_codigo_postal lanza excepción con código vacío"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act & Assert
        with pytest.raises(ValueError, match="El código postal no puede estar vacío"):
            domicilio.set_codigo_postal("")
    
    def test_domicilio_registrar_domicilio_exitoso(self):
        """Test: registrar_domicilio retorna True"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        resultado = domicilio.registrar_domicilio()
        
        # Assert
        assert resultado is True
    
    def test_domicilio_eliminar_domicilio_exitoso(self):
        """Test: eliminar_domicilio retorna True"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        resultado = domicilio.eliminar_domicilio()
        
        # Assert
        assert resultado is True
    
    def test_domicilio_buscar_domicilio_por_email_usuario(self):
        """Test: buscar_domicilio_por_email_usuario retorna True"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        resultado = domicilio.buscar_domicilio_por_email_usuario("test@test.com")
        
        # Assert
        assert resultado is True
    
    def test_domicilio_buscar_domicilio_por_id_encontrado(self):
        """Test: buscar_domicilio_por_id encuentra domicilio con ID correcto"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        resultado = domicilio.buscar_domicilio_por_id(1)
        
        # Assert
        assert resultado is True
    
    def test_domicilio_buscar_domicilio_por_id_no_encontrado(self):
        """Test: buscar_domicilio_por_id retorna False con ID incorrecto"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        resultado = domicilio.buscar_domicilio_por_id(999)
        
        # Assert
        assert resultado is False
    
    def test_domicilio_agregar_ubicacion_exitoso(self):
        """Test: agregar_ubicacion funciona correctamente"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar")
        
        # Act
        resultado = domicilio.agregar_ubicacion(ubicacion)
        
        # Assert
        assert resultado is True
        assert ubicacion in domicilio.get_ubicaciones_casa()
    
    def test_domicilio_agregar_ubicacion_duplicada(self):
        """Test: agregar_ubicacion maneja ubicación duplicada correctamente"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar")
        domicilio.agregar_ubicacion(ubicacion)
        
        # Act
        resultado = domicilio.agregar_ubicacion(ubicacion)
        
        # Assert
        assert resultado is False  # No se agrega duplicado
        assert domicilio.get_ubicaciones_casa().count(ubicacion) == 1
    
    def test_domicilio_remover_ubicacion_exitoso(self):
        """Test: remover_ubicacion funciona correctamente"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar")
        domicilio.agregar_ubicacion(ubicacion)
        
        # Act
        resultado = domicilio.remover_ubicacion(ubicacion)
        
        # Assert
        assert resultado is True
        assert ubicacion not in domicilio.get_ubicaciones_casa()
    
    def test_domicilio_remover_ubicacion_inexistente(self):
        """Test: remover_ubicacion maneja ubicación inexistente correctamente"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar")
        
        # Act
        resultado = domicilio.remover_ubicacion(ubicacion)
        
        # Assert
        assert resultado is False  # No se puede remover lo que no existe
    
    def test_domicilio_obtener_direccion_completa(self):
        """Test: obtener_direccion_completa retorna dirección formateada correctamente"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        direccion = domicilio.obtener_direccion_completa()
        
        # Assert
        assert direccion == "Calle Test 123, Centro, Buenos Aires, Argentina 1000"
    
    def test_domicilio_str_representacion(self):
        """Test: __str__ retorna la dirección completa"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        
        # Act
        resultado = str(domicilio)
        
        # Assert
        assert resultado == "Calle Test 123, Centro, Buenos Aires, Argentina 1000"
    
    def test_domicilio_ubicaciones_casa_copia_segura(self):
        """Test: get_ubicaciones_casa retorna una copia de la lista"""
        # Arrange
        domicilio = Domicilio(1, "Calle Test", 123, "Centro", "Buenos Aires", "Argentina", "1000")
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar")
        domicilio.agregar_ubicacion(ubicacion)
        
        # Act
        ubicaciones1 = domicilio.get_ubicaciones_casa()
        ubicaciones2 = domicilio.get_ubicaciones_casa()
        
        # Assert
        assert ubicaciones1 is not ubicaciones2  # Diferentes objetos
        assert ubicaciones1 == ubicaciones2  # Mismo contenido


class TestUbicacionCasa:
    """Clase de tests para UbicacionCasa siguiendo principios TDD"""
    
    def test_ubicacion_casa_creacion_exitosa(self):
        """Test: Una ubicación de casa se puede crear con todos los atributos requeridos"""
        # Arrange
        id_ubicacion = 1
        nombre = "Sala"
        descripcion = "Sala de estar principal"
        
        # Act
        ubicacion = UbicacionCasa(id_ubicacion, nombre, descripcion)
        
        # Assert
        assert ubicacion.get_id_ubicacion() == id_ubicacion
        assert ubicacion.get_nombre() == nombre
        assert ubicacion.get_descripcion() == descripcion
        assert ubicacion.get_dispositivos() == []
    
    def test_ubicacion_casa_getters_basicos(self):
        """Test: Los getters básicos funcionan correctamente"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        
        # Act & Assert
        assert ubicacion.get_id_ubicacion() == 1
        assert ubicacion.get_nombre() == "Sala"
        assert ubicacion.get_descripcion() == "Sala de estar principal"
        assert isinstance(ubicacion.get_dispositivos(), list)
    
    def test_ubicacion_casa_set_nombre_valido(self):
        """Test: set_nombre funciona con nombre válido"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala Vieja", "Descripción")
        
        # Act
        ubicacion.set_nombre("Sala Nueva")
        
        # Assert
        assert ubicacion.get_nombre() == "Sala Nueva"
    
    def test_ubicacion_casa_set_nombre_trim_espacios(self):
        """Test: set_nombre elimina espacios en blanco"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala Vieja", "Descripción")
        
        # Act
        ubicacion.set_nombre("  Sala Nueva  ")
        
        # Assert
        assert ubicacion.get_nombre() == "Sala Nueva"
    
    def test_ubicacion_casa_set_nombre_vacio(self):
        """Test: set_nombre lanza excepción con nombre vacío"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Descripción")
        
        # Act & Assert
        with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
            ubicacion.set_nombre("")
    
    def test_ubicacion_casa_set_descripcion_valido(self):
        """Test: set_descripcion funciona con descripción válida"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Descripción vieja")
        
        # Act
        ubicacion.set_descripcion("Descripción nueva")
        
        # Assert
        assert ubicacion.get_descripcion() == "Descripción nueva"
    
    def test_ubicacion_casa_set_descripcion_trim_espacios(self):
        """Test: set_descripcion elimina espacios en blanco"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Descripción vieja")
        
        # Act
        ubicacion.set_descripcion("  Descripción nueva  ")
        
        # Assert
        assert ubicacion.get_descripcion() == "Descripción nueva"
    
    def test_ubicacion_casa_set_descripcion_vacia(self):
        """Test: set_descripcion lanza excepción con descripción vacía"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Descripción")
        
        # Act & Assert
        with pytest.raises(ValueError, match="La descripción no puede estar vacía"):
            ubicacion.set_descripcion("")
    
    def test_ubicacion_casa_crear_ubicacion_exitoso(self):
        """Test: crear_ubicacion retorna True"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        
        # Act
        resultado = ubicacion.crear_ubicacion()
        
        # Assert
        assert resultado is True
    
    def test_ubicacion_casa_leer_ubicacion(self):
        """Test: leer_ubicacion retorna diccionario con información correcta"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        
        # Act
        resultado = ubicacion.leer_ubicacion()
        
        # Assert
        assert isinstance(resultado, dict)
        assert resultado['id_ubicacion'] == 1
        assert resultado['nombre'] == "Sala"
        assert resultado['descripcion'] == "Sala de estar principal"
        assert resultado['cantidad_dispositivos'] == 0
    
    def test_ubicacion_casa_actualizar_ubicacion_solo_nombre(self):
        """Test: actualizar_ubicacion funciona solo con nombre"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Descripción original")
        
        # Act
        resultado = ubicacion.actualizar_ubicacion(nuevo_nombre="Sala Nueva")
        
        # Assert
        assert resultado is True
        assert ubicacion.get_nombre() == "Sala Nueva"
        assert ubicacion.get_descripcion() == "Descripción original"
    
    def test_ubicacion_casa_actualizar_ubicacion_solo_descripcion(self):
        """Test: actualizar_ubicacion funciona solo con descripción"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Descripción original")
        
        # Act
        resultado = ubicacion.actualizar_ubicacion(nueva_descripcion="Descripción nueva")
        
        # Assert
        assert resultado is True
        assert ubicacion.get_nombre() == "Sala"
        assert ubicacion.get_descripcion() == "Descripción nueva"
    
    def test_ubicacion_casa_actualizar_ubicacion_ambos(self):
        """Test: actualizar_ubicacion funciona con ambos parámetros"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Descripción original")
        
        # Act
        resultado = ubicacion.actualizar_ubicacion("Sala Nueva", "Descripción nueva")
        
        # Assert
        assert resultado is True
        assert ubicacion.get_nombre() == "Sala Nueva"
        assert ubicacion.get_descripcion() == "Descripción nueva"
    
    def test_ubicacion_casa_eliminar_ubicacion_exitoso(self):
        """Test: eliminar_ubicacion retorna True"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        
        # Act
        resultado = ubicacion.eliminar_ubicacion()
        
        # Assert
        assert resultado is True
    
    def test_ubicacion_casa_agregar_dispositivo_exitoso(self):
        """Test: agregar_dispositivo funciona correctamente"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'TV'})()
        
        # Act
        resultado = ubicacion.agregar_dispositivo(dispositivo_mock)
        
        # Assert
        assert resultado is True
        assert dispositivo_mock in ubicacion.get_dispositivos()
    
    def test_ubicacion_casa_agregar_dispositivo_duplicado(self):
        """Test: agregar_dispositivo maneja dispositivo duplicado correctamente"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'TV'})()
        ubicacion.agregar_dispositivo(dispositivo_mock)
        
        # Act
        resultado = ubicacion.agregar_dispositivo(dispositivo_mock)
        
        # Assert
        assert resultado is False  # No se agrega duplicado
        assert ubicacion.get_dispositivos().count(dispositivo_mock) == 1
    
    def test_ubicacion_casa_remover_dispositivo_exitoso(self):
        """Test: remover_dispositivo funciona correctamente"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'TV'})()
        ubicacion.agregar_dispositivo(dispositivo_mock)
        
        # Act
        resultado = ubicacion.remover_dispositivo(dispositivo_mock)
        
        # Assert
        assert resultado is True
        assert dispositivo_mock not in ubicacion.get_dispositivos()
    
    def test_ubicacion_casa_remover_dispositivo_inexistente(self):
        """Test: remover_dispositivo maneja dispositivo inexistente correctamente"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'TV'})()
        
        # Act
        resultado = ubicacion.remover_dispositivo(dispositivo_mock)
        
        # Assert
        assert resultado is False  # No se puede remover lo que no existe
    
    def test_ubicacion_casa_listar_dispositivos_vacio(self):
        """Test: listar_dispositivos retorna lista vacía cuando no hay dispositivos"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        
        # Act
        resultado = ubicacion.listar_dispositivos()
        
        # Assert
        assert isinstance(resultado, list)
        assert len(resultado) == 0
    
    def test_ubicacion_casa_listar_dispositivos_con_dispositivos(self):
        """Test: listar_dispositivos retorna lista con dispositivos"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        dispositivo_mock = type('DispositivoMock', (), {
            'get_nombre': lambda: 'TV',
            'listar_dispositivos': lambda: {'nombre': 'TV', 'tipo': 'Televisión'}
        })()
        ubicacion.agregar_dispositivo(dispositivo_mock)
        
        # Act
        resultado = ubicacion.listar_dispositivos()
        
        # Assert
        assert isinstance(resultado, list)
        assert len(resultado) == 1
        assert resultado[0]['nombre'] == 'TV'
    
    def test_ubicacion_casa_str_representacion(self):
        """Test: __str__ retorna representación correcta de la ubicación"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        
        # Act
        resultado = str(ubicacion)
        
        # Assert
        assert "Sala" in resultado
        assert "Sala de estar principal" in resultado
    
    def test_ubicacion_casa_dispositivos_copia_segura(self):
        """Test: get_dispositivos retorna una copia de la lista"""
        # Arrange
        ubicacion = UbicacionCasa(1, "Sala", "Sala de estar principal")
        dispositivo_mock = type('DispositivoMock', (), {'get_nombre': lambda: 'TV'})()
        ubicacion.agregar_dispositivo(dispositivo_mock)
        
        # Act
        dispositivos1 = ubicacion.get_dispositivos()
        dispositivos2 = ubicacion.get_dispositivos()
        
        # Assert
        assert dispositivos1 is not dispositivos2  # Diferentes objetos
        assert dispositivos1 == dispositivos2  # Mismo contenido
