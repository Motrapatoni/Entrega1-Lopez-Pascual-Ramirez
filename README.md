# ENTREGA 1 DEL PROYECTO FINAL

## Como ejecutar este proyecto en tu maquina

Para correr este proyecto deberás seguir algunos pasos previos tales como clonar este repositorio, crear un entorno virtual, instalar requerimientos y ejecutar runserver para visualizar el mismo en el localhost.

## Para clonar haremos lo siguiente:

1. Abrir la terminal en tu ordenador.  
Win: Inicio →  Ejecutar → escribir: cmd → Enter  
OS: command + espacio → escribir: terminal → Enter

2. Nos ubicamos en la carpeta donde queremos que quede el proyecto.  
Ej: En el escritorio → carpeta dev
```
cd Desktop
```
```
cd dev
```

3. Ya en la ubicación destino del proyecto, vamos a clonar el repositorio
```
git clone https://github.com/Motrapatoni/Entrega1-Lopez-Pascual-Ramirez
```

## Ahora desde VScode abrimos la carpeta con nombre “Entrega1-Lopez-Pascual-Ramirez”

Una vez abierto nuestro proyecto en el VScode abrimos una terminar y validamos estar en la ubicación correcta ejecutanto por consola ```ls``` y nos debe de retornar los siguiente:
Entrega1                README.md               db.sqlite3              manage.py               requirements.txt
Con esto validamos que estamos en la ubicación correcta.

## Creamos el Entorno virtual.

Ejecutamos en la terminal lo siguiente:
```
python -m venv venv
```
Luego activamos el entorno virtual con:
```
. venv/bin/activate
```

## Instalación de paquetes
En la terminal vamos a ejecutar lo siguiente:
```
pip install -r requirements.txt
```
*Esto va a demorar unos momentos.*

## Luego para poder correr el proyecto en el LocalHost debes de ejecutar en la terminal:
```
python manage.py runserver
```