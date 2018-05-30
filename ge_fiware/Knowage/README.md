## KNOWAGE
Knowage es la suite profesional de código abierto para el análisis empresarial moderno sobre fuentes tradicionales y sistemas de big data. Knowage es la nueva generación de soluciones analíticas de código abierto, como una evolución natural del conocido SpagoBI. Basado en estándares abiertos y con una oferta modular, Knowage se dirige a dominios específicos para subproductos particulares, que se pueden combinar para obtener un tamaño personalizado en una única solución. 
Los subproductos de la suite son:
  -	BD (big data), para analizar datos almacenados en clusters de big data o bases de datos NoSQL
  -	SI (inteligencia inteligente), la inteligencia empresarial habitual en datos estructurados, pero más orientada a capacidades de autoservicio y creación de prototipos ágiles
  -	ER (informes empresariales), para producir y distribuir informes estáticos
  -	LI (inteligencia de ubicación), para relacionar datos comerciales con información espacial o geográfica
  -	PM (gestión del rendimiento), para gestionar KPI y organizar tablas de puntuación
  -	PA (análisis predictivo), para análisis más avanzados
  -	EI (inteligencia incorporada), para vincular Knowage con soluciones externas proporcionadas por el cliente o por terceros.
Los paquetes lanzados contienen todos los subproductos combinados juntos en una solución única y completa de análisis de datos. 
Knowage responde a una visión más moderna del análisis de datos, proporcionando capacidades avanzadas de autoservicio que otorgan autonomía al usuario final, ahora capaz de construir su propio análisis y explorar su propio espacio de datos, combinando también datos provenientes de diferentes fuentes. 

## Notes on the installation
Para poder levantar todos los contenedores relacionados con Knowage es necesario clonar el repositorio proporcionado en GitHub, se requiere ingresar en el repositorio a la siguiente dirección Knowage-Server-Docker\6.1.1, una vez ubicado dentro del repositorio se ejecutara el comando sudo docker-compose up –d gracias al archivo docker-compose.yml se levantaran los servicios de knowage y mysql.

Note
-	Al ejecutar el docker compose se levantan 2 contenedores knowage y mysql.
-	Para comprobar su correcto funcionamiento es necesario ingresar a  http://localhost:8080/knowage.
-	Se ejecutó el docker-compose ubicado en el directorio Knowage-Server-Docker\6.1.1\docker-compose.yml. 
-	Se realizaron las pruebas de extremo a extremo propuestas en la guía del administrador para comprobar su correcto funcionamiento.
-	Los usuarios disponibles por default son:
“biadmin/biadmin, bidev/bidev and biuser/biuser”
-	Se proporciona documentación en http://knowage.readthedocs.io/en/latest/index.html.

## Final Evaluation
El despliegue de este habilitador es muy fácil y sencilla, no hay mayor problema para desplegar los servicios bastara con ejecutar el archivo docker-compose proporcionado en GitHub.
Las pruebas de cordura propuestas en la documentación concuerdan con el funcionamiento del servicio Knowage en docker.
El contenedor funciona a la perfección y no se requiere la configuración de ningún archivo externo.
