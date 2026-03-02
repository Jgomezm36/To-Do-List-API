# 📝 To-Do List API con FastAPI

Esta es una API REST profesional construida con **FastAPI** para la gestión de tareas (To-Do List). El proyecto utiliza un sistema de persistencia local basado en un archivo **JSON**, lo que permite mantener los datos sin necesidad de configurar una base de datos externa.

## 🚀 Características
* **CRUD Completo:** Crear, leer, actualizar y eliminar tareas.
* **Persistencia Local:** Almacenamiento automático en `tasks.json`.
* **Validación de Datos:** Uso de **Pydantic** para garantizar la integridad de la información.
* **ID Únicos:** Generación automática de UUIDs para cada tarea.
* **Documentación Automática:** Swagger UI integrada por defecto.

---

## 🛠️ Requisitos Técnicos
* **Lenguaje:** Python 3.9 o superior.
* **Framework:** FastAPI.
* **Servidor ASGI:** Uvicorn.
* **Gestión de Datos:** Pydantic y JSON.

---

## 📥 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
   cd tu-repositorio

2. Crear y activar un entorno virtual:
# En Windows
python -m venv venv
.\venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/actívate

3.Instalar las dependencias:
pip install fastapi uvicorn pydantic

🏃 Cómo ejecutar la aplicación
Para iniciar el servidor de desarrollo, utiliza el siguiente comando:
uvicorn main:app --reload
Una vez ejecutado, la API estará disponible en: http://127.0.0.1:8000
📑 Prueba de Endpoints
La API puede probarse de dos formas principales:

1. Swagger UI (Recomendado)
Accede a la documentación interactiva en: http://127.0.0.1:8000/docs. Desde aquí puedes enviar peticiones directamente sin usar herramientas externas.
2. Postman o Insomnia
Puedes realizar peticiones HTTP a los siguientes endpoints:
Método,Endpoint,Descripción
GET,/tasks,Obtiene todas las tareas.
GET,/tasks/{id},Obtiene una tarea específica por su ID.
POST,/tasks,"Crea una nueva tarea (Título, Descripción opcional)."
PUT,/tasks/{id},Actualiza el estado o datos de una tarea existente.
DELETE,/tasks/{id},Elimina una tarea de la lista.

📂 Estructura del Proyecto

├── main.py          # Definición de rutas y lógica de la API
├── models.py        # Modelos de datos (Pydantic)
├── storage.py       # Funciones de lectura/escritura del archivo JSON
├── tasks.json       # Base de datos local (se crea automáticamente)
└── README.md        # Documentación del proyecto
