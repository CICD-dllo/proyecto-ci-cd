# Conversor de Unidades de Tiempo - Proyecto CI/CD

Este proyecto implementa un conversor de unidades de tiempo web utilizando Flask, con un pipeline completo de integración continua y despliegue continuo (CI/CD).

## Funcionalidades

- Conversión entre diferentes unidades de tiempo:
  - Segundos
  - Minutos
  - Horas
  - Días
  - Semanas

## Tecnologías

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Testing**: PyTest, Selenium
- **CI/CD**: GitHub Actions
- **Calidad de código**: SonarCloud, Black, Flake8, Pylint
- **Containerización**: Docker
- **Infraestructura como código**: AWS CloudFormation
- **Despliegue**: AWS ECS Fargate con Application Load Balancer

## Estructura del Proyecto

```
├── app/                    # Código fuente de la aplicación
│   ├── __init__.py
│   ├── app.py              # Aplicación Flask
│   ├── conversor_tiempo.py # Lógica de negocio (conversión de tiempo)
│   └── templates/          # Plantillas HTML
│       └── index.html      # Interfaz de usuario
├── tests/                  # Tests automatizados
│   ├── test_conversor_tiempo.py    # Tests unitarios
│   ├── test_app.py                 # Tests de integración
│   ├── test_acceptance_app.py      # Tests de aceptación con Selenium
│   └── test_smoke_app.py           # Tests de humo para producción
├── .github/workflows/      # Archivos de configuración GitHub Actions
│   ├── ci.yml              # Workflow de CI
│   └── ci-cd.yml           # Workflow completo de CI/CD con despliegue
├── Dockerfile              # Definición de imagen Docker
├── requirements.txt        # Dependencias del proyecto
├── template.yaml           # Plantilla AWS CloudFormation
├── sonar-project.properties # Configuración SonarCloud
└── README.md               # Este archivo
```

## Pipeline CI/CD

El proyecto utiliza GitHub Actions para automatizar:

1. **Integración Continua**:
   - Formateo de código (Black)
   - Análisis estático (Flake8, Pylint)
   - Tests unitarios y de integración
   - Análisis de calidad (SonarCloud)
   - Construcción y publicación de imagen Docker

2. **Despliegue Continuo**:
   - Despliegue a entorno de Staging
   - Tests de aceptación en Staging
   - Despliegue a Producción
   - Tests de humo en Producción

## Ejecución Local

1. Clonar el repositorio
2. Instalar dependencias con `pip install -r requirements.txt`
3. Ejecutar `flask --app app.app run`
4. Abrir http://localhost:5000 en un navegador

## Ejecutar Tests

```bash
# Tests unitarios y de integración
pytest --ignore=tests/test_acceptance_app.py --ignore=tests/test_smoke_app.py

# Tests de aceptación (requiere Flask en ejecución)
pytest tests/test_acceptance_app.py