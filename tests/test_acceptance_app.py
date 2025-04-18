import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:5000")

# Configuración del driver (elige uno: Chrome o Firefox)
@pytest.fixture
def browser():
    # Opción 1: Chrome (headless - sin interfaz gráfica)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecuta sin interfaz gráfica
    options.add_argument("--no-sandbox") # Necesario para algunos entornos
    options.add_argument("--disable-dev-shm-usage") # Necesario para algunos entornos
    driver = webdriver.Chrome(options=options)

    # Opción 2: Firefox (headless)
    # options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)

    # Opción 3: Chrome (con interfaz gráfica - para depuración local)
    # driver = webdriver.Chrome()

    # Opción 4: Firefox (con interfaz gráfica)
    # driver = webdriver.Firefox()
    yield driver
    # time.sleep(5)

    driver.quit()


# Función de ayuda para esperar y obtener el resultado
def get_resultado(browser):
    try:
        # Espera HASTA QUE el <h2> sea visible (máximo 10 segundos)
        resultado = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h2"))
        )
        print(resultado.text)
        return resultado.text
    except TimeoutException:
        return "Error: Tiempo de espera agotado esperando el resultado."

# Función auxiliar para encontrar elementos:
def find_elements(browser):
    valor_input = browser.find_element(By.ID, "valor")
    unidad_origen_select = Select(browser.find_element(By.ID, "unidad_origen"))
    unidad_destino_select = Select(browser.find_element(By.ID, "unidad_destino"))
    convertir_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    return valor_input, unidad_origen_select, unidad_destino_select, convertir_button

@pytest.mark.parametrize(
    "valor, unidad_origen, unidad_destino, resultado_esperado",
    [
        ("60", "segundos", "minutos", "60.0 segundos = 1.0 minutos"),
        ("1", "minutos", "segundos", "1.0 minutos = 60.0 segundos"),
        ("2", "horas", "minutos", "2.0 horas = 120.0 minutos"),
        ("1", "dias", "horas", "1.0 dias = 24.0 horas"),
        ("10", "minutos", "minutos", "10.0 minutos = 10.0 minutos"),
        ("abc", "minutos", "segundos", "Error: Introduce un valor numérico válido"),
    ],
)
def test_conversor_tiempo(browser, valor, unidad_origen, unidad_destino, resultado_esperado):
    browser.get(BASE_URL)

    # Encuentra los elementos de la página usando la función auxiliar
    valor_input, unidad_origen_select, unidad_destino_select, convertir_button = find_elements(browser)

    # Realiza la operación:
    valor_input.send_keys(valor)
    unidad_origen_select.select_by_value(unidad_origen)
    unidad_destino_select.select_by_value(unidad_destino)
    convertir_button.click()


    # Verifica con la función auxiliar:
    assert resultado_esperado in get_resultado(browser)