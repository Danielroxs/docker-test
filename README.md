# Arkham AI - TARS Engine Simulator

Este repositorio contiene un simulador de proceso de Inteligencia Artificial para la plataforma de **Arkham Technologies**. El objetivo es demostrar el despliegue de microservicios aislados utilizando **Docker**.

## 🛠️ Tecnologías utilizadas
- **Python 3.9-slim**: Motor de ejecución ligero.
- **Docker**: Contenerización y aislamiento de procesos.
- **GitHub Codespaces**: Entorno de desarrollo remoto.

## Cómo ejecutar este proyecto
Para correr el simulador de TARS en cualquier entorno con Docker:

1. **Construir la imagen:**
   ```bash
   docker build -t arkham-tars-engine .

2. **Ejecutar el contenedor:**
   ```bash
docker run --rm -e PYTHONUNBUFFERED=1 --name engine-v1 arkham-tars-engine
