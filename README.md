# 📝 Learning Log

**Learning Log** es una aplicación web desarrollada con **Python y Django**, que permite a los usuarios registrar y gestionar temas sobre los que están aprendiendo, junto con entradas relacionadas. Este proyecto forma parte del libro *"Python Crash Course"* de Eric Matthes, y está diseñado para enseñar los fundamentos del desarrollo web con Django.

---

## 🌐 Tecnologías utilizadas

- **Python**
- **Django** (framework web)
- **SQLite** (base de datos por defecto de Django)
- **HTML/CSS** (plantillas básicas para frontend)

---

## 🚀 Funcionalidades principales

- ✅ Registro e inicio de sesión de usuarios
- ✅ Creación de temas de aprendizaje personalizados
- ✅ Añadir entradas relacionadas a cada tema
- ✅ Ver listado de temas y entradas
- ✅ Restringir cada usuario a sus propios datos
- ✅ Interfaz sencilla y limpia para gestionar el contenido

---

## 🎯 Objetivos del proyecto

- Aprender el flujo básico de trabajo con Django
- Crear modelos, vistas y templates
- Usar el panel de administración de Django
- Implementar autenticación de usuarios
- Comprender el sistema de URLs y vistas basadas en clases/funciones

# Learning Log

## Overview

A web application called learning log that allows users to record the topics they are interested in and make journal entries as they learn about each topic. The home page describes the site and will invite users to register or log in. Once the session has started. The user can create new topics, add entries and read and edit existing ones.


## Local Development

To run this project locally, follow these steps:

1. Clone the repository:

git clone https://github.com/yourusername/your-project.git
cd your-project


2. Activate the virtual environment:

source ll_env/bin/activate

2.1 Or create an venv, activate it and Install dependencies:

pip install -r requirements.txt


3. Run the development server:

python manage.py runserver


4. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).

## Deployment to Heroku

To deploy this project to Heroku, you can use the provided configuration files:

- `requirements.txt`: Lists the Python dependencies required for your application.
- `runtime.txt`: Specifies the Python version to use.
- `Procfile`: Specifies how to run your application on Heroku.

Follow these steps to deploy:

1. Create a new Heroku app:

heroku create


2. Push your code to Heroku:

git push heroku master


3. Run any necessary migrations:

heroku run python manage.py migrate


4. Open your deployed application in your web browser with:

heroku open
