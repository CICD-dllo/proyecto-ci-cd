# app/app.py
"""
Módulo principal de la aplicación de conversión de unidades de tiempo.

Este módulo implementa una aplicación web Flask que proporciona una
interfaz para realizar conversiones entre diferentes unidades de tiempo.
La aplicación maneja solicitudes GET y POST, procesa los datos del formulario y
muestra los resultados de la conversión.

La aplicación incluye manejo de errores para:
- Entradas no numéricas
- Operaciones de conversión no válidas
"""

from flask import Flask, render_template, request

# Importación de funciones de conversión
from . import conversor_tiempo

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Maneja las solicitudes GET y POST para la página principal del conversor.

    Esta función procesa el valor, la unidad de origen y la unidad de destino
    enviados a través del formulario, realiza la conversión correspondiente y
    devuelve el resultado.

    Returns:
        str: Una plantilla HTML renderizada con el resultado de la
        conversión o None si no se ha realizado ninguna operación.

    Raises:
        ValueError: Si el valor ingresado no es válido.
    """
    resultado = None
    if request.method == "POST":
        try:
            valor = float(request.form["valor"])
            unidad_origen = request.form["unidad_origen"]
            unidad_destino = request.form["unidad_destino"]

            # Matriz de conversión
            # mapea combinaciones de origen y destino a funciones
            conversiones = {
                ("segundos", "minutos"): conversor_tiempo.segundos_a_minutos,
                ("segundos", "horas"): conversor_tiempo.segundos_a_horas,
                ("segundos", "dias"): conversor_tiempo.segundos_a_dias,
                ("segundos", "semanas"): conversor_tiempo.segundos_a_semanas,
                ("minutos", "segundos"): conversor_tiempo.minutos_a_segundos,
                ("minutos", "horas"): conversor_tiempo.minutos_a_horas,
                ("minutos", "dias"): conversor_tiempo.minutos_a_dias,
                ("horas", "segundos"): conversor_tiempo.horas_a_segundos,
                ("horas", "minutos"): conversor_tiempo.horas_a_minutos,
                ("horas", "dias"): conversor_tiempo.horas_a_dias,
                ("dias", "segundos"): conversor_tiempo.dias_a_segundos,
                ("dias", "minutos"): conversor_tiempo.dias_a_minutos,
                ("dias", "horas"): conversor_tiempo.dias_a_horas,
            }

            # Verificar si la conversión es válida
            clave_conversion = (unidad_origen, unidad_destino)
            if clave_conversion in conversiones:
                # Ejecutar la función de conversión correspondiente
                funcion_conversion = conversiones[clave_conversion]
                resultado_valor = funcion_conversion(valor)
                resultado = f"{valor} {unidad_origen} = "
                resultado += f"{resultado_valor} {unidad_destino}"
            elif unidad_origen == unidad_destino:
                # Misma unidad, no hay conversión
                resultado = f"{valor} {unidad_origen} = "
                resultado += f"{valor} {unidad_destino}"
            else:
                resultado = "Error: Conversión no soportada"

        except ValueError:
            resultado = "Error: Introduce un valor numérico válido"

    return render_template("index.html", resultado=resultado)

# Endpoint de verificación de salud
@app.route("/health")
def health():
    """
    Endpoint de verificación de salud.
    """
    return "OK", 200


if __name__ == "__main__":  # pragma: no cover
    # Quita debug=True para producción
    app.run(port=5000, host="0.0.0.0")
