# learnOrbit

Esta es la implementación de nuestra plataforma **learnOrbit**.

## Antes de ejecutar la página

Para poder ver la página web en un navegador, sigue estos pasos para configurar el entorno.

### 1. Verificar la instalación de Python

Es necesario tener **Python** instalado en tu máquina.

- Si no tienes instalado Python, puedes descargarlo desde la [página oficial](https://www.python.org/).
- Una vez instalado, verifica la instalación ejecutando el siguiente comando en la terminal:

  ```bash
  python --version

### 2. Verificar la instalación de pip

Si instalaste Python desde la página oficial, ya tendrás instalado por defecto **pip**. Aun así, verifica que `pip` esté instalado correctamente usando el siguiente comando:

```bash
pip --version
```
Si no tienes **pip** instalado lo necesitas descargar para continuar.

### 3. Entorno virtual

Se recomienda crear un entorno virtual espcialmente si se esta usando un OS como Ubuntu. Para hacer esto se necesita usar los siguientes comados
```bash
python -m venv myenv
```

Y activa el entorno virtual
En Windows
```bash
myenv\Scripts\activate
```
En MacOS/Linux
```bash
source/myenv/bin/activate
```

### 4. Instalar Django

Para instalar Django puedes usar el siguiente comando
```bash
pip install django
```

Para verificar que Django se instalo correctamente se puede usar el comando
```bash
django-admin --version
```

### 5. Correr la página
Finalmente puedes correr la página con al comando
```bash
python manage.py runserver
```

Cuando corres el comando te manda a el enlace **http://127.0.0.1:8000/** esto te mostrara una pagina con informacion para poder ver la pagina ingresa el enlace **http://127.0.0.1:8000/hello**
