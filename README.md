# Asistente de Productividad Contextual (APC)

## Descripción
El Asistente de Productividad Contextual (APC) es una herramienta diseñada para ayudar a los usuarios a mantener el enfoque y la productividad basándose en su ubicación, hora del día y actividades programadas.

## Características principales
- Gestión de ubicaciones importantes
- Configuración de horarios productivos
- Programación de actividades
- Alertas basadas en contexto (ubicación y tiempo)

## Cómo funciona
El APC utiliza la geolocalización y el tiempo actual para proporcionar recordatorios y sugerencias personalizadas. El script verifica periódicamente:

1. Si el usuario está en un horario productivo
2. Si el usuario está cerca de una ubicación importante
3. Si hay actividades programadas para el momento actual

## Requisitos
- Python 3.6+
- geopy

## Instalación
1. Clona este repositorio:
   git clone https://github.com/Abe1256/Digitalizacion2/tree/main
2. Instala las dependencias:
pip install -r requirements.txt

## Uso
1. Ejecuta el script principal:
python asistente_productividad.py
2. Sigue las instrucciones en pantalla para configurar tu ubicación actual.
3. El asistente comenzará a proporcionar alertas y recordatorios basados en tu contexto.

## Configuración
El archivo `config.json` se crea automáticamente y almacena:
- Ubicaciones importantes
- Horarios productivos
- Actividades programadas

Puedes editar este archivo manualmente o usar las funciones del script para actualizarlo.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de enviar un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
