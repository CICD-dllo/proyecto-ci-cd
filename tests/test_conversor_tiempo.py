# tests/test_conversor_tiempo.py
import pytest
from app.conversor_tiempo import (
    segundos_a_minutos, segundos_a_horas, segundos_a_dias,
    minutos_a_segundos, minutos_a_horas, minutos_a_dias,
    horas_a_segundos, horas_a_minutos, horas_a_dias,
    dias_a_segundos, dias_a_minutos, dias_a_horas, segundos_a_semanas
)

def test_segundos_a_minutos():
    assert segundos_a_minutos(60) == 1
    assert segundos_a_minutos(120) == 2
    assert segundos_a_minutos(90) == 1.5

def test_segundos_a_horas():
    assert segundos_a_horas(3600) == 1
    assert segundos_a_horas(7200) == 2
    assert segundos_a_horas(5400) == 1.5

def test_segundos_a_dias():
    assert segundos_a_dias(86400) == 1
    assert segundos_a_dias(172800) == 2
    assert segundos_a_dias(129600) == 1.5

def test_segundos_a_semanas():
    assert segundos_a_semanas(604800) == 1
    assert segundos_a_semanas(1209600) == 2
    assert segundos_a_semanas(907200) == 1.5

def test_minutos_a_segundos():
    assert minutos_a_segundos(1) == 60
    assert minutos_a_segundos(2) == 120
    assert minutos_a_segundos(1.5) == 90

def test_minutos_a_horas():
    assert minutos_a_horas(60) == 1
    assert minutos_a_horas(120) == 2
    assert minutos_a_horas(90) == 1.5

def test_minutos_a_dias():
    assert minutos_a_dias(1440) == 1
    assert minutos_a_dias(2880) == 2
    assert minutos_a_dias(2160) == 1.5

def test_horas_a_segundos():
    assert horas_a_segundos(1) == 3600
    assert horas_a_segundos(2) == 7200
    assert horas_a_segundos(1.5) == 5400

def test_horas_a_minutos():
    assert horas_a_minutos(1) == 60
    assert horas_a_minutos(2) == 120
    assert horas_a_minutos(1.5) == 90

def test_horas_a_dias():
    assert horas_a_dias(24) == 1
    assert horas_a_dias(48) == 2
    assert horas_a_dias(36) == 1.5

def test_dias_a_segundos():
    assert dias_a_segundos(1) == 86400
    assert dias_a_segundos(2) == 172800
    assert dias_a_segundos(1.5) == 129600

def test_dias_a_minutos():
    assert dias_a_minutos(1) == 1440
    assert dias_a_minutos(2) == 2880
    assert dias_a_minutos(1.5) == 2160

def test_dias_a_horas():
    assert dias_a_horas(1) == 24
    assert dias_a_horas(2) == 48
    assert dias_a_horas(1.5) == 36