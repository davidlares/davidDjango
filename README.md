## DavidDjango

Proyecto educacional sobre el desarrollo de API REST con Django en su version 2.12, y Django Rest Framework para elaboración de un CRUD System de Videos (name, description y slug)

## Requisitos

  - Mysql 5.x instalado
  - Pypi - Package Package Index instalado
  - virtualEnv para el soporte de multiples versiones de las dependencias (ver requirements.txt)

##  Uso Local

  - luego de clonado o descargado el repositorio, asegurense de tener un entorno VirtualEnv corriendo
  - Creen un superusuario para el Django admin a traves de `django-admin createsuperuser`
  - Corran las migraciones de la app `video` y utilicen la API a través de Postman o CURL

## API Endpoints

  - /api/v1/videos [GET, POST]
  - /api/v1/video/{N} [GET, PUT, DELETE]

## Créditos
- [David E Lares S](https://twitter.com/@davidlares3)

## Licencia

- [MIT](https://opensource.org/licenses/MIT)
