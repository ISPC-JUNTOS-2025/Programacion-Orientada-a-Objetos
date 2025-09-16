import pytest
from datetime import date, datetime
from enums import Rol
from entidades.Usuario import Usuario, lista_de_usuarios


class TestUsuario:
    def test_usuario_creacion_exitosa(self):
        id_usuario = 1
        nombre = "Juan"
        apellido = "Pérez"
        email = "juan@test.com"
        contraseña = "juan123"
        telefono = "123456789"
        rol = Rol.USUARIO
        fecha_nacimiento = date(1995, 5, 15)
        
        usuario = Usuario(id_usuario, nombre, apellido, email, contraseña, 
                         telefono, rol, fecha_nacimiento)
        
        assert usuario.get_id_usuario() == id_usuario
        assert usuario.get_nombre() == nombre
        assert usuario.get_apellido() == apellido
        assert usuario.get_email() == email
        assert usuario.get_telefono() == telefono
        assert usuario.get_rol() == rol
        assert usuario.get_fecha_nacimiento() == fecha_nacimiento
        assert isinstance(usuario.get_fecha_creacion(), datetime)
        assert usuario.get_lista_de_domicilios() == []
    
    def test_usuario_setters_validos(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        usuario.set_nombre("Carlos")
        assert usuario.get_nombre() == "Carlos"
        
        usuario.set_apellido("García")
        assert usuario.get_apellido() == "García"
        
        usuario.set_email("carlos@test.com")
        assert usuario.get_email() == "carlos@test.com"
        
        usuario.set_telefono("987654321")
        assert usuario.get_telefono() == "987654321"
        
        usuario.set_rol(Rol.ADMINISTRADOR)
        assert usuario.get_rol() == Rol.ADMINISTRADOR
        
        nueva_fecha = date(1990, 1, 1)
        usuario.set_fecha_nacimiento(nueva_fecha)
        assert usuario.get_fecha_nacimiento() == nueva_fecha
    
    def test_usuario_set_nombre_trim_espacios(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        usuario.set_nombre("  Carlos  ")

        assert usuario.get_nombre() == "Carlos"
    
    def test_usuario_set_apellido_trim_espacios(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        usuario.set_apellido("  García  ")

        assert usuario.get_apellido() == "García"
    
    def test_usuario_set_contraseña_trim_espacios(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        usuario.set_contraseña("  nueva123  ")

        assert usuario.get_contraseña() == "nueva123"
    
    def test_usuario_agregar_domicilio_exitoso(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))
        domicilio_mock = "Calle Test 123"

        usuario.set_lista_de_domicilios(domicilio_mock)

        assert domicilio_mock in usuario.get_lista_de_domicilios()
        assert len(usuario.get_lista_de_domicilios()) == 1
    
    def test_usuario_registrar_usuario_exitoso(self):
        usuario = Usuario(1, "", "", "", "", "", Rol.USUARIO, date(1995, 5, 15))
        nombre = "Juan"
        apellido = "Pérez"
        email = "juan@test.com"
        contraseña = "juan123"
        telefono = "123456789"
        fecha_nacimiento = date(1995, 5, 15)

        resultado = usuario.registrar_usuario(nombre, apellido, email, contraseña, 
                                            telefono, fecha_nacimiento)

        assert isinstance(resultado, dict)
        assert resultado['nombre'] == nombre
        assert resultado['apellido'] == apellido
        assert resultado['email'] == email
        assert resultado['telefono'] == telefono
        assert resultado['rol'] == Rol.USUARIO
        assert resultado['fecha_nacimiento'] == fecha_nacimiento
        assert 'fecha_creacion' in resultado
        assert 'direcciones' in resultado
    
    def test_usuario_registrar_usuario_nombre_vacio(self):
        usuario = Usuario(1, "", "", "", "", "", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="El nombre no puede estar vacio"):
            usuario.registrar_usuario("", "Pérez", "juan@test.com", "juan123", 
                                    "123456789", date(1995, 5, 15))
    
    def test_usuario_registrar_usuario_apellido_vacio(self):
        usuario = Usuario(1, "", "", "", "", "", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="El apellido no puede estar vacio"):
            usuario.registrar_usuario("Juan", "", "juan@test.com", "juan123", 
                                    "123456789", date(1995, 5, 15))
    
    def test_usuario_registrar_usuario_contraseña_vacia(self):
        usuario = Usuario(1, "", "", "", "", "", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="La contraseña no puede estar vacia"):
            usuario.registrar_usuario("Juan", "Pérez", "juan@test.com", "", 
                                    "123456789", date(1995, 5, 15))
    
    def test_usuario_registrar_usuario_telefono_vacio(self):
        usuario = Usuario(1, "", "", "", "", "", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="El telefono no puede estar vacio"):
            usuario.registrar_usuario("Juan", "Pérez", "juan@test.com", "juan123", 
                                    "", date(1995, 5, 15))
    
    def test_usuario_registrar_usuario_fecha_vacia(self):
        usuario = Usuario(1, "", "", "", "", "", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="La fecha de nacimiento no puede estar vacia"):
            usuario.registrar_usuario("Juan", "Pérez", "juan@test.com", "juan123", 
                                    "123456789", "")
    
    def test_usuario_iniciar_sesion_exitoso(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        resultado = usuario.iniciar_sesion("juan@test.com", "juan123")

        assert isinstance(resultado, dict)
        assert resultado['nombre'] == "Juan"
        assert resultado['apellido'] == "Pérez"
        assert resultado['email'] == "juan@test.com"
        assert resultado['rol'] == Rol.USUARIO.value
        assert 'fecha_creacion' in resultado
        assert 'direcciones' in resultado
    
    def test_usuario_iniciar_sesion_email_vacio(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="El email o la contraseña no pueden estar vacíos"):
            usuario.iniciar_sesion("", "juan123")
    
    def test_usuario_iniciar_sesion_contraseña_vacia(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="El email o la contraseña no pueden estar vacíos"):
            usuario.iniciar_sesion("juan@test.com", "")
    
    def test_usuario_iniciar_sesion_email_incorrecto(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="Email o contraseña incorrectos"):
            usuario.iniciar_sesion("otro@test.com", "juan123")
    
    def test_usuario_consultar_datos_personales(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        resultado = usuario.consultar_datos_personales()

        assert isinstance(resultado, dict)
        assert resultado['id_usuario'] == 1
        assert resultado['nombre'] == "Juan"
        assert resultado['apellido'] == "Pérez"
        assert resultado['email'] == "juan@test.com"
        assert resultado['telefono'] == "123456789"
        assert resultado['rol'] == Rol.USUARIO.value
        assert 'fecha_creacion' in resultado
        assert 'fecha_nacimiento' in resultado
        assert 'cantidad_domicilios' in resultado
    
    def test_usuario_cambiar_rol_exitoso(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        resultado = usuario.cambiar_rol_de_usuario(Rol.ADMINISTRADOR)

        assert resultado is True
        assert usuario.get_rol() == Rol.ADMINISTRADOR
    
    def test_usuario_cambiar_rol_nulo(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="El nuevo rol no puede ser nulo"):
            usuario.cambiar_rol_de_usuario(None)
    
    def test_usuario_agregar_domicilio_exitoso(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))
        domicilio_mock = "Calle Test 123"

        resultado = usuario.agregar_domicilio(domicilio_mock)

        assert resultado is True
        assert domicilio_mock in usuario.get_lista_de_domicilios()
    
    def test_usuario_agregar_domicilio_duplicado(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))
        domicilio_mock = "Calle Test 123"
        usuario.set_lista_de_domicilios(domicilio_mock)

        resultado = usuario.agregar_domicilio(domicilio_mock)

        assert resultado is True  # Retorna True pero no agrega duplicado
    
    def test_usuario_agregar_domicilio_nulo(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="El domicilio no puede ser nulo"):
            usuario.agregar_domicilio(None)
    
    def test_usuario_remover_domicilio_exitoso(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))
        domicilio_mock = "Calle Test 123"
        usuario.set_lista_de_domicilios(domicilio_mock)

        resultado = usuario.remover_domicilio(domicilio_mock)

        assert resultado is True
        assert domicilio_mock not in usuario.get_lista_de_domicilios()
    
    def test_usuario_remover_domicilio_inexistente(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))
        domicilio_mock = "Calle Test 123"

        resultado = usuario.remover_domicilio(domicilio_mock)

        assert resultado is True  # Retorna True pero no remueve nada
    
    def test_usuario_remover_domicilio_nulo(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        with pytest.raises(ValueError, match="El domicilio no puede ser nulo"):
            usuario.remover_domicilio(None)
    
    def test_usuario_consultar_direcciones_usuario_sin_direcciones(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        resultado = usuario.consultar_direcciones_usuario()

        assert resultado is None  # No retorna nada, solo imprime
    
    def test_usuario_consultar_direcciones_usuario_con_direcciones(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))
        domicilio_mock = "Calle Test 123"
        usuario.set_lista_de_domicilios(domicilio_mock)

        resultado = usuario.consultar_direcciones_usuario()

        assert resultado is None  # No retorna nada, solo imprime
    
    def test_usuario_str_representacion(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan@test.com", "juan123", 
                         "123456789", Rol.USUARIO, date(1995, 5, 15))

        resultado = str(usuario)

        assert "Juan" in resultado
        assert "Pérez" in resultado
        assert Rol.USUARIO.value in resultado
