import pytest
from datetime import datetime
from abc import ABC
from entidades.Dispositivo import Dispositivo


class DispositivoConcreto(Dispositivo):
    
    def encender(self) -> bool:
        if not self._estado:
            self._estado = True
            return True
        return False
    
    def apagar(self) -> bool:
        if self._estado:
            self._estado = False
            return True
        return False


class TestDispositivo:
    
    def test_dispositivo_es_clase_abstracta(self):
        # Assert
        assert issubclass(Dispositivo, ABC)
        assert hasattr(Dispositivo, '__abstractmethods__')
        assert 'encender' in Dispositivo.__abstractmethods__
        assert 'apagar' in Dispositivo.__abstractmethods__
    
    def test_dispositivo_creacion_exitosa(self):
        id_dispositivo = 1
        nombre = "Test Device"
        tipo = "Test Type"
        marca = "Test Brand"
        modelo = "Test Model"
        consumo_energetico = 100.5

        dispositivo = DispositivoConcreto(id_dispositivo, nombre, tipo, marca, modelo, consumo_energetico)

        assert dispositivo.get_id_dispositivo() == id_dispositivo
        assert dispositivo.get_nombre() == nombre
        assert dispositivo.get_tipo() == tipo
        assert dispositivo.get_marca() == marca
        assert dispositivo.get_modelo() == modelo
        assert dispositivo.get_consumo_energetico() == consumo_energetico
        assert dispositivo.get_estado() is False  # Estado inicial apagado
        assert isinstance(dispositivo.get_fecha_creacion(), datetime)
        assert dispositivo.get_automatizaciones() == []
    
    def test_dispositivo_getters_basicos(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        assert dispositivo.get_id_dispositivo() == 1
        assert dispositivo.get_nombre() == "Test Device"
        assert dispositivo.get_tipo() == "Test Type"
        assert dispositivo.get_marca() == "Test Brand"
        assert dispositivo.get_modelo() == "Test Model"
        assert dispositivo.get_consumo_energetico() == 100.5
        assert dispositivo.get_estado() is False
        assert isinstance(dispositivo.get_fecha_creacion(), datetime)
        assert isinstance(dispositivo.get_automatizaciones(), list)
    
    def test_dispositivo_set_nombre_valido(self):
        dispositivo = DispositivoConcreto(1, "Old Name", "Test Type", "Test Brand", "Test Model", 100.5)

        dispositivo.set_nombre("New Name")

        assert dispositivo.get_nombre() == "New Name"
    
    def test_dispositivo_set_nombre_trim_espacios(self):
        dispositivo = DispositivoConcreto(1, "Old Name", "Test Type", "Test Brand", "Test Model", 100.5)

        dispositivo.set_nombre("  New Name  ")

        assert dispositivo.get_nombre() == "New Name"
    
    def test_dispositivo_set_nombre_vacio(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
            dispositivo.set_nombre("")
    
    def test_dispositivo_set_nombre_solo_espacios(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
            dispositivo.set_nombre("   ")
    
    def test_dispositivo_set_consumo_energetico_valido(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        dispositivo.set_consumo_energetico(200.0)

        assert dispositivo.get_consumo_energetico() == 200.0
    
    def test_dispositivo_set_consumo_energetico_cero(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        dispositivo.set_consumo_energetico(0.0)

        assert dispositivo.get_consumo_energetico() == 0.0
    
    def test_dispositivo_set_consumo_energetico_negativo(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        with pytest.raises(ValueError, match="El consumo energético no puede ser negativo"):
            dispositivo.set_consumo_energetico(-50.0)
    
    def test_dispositivo_encender_apagado(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)
        assert dispositivo.get_estado() is False

        resultado = dispositivo.encender()

        assert resultado is True
        assert dispositivo.get_estado() is True
    
    def test_dispositivo_encender_ya_encendido(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)
        dispositivo.encender()  # Encender primero
        assert dispositivo.get_estado() is True

        resultado = dispositivo.encender()

        assert resultado is False
        assert dispositivo.get_estado() is True
    
    def test_dispositivo_apagar_encendido(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)
        dispositivo.encender()
        assert dispositivo.get_estado() is True

        resultado = dispositivo.apagar()

        assert resultado is True
        assert dispositivo.get_estado() is False
    
    def test_dispositivo_apagar_ya_apagado(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)
        assert dispositivo.get_estado() is False

        resultado = dispositivo.apagar()

        assert resultado is False
        assert dispositivo.get_estado() is False
    
    def test_dispositivo_crear_dispositivo_exitoso(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        resultado = dispositivo.crear_dispositivo()

        assert resultado is True
    
    def test_dispositivo_buscar_por_nombre_exitoso(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        resultado = dispositivo.buscar_por_nombre("Test Device")

        assert resultado is True
    
    def test_dispositivo_buscar_por_nombre_case_insensitive(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        resultado = dispositivo.buscar_por_nombre("test device")

        assert resultado is True
    
    def test_dispositivo_buscar_por_nombre_no_encontrado(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        resultado = dispositivo.buscar_por_nombre("Other Device")

        assert resultado is False
    
    def test_dispositivo_listar_dispositivos(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        resultado = dispositivo.listar_dispositivos()

        assert isinstance(resultado, dict)
        assert resultado['id'] == 1
        assert resultado['nombre'] == "Test Device"
        assert resultado['tipo'] == "Test Type"
        assert resultado['marca'] == "Test Brand"
        assert resultado['modelo'] == "Test Model"
        assert resultado['estado'] == "Apagado"
        assert resultado['consumo_energetico'] == 100.5
        assert 'fecha_creacion' in resultado
    
    def test_dispositivo_listar_dispositivos_encendido(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)
        dispositivo.encender()

        resultado = dispositivo.listar_dispositivos()

        assert resultado['estado'] == "Encendido"
    
    def test_dispositivo_eliminar_por_nombre_exitoso(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        resultado = dispositivo.eliminar_por_nombre()

        assert resultado is True
    
    def test_dispositivo_devolver_lista_de_dispositivos(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        resultado = dispositivo.devolver_lista_de_dispositivos()

        assert isinstance(resultado, list)
        assert len(resultado) == 1
        assert isinstance(resultado[0], dict)
        assert resultado[0]['id'] == 1
    
    def test_dispositivo_str_representacion(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        resultado = str(dispositivo)

        assert "Test Type" in resultado
        assert "Test Device" in resultado
        assert "Test Brand" in resultado
        assert "Test Model" in resultado
    
    def test_dispositivo_automatizaciones_lista_vacia_inicial(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        automatizaciones = dispositivo.get_automatizaciones()

        assert isinstance(automatizaciones, list)
        assert len(automatizaciones) == 0
    
    def test_dispositivo_automatizaciones_copia_segura(self):
        dispositivo = DispositivoConcreto(1, "Test Device", "Test Type", "Test Brand", "Test Model", 100.5)

        automatizaciones1 = dispositivo.get_automatizaciones()
        automatizaciones2 = dispositivo.get_automatizaciones()

        assert automatizaciones1 is not automatizaciones2  # Diferentes objetos
        assert automatizaciones1 == automatizaciones2  # Mismo contenido
