##### Made by **JR_DEV**
## **DJANGO API TEMPLATE**

[![N|Solid](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRwnr7XMtqqtRAb_z1AMcHAvijwFhhRTmYBn4YnEjUa4Br5ZO8ZVSQKH6FKov2lNo7W1S-nEb0=w3584-h2082)](https://drive.google.com/file/d/1r7-40jX948-rlMRe1vKdcbPODAgh49j-/preview)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Esta es una plantilla para comenzar tus proyectos de Django con una base bien sólida. Esta pensada para ser modular y escalable a si que no tendrás que preocuparte de nada más que de empezar a programar.

## Highlights

- Docker configurado para usar con postgres
- Settings desacopladas según variables de entorno (Una para debug, otra dev, y otra prod)
- Api versionada por defecto
- Usuario custom ya creado
- Rest framework, django filters, Rest framework authtoken, Rest framework jwt ya estan ready to go
- Cors headers metidos para que tu realices las configuraciones que te convengan

## Installation

Primero debemos clonar el repositorio y situarnos dentro de el.

```sh
git clone https://github.com/josericardopenase/django_base_template.git
cd django_base_template
```
tenemos dos tipos de instalaciones, usando docker o sin usarlo.

**Sin docker:**

Simplemente clona el repositorio instala las dependencias con pipenv y realiza las migraciones.

```sh

pipenv install
python3 manage.py migrate
python3 manage.py runserver
```

**Con docker**

```sh
docker build . -t django-template
docker run -p 8000:8000 django-template
```

## Variables de entorno

Primero tenemos que crear un archivo .env en la raiz
```sh
touch .env
vim .env
```
Para hacer funcionar la plantilla sin ningún tipo de problema tendremos que configurar las siguientes variables de entorno:

**DJANGO_SECRET_KEY="clave secreta de django"
DJANGO_ENV="DEBUG" | "DEV" | "PROD"**

Estas de aqui son solo para producción, para conectar nuestra db de postgresql

**POSTGRES_NAME=""
POSTGRES_USER=""
POSTGRES_PASSWORD=""
POSTGRES_HOST=""
POSTGRES_PORT=""**

## Development

¿Quieres contribuir?
Genial! Contactame al github y hablamos :)
