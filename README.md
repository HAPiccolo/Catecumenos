# Catecumenos
## Simple sistema de registro de catecúmenos realizado en DJango para la materia Practica Profesionalizante.


Pasos para correrlo:

1) Clonamos el repositorio:
  ```bash
  git clone https://github.com/HAPiccolo/Catecumenos.git
  ```

3) Ingresamos a la carpeta:
  ```bash
  cd Catecumenos
  ```
NOTA: si no tiene python3-venv lo instalamos

5) Instalamos python3-venv
  ```bash
  sudo apt install python3-venv
  ``` 

7) Creamos el entorno virtual
  ```bash
  python3 -m venv env
  ```

8) Activamos el entorno virtual
  ```bash
  source env/bin/activate
  ```

10) Una vez activado el entorno virtual creamos la BD aplicando las migraciones
  ```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

11) Creamos el superusario para administrar el panel de admin del proyecto
  ```bash
  python3 manage.py createsuperuser
  ```

11) Corremos el servidor para probar el proyecto
  ```bash
  python3 manage.py runserver
  ```

