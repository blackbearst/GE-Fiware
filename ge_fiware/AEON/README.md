## Fiware cloud messaging (AEON)
El Cloud Messaging GE (AEON) proporciona servicios en la nube (canales) para comunicar un número ilimitado de entidades, intercambiando una cantidad ilimitada de información. Pero no solo se trata de la comunicación, sino que también brinda servicios para la administración fácil de las entidades que participan en sus entornos: móvil, camión, caja, termómetro, incluso usted mismo).
El Cloud Messaging GE admite dos bloques de operaciones principales:
-	Gestión de recursos: gestión de las diferentes entidades y canales.
+	Crear, Eliminar, Actualizar y Eliminar Entidades
+	Crear, eliminar, actualizar y eliminar canales asociados a una entidad
-	Publicar / Suscribir: basado en la gestión de las operaciones de publicación y suscripción.
+	Publicar información en un canal
+ Suscribirse a un canal Detenga, continúe y detenga la suscripción para tener un mejor control de sus operaciones.

La mensajería en la nube GE ofrece, no solo y la API para administrar todos los recursos, sino también proporciona diferentes SDK para comenzar a usarlosimplemente incluyéndolo en su código.

## Notes on the installation
El despliegue de la imagen docker presento algunos errores al levantar el servicio de aeon/backend  debido a que se requiere tener instalados algunos componentes extra para que pueda ejecutarse esta imagen.
Se requiere tener previamente desplegado mongo, rabbit, events y dashboard, por lo cual es necesario desplegar todo con la ayuda de un archivo docker compse y un archivo deploy_aeon.sh para descargar events, dashboard y rabbit de sus respectivos repositorios en github.  
Otro problema es la poca documentación disponible, la única documentación disponible esta en git y en el FIWARE Catalogue.
En el manual de instalación se proponen algunas pruebas de cordura para verificar el correcto funcionamiento del Generic Enabler, esta información también es escasa y la explicación no es lo suficientemente clara.

## Final Evaluation
El despliegue de AEON es sencillo con el docker compose proporcionado en el repositorio de github, aunque la información es escasa los datos proporcionados son suficientes para poder crear y ejecutar el contenedor. 

