# app/conversor_tiempo.py
"""
Módulo que contiene las operaciones de conversión de unidades de tiempo.

Este módulo proporciona funciones para realizar conversiones entre diferentes
unidades de tiempo:
- Segundos
- Minutos
- Horas
- Días
- Semanas
- Meses (promedio de 30.44 días)
- Años (365.25 días)

Todas las funciones aceptan números de punto flotante como entrada y
devuelven el resultado como un número de punto flotante.
"""


def segundos_a_minutos(segundos):
    """
    Convierte segundos a minutos.

    Args:
        segundos (float): Cantidad de segundos a convertir.

    Returns:
        float: Equivalente en minutos.
    """
    return segundos / 60


def segundos_a_horas(segundos):
    """
    Convierte segundos a horas.

    Args:
        segundos (float): Cantidad de segundos a convertir.

    Returns:
        float: Equivalente en horas.
    """
    return segundos / 3600


def segundos_a_dias(segundos):
    """
    Convierte segundos a días.

    Args:
        segundos (float): Cantidad de segundos a convertir.

    Returns:
        float: Equivalente en días.
    """
    return segundos / 86400


def segundos_a_semanas(segundos):
    """
    Convierte segundos a semanas.

    Args:
        segundos (float): Cantidad de segundos a convertir.

    Returns:
        float: Equivalente en semanas.
    """
    return segundos / 604800


def minutos_a_segundos(minutos):
    """
    Convierte minutos a segundos.

    Args:
        minutos (float): Cantidad de minutos a convertir.

    Returns:
        float: Equivalente en segundos.
    """
    return minutos * 60


def minutos_a_horas(minutos):
    """
    Convierte minutos a horas.

    Args:
        minutos (float): Cantidad de minutos a convertir.

    Returns:
        float: Equivalente en horas.
    """
    return minutos / 60


def minutos_a_dias(minutos):
    """
    Convierte minutos a días.

    Args:
        minutos (float): Cantidad de minutos a convertir.

    Returns:
        float: Equivalente en días.
    """
    return minutos / 1440


def horas_a_segundos(horas):
    """
    Convierte horas a segundos.

    Args:
        horas (float): Cantidad de horas a convertir.

    Returns:
        float: Equivalente en segundos.
    """
    return horas * 3600


def horas_a_minutos(horas):
    """
    Convierte horas a minutos.

    Args:
        horas (float): Cantidad de horas a convertir.

    Returns:
        float: Equivalente en minutos.
    """
    return horas * 60


def horas_a_dias(horas):
    """
    Convierte horas a días.

    Args:
        horas (float): Cantidad de horas a convertir.

    Returns:
        float: Equivalente en días.
    """
    return horas / 24


def dias_a_segundos(dias):
    """
    Convierte días a segundos.

    Args:
        dias (float): Cantidad de días a convertir.

    Returns:
        float: Equivalente en segundos.
    """
    return dias * 86400


def dias_a_minutos(dias):
    """
    Convierte días a minutos.

    Args:
        dias (float): Cantidad de días a convertir.

    Returns:
        float: Equivalente en minutos.
    """
    return dias * 1440


def dias_a_horas(dias):
    """
    Convierte días a horas.

    Args:
        dias (float): Cantidad de días a convertir.

    Returns:
        float: Equivalente en horas.
    """
    return dias * 24