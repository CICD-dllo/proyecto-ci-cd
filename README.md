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
```

## Estrategias de Despliegue y Rollback

Este proyecto implementa dos estrategias avanzadas para garantizar despliegues seguros y confiables:

### Rolling Update

Los despliegues se realizan mediante una estrategia de "Rolling Update" donde:

1. Se lanza la nueva versión gradualmente
2. Las instancias se reemplazan una por una
3. El tráfico se redirige automáticamente a las nuevas instancias
4. Las verificaciones de salud aseguran que solo instancias saludables reciban tráfico

Esto se implementa mediante la siguiente configuración en ECS:
- `DesiredCount: 2`: Mantenemos al menos dos instancias para permitir actualizaciones sin tiempo de inactividad
- `DeploymentConfiguration`: Controla el porcentaje mínimo y máximo de instancias durante los despliegues
- `DeploymentController: ECS`: Utiliza el controlador de despliegue estándar de ECS

### Rollback Automático

El sistema está configurado para realizar rollback automático cuando ocurren fallos:

1. Si una nueva versión no pasa las verificaciones de salud
2. Si el despliegue no se estabiliza en el tiempo esperado

Esto se implementa mediante:
- `DeploymentCircuitBreaker`: Detecta cuando un despliegue está fallando
- `Rollback: true`: Vuelve automáticamente a la versión anterior cuando se detectan fallos

### Rollback Manual

Además del rollback automático, se puede forzar un rollback manual:

1. Añadiendo `[rollback]` en el mensaje del commit
2. Si el despliegue falla, el job `rollback-prod` se ejecutará automáticamente

Para realizar un rollback manual:
```bash
git commit -m "Algún cambio [rollback]"
git push origin main
```

Este proceso revierte a la versión anterior de la aplicación, asegurando que el servicio vuelva a un estado conocido y estable.
