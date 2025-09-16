import pytest
from datetime import date, datetime
from enums import Rol, TipoDispositivoDigital
from entidades.Usuario import Usuario
from entidades.Dispositivo import Dispositivo
from entidades.DispositivoDigital import DispositivoDigital
from entidades.Domicilio import Domicilio, UbicacionCasa


@pytest.fixture
def usuario_admin():
    return Usuario(
        id_usuario=1,
        nombre="Admin",
        apellido="Sistema",
        email="admin@test.com",
        contraseña="admin123",
        telefono="123456789",
        rol=Rol.ADMINISTRADOR,
        fecha_nacimiento=date(1990, 1, 1)
    )


@pytest.fixture
def usuario_normal():
    return Usuario(
        id_usuario=2,
        nombre="Juan",
        apellido="Pérez",
        email="juan@test.com",
        contraseña="juan123",
        telefono="987654321",
        rol=Rol.USUARIO,
        fecha_nacimiento=date(1995, 5, 15)
    )


@pytest.fixture
def domicilio_test():
    return Domicilio(
        id_domicilio=1,
        calle="Calle Test",
        numero=123,
        barrio="Centro",
        ciudad="Buenos Aires",
        pais="Argentina",
        codigo_postal="1000"
    )


@pytest.fixture
def ubicacion_casa_test():
    return UbicacionCasa(
        id_ubicacion=1,
        nombre="Sala",
        descripcion="Sala de estar principal"
    )


@pytest.fixture
def dispositivo_digital_test():
    return DispositivoDigital(
        id_dispositivo=1,
        nombre="Smart TV",
        marca="Samsung",
        modelo="QLED 55",
        consumo_energetico=150.5,
        tipo_dispositivo=TipoDispositivoDigital.TELEVISION
    )
