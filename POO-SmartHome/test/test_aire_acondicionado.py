import pytest
from datetime import datetime
from entidades.AireAcondicionado import AireAcondicionado


class TestAireAcondicionado:
    
    def test_aire_acondicionado_creacion_exitosa(self):
        id_dispositivo = 1
        nombre = "Aire Sala"
        marca = "Samsung"
        modelo = "AR12"
        consumo_energetico = 200.0
        temperatura_actual = 22

        aire = AireAcondicionado(id_dispositivo, nombre, marca, modelo, consumo_energetico, temperatura_actual)

        assert aire.get_id_dispositivo() == id_dispositivo
        assert aire.get_nombre() == nombre
        assert aire.get_tipo() == "Aire Acondicionado"
        assert aire.get_marca() == marca
        assert aire.get_modelo() == modelo
        assert aire.get_consumo_energetico() == consumo_energetico
        assert aire.get_temperatura_actual() == temperatura_actual
        assert aire.get_temperatura_objetivo() == temperatura_actual
        assert aire.get_modo_eco() is False
        assert aire.get_estado() is False
        assert isinstance(aire.get_fecha_creacion(), datetime)
    
    def test_aire_acondicionado_creacion_temperatura_default(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0)

        assert aire.get_temperatura_actual() == 22
        assert aire.get_temperatura_objetivo() == 22
    
    def test_aire_acondicionado_getters_temperatura(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 25)

        assert aire.get_temperatura_actual() == 25
        assert aire.get_temperatura_objetivo() == 25
        assert aire.get_modo_eco() is False
    
    def test_aire_acondicionado_encender_apagado(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)
        assert aire.get_estado() is False

        resultado = aire.encender()

        assert resultado is True
        assert aire.get_estado() is True
    
    def test_aire_acondicionado_encender_ya_encendido(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)
        aire.encender()
        assert aire.get_estado() is True

        resultado = aire.encender()

        assert resultado is False
        assert aire.get_estado() is True
    
    def test_aire_acondicionado_apagar_encendido(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)
        aire.encender()
        assert aire.get_estado() is True

        resultado = aire.apagar()

        assert resultado is True
        assert aire.get_estado() is False
    
    def test_aire_acondicionado_apagar_ya_apagado(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)
        assert aire.get_estado() is False

        resultado = aire.apagar()

        assert resultado is False
        assert aire.get_estado() is False
    
    def test_aire_acondicionado_establecer_temperatura_valida(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        resultado = aire.establecer_temperatura(25)

        assert resultado is True
        assert aire.get_temperatura_objetivo() == 25
    
    def test_aire_acondicionado_establecer_temperatura_minima(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        resultado = aire.establecer_temperatura(16)

        assert resultado is True
        assert aire.get_temperatura_objetivo() == 16
    
    def test_aire_acondicionado_establecer_temperatura_maxima(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        resultado = aire.establecer_temperatura(30)

        assert resultado is True
        assert aire.get_temperatura_objetivo() == 30
    
    def test_aire_acondicionado_establecer_temperatura_muy_baja(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        resultado = aire.establecer_temperatura(15)

        assert resultado is False
        assert aire.get_temperatura_objetivo() == 22
    
    def test_aire_acondicionado_establecer_temperatura_muy_alta(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        resultado = aire.establecer_temperatura(31)

        assert resultado is False
        assert aire.get_temperatura_objetivo() == 22
    
    def test_aire_acondicionado_establecer_temperatura_encendido(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)
        aire.encender()

        resultado = aire.establecer_temperatura(25)

        assert resultado is True
        assert aire.get_temperatura_objetivo() == 25
    
    def test_aire_acondicionado_activar_modo_eco(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)
        assert aire.get_modo_eco() is False

        resultado = aire.activar_modo_eco()

        assert resultado is True
        assert aire.get_modo_eco() is True
    
    def test_aire_acondicionado_activar_modo_eco_multiple_veces(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        resultado1 = aire.activar_modo_eco()
        resultado2 = aire.activar_modo_eco()

        assert resultado1 is True
        assert resultado2 is True
        assert aire.get_modo_eco() is True
    
    def test_aire_acondicionado_herencia_de_dispositivo(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        assert hasattr(aire, 'get_id_dispositivo')
        assert hasattr(aire, 'get_nombre')
        assert hasattr(aire, 'get_tipo')
        assert hasattr(aire, 'get_marca')
        assert hasattr(aire, 'get_modelo')
        assert hasattr(aire, 'get_estado')
        assert hasattr(aire, 'get_consumo_energetico')
        assert hasattr(aire, 'get_fecha_creacion')
        assert hasattr(aire, 'get_automatizaciones')
        assert hasattr(aire, 'crear_dispositivo')
        assert hasattr(aire, 'buscar_por_nombre')
        assert hasattr(aire, 'listar_dispositivos')
        assert hasattr(aire, 'eliminar_por_nombre')
        assert hasattr(aire, 'devolver_lista_de_dispositivos')
        assert hasattr(aire, '__str__')

        assert hasattr(aire, 'encender')
        assert hasattr(aire, 'apagar')

        assert hasattr(aire, 'get_temperatura_actual')
        assert hasattr(aire, 'get_temperatura_objetivo')
        assert hasattr(aire, 'get_modo_eco')
        assert hasattr(aire, 'establecer_temperatura')
        assert hasattr(aire, 'activar_modo_eco')
    
    def test_aire_acondicionado_metodos_heredados_funcionan(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        assert aire.crear_dispositivo() is True

        assert aire.buscar_por_nombre("Aire Sala") is True
        assert aire.buscar_por_nombre("aire sala") is True
        assert aire.buscar_por_nombre("Other Device") is False

        lista = aire.listar_dispositivos()
        assert isinstance(lista, dict)
        assert lista['nombre'] == "Aire Sala"
        assert lista['tipo'] == "Aire Acondicionado"

        assert aire.eliminar_por_nombre() is True

        lista_dispositivos = aire.devolver_lista_de_dispositivos()
        assert isinstance(lista_dispositivos, list)
        assert len(lista_dispositivos) == 1
    
    def test_aire_acondicionado_str_representacion(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        resultado = str(aire)

        assert "Aire Acondicionado" in resultado
        assert "Aire Sala" in resultado
        assert "Samsung" in resultado
        assert "AR12" in resultado
    
    def test_aire_acondicionado_rango_temperaturas_completo(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        for temp in range(16, 31):
            resultado = aire.establecer_temperatura(temp)
            assert resultado is True
            assert aire.get_temperatura_objetivo() == temp
    
    def test_aire_acondicionado_estado_inicial_correcto(self):
        aire = AireAcondicionado(1, "Aire Sala", "Samsung", "AR12", 200.0, 22)

        assert aire.get_estado() is False
        assert aire.get_temperatura_actual() == 22
        assert aire.get_temperatura_objetivo() == 22
        assert aire.get_modo_eco() is False
        assert aire.get_tipo() == "Aire Acondicionado"
        assert isinstance(aire.get_fecha_creacion(), datetime)
