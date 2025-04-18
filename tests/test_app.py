# tests/test_app.py
import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data  # Asumiendo que la plantilla HTML comienza con <!DOCTYPE html>

def test_index_post_segundos_a_minutos(client):
    response = client.post('/', data={'valor': '60', 'unidad_origen': 'segundos', 'unidad_destino': 'minutos'})
    assert response.status_code == 200
    assert b'60.0 segundos = 1.0 minutos' in response.data

def test_index_post_minutos_a_segundos(client):
    response = client.post('/', data={'valor': '1', 'unidad_origen': 'minutos', 'unidad_destino': 'segundos'})
    assert response.status_code == 200
    assert b'1.0 minutos = 60.0 segundos' in response.data

def test_index_post_horas_a_minutos(client):
    response = client.post('/', data={'valor': '2', 'unidad_origen': 'horas', 'unidad_destino': 'minutos'})
    assert response.status_code == 200
    assert b'2.0 horas = 120.0 minutos' in response.data

def test_index_post_dias_a_horas(client):
    response = client.post('/', data={'valor': '1', 'unidad_origen': 'dias', 'unidad_destino': 'horas'})
    assert response.status_code == 200
    assert b'1.0 dias = 24.0 horas' in response.data

def test_index_post_misma_unidad(client):
    response = client.post('/', data={'valor': '10', 'unidad_origen': 'minutos', 'unidad_destino': 'minutos'})
    assert response.status_code == 200
    assert b'10.0 minutos = 10.0 minutos' in response.data

def test_index_post_conversion_no_soportada(client):
    response = client.post('/', data={'valor': '10', 'unidad_origen': 'semanas', 'unidad_destino': 'minutos'})
    assert response.status_code == 200
    assert b'Error: Conversi\xc3\xb3n no soportada' in response.data

def test_index_post_valor_invalido(client):
    response = client.post('/', data={'valor': 'abc', 'unidad_origen': 'minutos', 'unidad_destino': 'segundos'})
    assert response.status_code == 200
    assert b'Error: Introduce un valor num\xc3\xa9rico v\xc3\xa1lido' in response.data

def test_health_endpoint(client):
    """
    Prueba el endpoint de healthcheck.
    Verifica que el endpoint /health 
    responda con estado 200 y el mensaje 'OK'.
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert b'OK' in response.data