## Application mashup (Wirecloud)
Wirecloud se basa en el desarrollo de usuario final (software), RIA y tecnologías semánticas para ofrecer una plataforma de mashup de aplicaciones web centrada en usuarios finales de próxima generación destinada a permitir a los usuarios finales sin habilidades de programación crear fácilmente aplicaciones web y tableros / cabinas (por ejemplo, visualizar sus datos de interés o controlar su hogar o entorno domesticado).
Están destinados a aprovechar la "larga cola" de la Web of Services (también conocida como la web programable) al explotar el desarrollo rápido, el bricolaje y la capacidad de compartir. Por lo general atienden una necesidad específica de la situación (es decir, inmediata, de corta duración, personalizada), frecuentemente con alto potencial de reutilización.

## Notes on the installation
Fue muy sencillo desplegar los servicios gracias al docker compose proporcionado en el repositorio de GitHub, vasto con levantar el servicio con el comando docker-compose up –d. 

Note
-	Al ejecutar el docker compose se levantan 3 contenedores nginx, wirecloud y pstgres.
-	Para comprobar su correcto funcionamiento es necesario ingresar a  http://localhost:80. 
-	Se ejecutó el docker-compose ubicado en el directorio docker-wirecloud\hub-docs\docker-compose.yml. 
-	Se realizaron las pruebas de extremo a extremo propuestas en la guía del administrador para comprobar su correcto funcionamiento.
-	Para ingresar a wirecloud es necesario crear una cuenta de usuario ejecutando el siguiente comando:
docker-compose exec wirecloud manage.py createsuperuser
-	Se proporciona una muy buena documentación en https://wirecloud.readthedocs.io/en/latest/.
 
## Final Evaluation
Gracias al docker compose proporcionado en GitHub fue bastante sencillo el despliegue de este habilitador genérico, no se requiere de mayor configuración en algún documento del repositorio, bastará con ejecutar le docker compose y este se encargará de descargar todas las dependencias requeridas.

