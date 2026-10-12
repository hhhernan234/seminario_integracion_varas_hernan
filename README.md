Seminario de Integración

Autor: Hernán Varas

Materia: Seminario de Integración

📌 Descripción del Cuestionario / Proyecto

Este repositorio contiene los contenidos, guías y ejercicios prácticos de la materia Seminario de Integración. El objetivo principal es la consolidación y repaso de fundamentos de Python, avanzando gradualmente hacia la integración de tecnologías modernas de backend y frontend para la construcción de arquitectura web completa e interconectada.

🚀 Tecnologías Utilizadas

Python Ecosystem: Python 3.x, venv, uv (Fast Package Manager), FastAPI.

Node.js Ecosystem: Node.js, NestJS.

Frontend Ecosystem: Angular, TypeScript.

Herramientas de Soporte: Git, Docker (opcional/despliegue).

📚 Programa y Contenidos por Temas

Tema 1: Repaso de Fundamentos de Python

Sintaxis básica, estructuras de datos avanzadas (listas, diccionarios, sets).

Programación Orientada a Objetos (POO) en Python.

Manejo de excepciones, módulos y paquetes.

Asincronía con asyncio y tipos de datos con Pydantic.

Tema 2: Entornos Virtuales y Gestión de Dependencias

Aislamiento de entornos con venv.

Introducción y gestión ultra-rápida de paquetes con uv.

Gestión de dependencias y archivos de configuración (pyproject.toml, requirements.txt).

Tema 3: Desarrollo Backend con Python (FastAPI)

Principios de APIs RESTful.

Rutas, controladores y manejo de peticiones (GET, POST, PUT, DELETE).

Inyección de dependencias y middlewares.

Validación de datos y documentación automática con Swagger / OpenAPI.

Tema 4: Ecosistema Node.js y NestJS

Repaso de JavaScript Asíncrono / TypeScript.

Introducción a la arquitectura de NestJS (Módulos, Controladores, Servicios).

Inyección de dependencias en NestJS y DTOs (Data Transfer Objects).

Comparativa y casos de uso: FastAPI vs NestJS.

Tema 5: Frontend con Angular

Fundamentos de Angular: Componentes, Servicios y Módulos.

Enrutamiento (Routing) y navegación.

Consumo de APIs REST (FastAPI / NestJS) mediante HttpClient.

Manejo de estado local y reactividad con RxJS.

Tema 6: Integración Full Stack y Buenas Prácticas

Comunicación cliente-servidor y políticas CORS.

Estrategias de autenticación y autorización (JWT).

Estructura y organización de proyectos multitecnología.

Control de versiones avanzado con Git y .gitignore unificado.

🛠️ Requisitos Previos e Instalación

Prerrequisitos

Python 3.10+

Node.js 18+ / npm / pnpm

Angular CLI (npm install -g @angular/cli)

uv instalado (pip install uv o mediante instalador oficial)

Configuración del Entorno Python (con uv)

# Crear entorno virtual con uv
uv venv .venv

# Activar entorno virtual
# En Linux/macOS:
source .venv/bin/activate
# En Windows:
.venv\Scripts\activate

# Instalación de dependencias
uv pip install -r requirements.txt


Configuración de Node.js / Angular

# Instalar dependencias en el frontend/backend Node.js
npm install

# Iniciar servidor de desarrollo en Angular
ng serve


📝 Licencia y Autoría

Autor: Hernán Varas

Creado como material de estudio y aplicación para la materia Seminario de Integración.