# WOOWUP Challenge

- Problema: se necesita crear una API que me permita enviar un correo electronico, donde debe intentar con diferentes proveedores de correo si alguno falla debe intentar con el siguiente configurado.
- Solucion: 
  - Se crea una API(Python+FastAPI) que tiene configurado el envio de correo con SPARKPOST, MAILJET y SMTP Gmail, usando inyeccion de dependencias para la configuracion, el patron strategy(SPARKPOST, MAILJET y SMTP Gmail)
  - se crea front usando JS, CSS y HTML para consumir la API.

## Contenido

- [WOOWUP Challenge](#woowup-challenge)
  - [Contenido](#contenido)
  - [Demo](#demo)
  - [Backend](#backend)
    - [Pre-requisitos](#pre-requisitos)
    - [Librerias](#librerias)
    - [Instalacion](#instalacion)
    - [Ejecucion](#ejecucion)
  - [Frontend](#frontend)
    - [Pre-requisitos](#pre-requisitos-1)
    - [Librerias](#librerias-1)
    - [Ejecucion](#ejecucion-1)

## Demo

Use RailWay para desplegar la aplicacion.

- [Frontend](https://gregarious-solace-production.up.railway.app) 
- [API](https://woowup-challenge-production.up.railway.app)
- [API DOCS](https://woowup-challenge-production.up.railway.app/docs)

## Backend

### Pre-requisitos

- Python 3.6+ Tengo experiencia trabajando con esta de 6 años aprox.

### Librerias

- FastAPI: use esta libreria porque me permite crear, configurar(inyeccion de dependencias, modelos, rutas) y documentar rapidamente un API.
- Sparkpost: SDK que permite enviar y recibir correos usando  los servicios de [SparkPost](https://developers.sparkpost.com) 
  - **NOTA**: actualmente el correo no se envia con este servidor debido a que cuenta que configure fue bloqueada por razones que desconozco.
- MailJet: SDK que permite enviar y recibir correos usando  los servicios de [MailJet](https://dev.mailjet.com) 
  - **NOTA**: actualmente el correo no se envia con este servidor debido a que cuenta que configure fue bloqueada por razones que desconozco.
- SMTP Google: se usa SMTPlib para configurar el envio del correo electrónico usando Google. 

### Instalacion

1. Ingresar a la carpeta de backend: `cd back` 
2. Crear de entorno local: `python -m venv .venv`
3. Activar entorno local:
   - Windows cmd: `.venv\Scripts\activate.bat` 
   - Lunix o MacOS: `source .venv/bin/activate`
4. Instalacion de dependencias: `pip install -r requirements.txt`
5. Desactivar entorno local(opcional): `deactivate`

### Ejecucion

1. Ingresar a la carpeta de backend: `cd back` 
2. Ejecutar el servidor:
   - Modo desarrollador: `fastapi dev api/main.py`
   - Uvicorn: `uvicorn api.main:app --host 0.0.0.0 --port 8000`
3. Ruta del API: `localhost:8000`
4. Docuemntacion del API: `localhost:8000/docs`

## Frontend

### Pre-requisitos

- Python 3.6+

### Librerias

- Tagify: la utilice para crear el `<input> "recipients"` para agregar o quitar correos de destinatarios.
- Notyf: la utilice para mostrar en notificacion de cuando se genera alguna validacion en el formulario y cuando se recibe una respuesta de la API..
- Joi-browser: la utilice para hacer las validaciones del formulario usando un schema.
- Quill: la utilice para `<input> "content"` que genera texto enriquecido como html.

### Ejecucion

1. Ingresar a carpeta de frontend: `cd front`
2. Ejecutar el servidor con python: `python -m http.server 8001`
3. Ingresar en el navegador usando la ruta: `localhost:8001`

