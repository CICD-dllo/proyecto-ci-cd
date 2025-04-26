# tests/test_smoke_app.py
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

# Fixture para configurar el navegador (similar a las pruebas de aceptación)
@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecuta sin interfaz gráfica
    options.add_argument("--no-sandbox") # Necesario para algunos entornos
    options.add_argument("--disable-dev-shm-usage") # Necesario para algunos entornos
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_smoke_test(browser):
    """SMOKE TEST: Verifica carga básica y título."""
    # Lee la URL de producción desde una variable de entorno

     # Usar la variable de entorno APP_BASE_URL que inyectaremos
     # en el pipeline con la URL del ALB de Producción
    app_url = os.environ.get("APP_BASE_URL", "http://localhost:5000")
    print(f"Smoke test ejecutándose contra: {app_url}") # Imprime para depuración
    try:
        browser.get(app_url + "/")
        print(f"Título de la página: {browser.title}")
        
        if False: #condicional para simular un fallo
            # Verifica que el título contenga "Conversor de Unidades de Tiempo"
            assert "Conversor de Unidades de Tiempo" in browser.title
        else:
            # Forzamos un fallo cambiando la aserción para que busque un título incorrecto
            assert False

        h1_element = browser.find_element(By.TAG_NAME, "h1")
        print(f"Texto H1: {h1_element.text}")
        assert h1_element.text == "Conversor de Unidades de Tiempo" # Verifica el texto del H1
        
        # Reactivamos la aserción que siempre fallará para probar el rollback
        print("PRUEBA DE ROLLBACK: Esta aserción fallará intencionalmente")
        assert False, "Fallo intencional para probar el mecanismo de rollback [rollback]"
        
        print("Smoke test pasado exitosamente.")
    except Exception as e:
        print(f"Smoke test falló: {e}")
        # Opcional: tomar captura de pantalla si falla
        # browser.save_screenshot('smoke_test_failure.png')
         # Vuelve a lanzar la excepción para que pytest marque el test como fallido
        raise