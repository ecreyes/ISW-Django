# Requerimientos Previos.
* [Python 3.5.0](https://www.python.org/downloads/)
* [Pyscopg2](http://www.stickpeople.com/projects/python/win-psycopg/)
* [PostgreSQL](https://www.postgresql.org/download/)
* [Yahoo Quote Download](https://github.com/c0redumb/yahoo_quote_download)

## Configurar ambiente de trabajo
1. Instalar Django de manera global, abrir cmd
```=bash
python -m pip install django
```
Esto instalará django en la version más reciente.
2. Instalar VirtualEnv para los entornos virtuales.
```=bash
python -m pip install virtualenv
```
Con esto se instalará virtual env.

3. Para saber que tenemos instalado utilizamos.
```=bash
python -m pip freeze
```

4. Crear un entorno virtual.
Crear una carpeta llamada `ambientes` en el escritorio, esta carpeta servirá para configurar todos los ambientes virtuales.

Una vez dentro de la carpeta ambientes, hay que escribir
```=bash
python -m venv test
```
Este comando creará un entorno virtual.
Dentro de la carpeta `test` que se va a crear hay una carpeta llamada `Scripts` con un archivo `activate.bat`
Hay que entrar a la carpeta `Scripts` y ejecutar el comando `activate.bat` escribiendo solamante
```=bash
activate
```
De esta forma se activara el entorno virtual.
Ahora que esta activado el entorno virtual, hay que instalar Django para el entorno virtual ya que antes estaba instalado de manera global, para instalarlo regresar a la carpeta test y usar
```=bash
python -m pip install django
```
Para finalizar ver los paquetes instalados con
```=bash
python -m pip freeze
```
y para desactivar el entorno virtual escribir
```=bash
deactivate
```

Al ejecutar `pip freeze` (estamos utilizando un entorno virtual,por eso no se usa python -m) vemos que falta Pyscopg2,entonces hay que hacer lo siguiente.
* Ejecutar
```=bash
easy_install psycopg2-2.6.2.win-amd64-py3.5-pg9.5.3-release.exe
```

## Instalar los requerimientos de el entorno virtual.
Primero instalar el Yahoo quote downloads que no esta en pip, para hacer esto una vez dentro del entorno virtual entrar por cmd a la carpeta de yahoo y ejecutar el archivo `setup.py`
```
setup.py install
```
Luego usar el comando de abajo.
Este comando permitirá instalar todos los paquetes que necesita el proyecto y los instalará pip
```
pip install -r requirements.txt
```

## Configurar la base de datos.
En el proyeto se debe crear una base de datos con los siguientes campos.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'isw',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST':'localhost',
        'PORT': 5432,
    }
}
```
* Nombre = isw (nombre de la base de datos)
* user = usuario que se escribio al instalar postgresql, por default es postgres
* password = contraseña que se utilizo al instalar postgresql
Los demas campos DEBEN quedar como estan.

## Crear el usuario administrador.
Si la configuración anterior fue correcta se podrá hacer las migraciones y crear el administrador del sitio.
Primero correr las migraciones
```
manage.py migrate
```
Luego crear el administrador
```
manage.py createsuperuser
```
Los unicos campos que interesan son el de
* Nombre = admin
* password = django12345
los demas se pueden omitir
