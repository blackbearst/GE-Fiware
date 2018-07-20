## PEP Proxy (Wilma)
Obtiene la implementación de referencia de PEP Proxy Generic Enabler. Gracias a este componente y junto con la gestión de identidad y la autorización PDP GEs, agregará autenticación y seguridad de autorización a sus aplicaciones back-end. Por lo tanto, solo los usuarios de FIWARE podrán acceder a sus servicios de GEs o REST. Pero también podrá administrar permisos y políticas específicos para sus recursos, lo que le permitirá diferentes niveles de acceso a sus usuarios.

PEP Proxy proporciona una capa de seguridad para agregar filtros de autenticación y autorización a FIWARE GEs y cualquier servicio de back-end. Es el PEP (Police Enforcement Point) del Capítulo de Seguridad de FIWARE. Entonces, junto con Identity Management and Authorization PDP GEs brinda seguridad a FIWARE backends.
El caso de uso básico es un escenario en el que tiene usuarios de una aplicación de front-end que accederá a recursos en una aplicación de back-end. Y desea permitir que solo los usuarios de FIWARE accedan a esos recursos. Los pasos para configurar este entorno son los siguientes:
-	Implemente un Proxy PEP en la parte superior de su servicio de fondo. Ahora el punto final de este servicio es el punto final del Proxy PEP y usted tiene que cambiar el back-end a otro punto final (puede estar en el mismo servidor pero en otro puerto). El Proxy PEP redirigirá las solicitudes al servicio.
-	Registre su aplicación en el IdM.
-	Con una biblioteca OAuth2 y las credenciales obtenidas en el IdM para la aplicación, implemente un mecanismo OAuth2 en su aplicación. Por lo tanto, sus usuarios podrán iniciar sesión en su aplicación utilizando sus registros de FIWARE.
-	Cuando un usuario inicia sesión en su aplicación, IdM generará un token OAuth2 que lo represente. Debe guardar este token OAuth2 para incluirlo en las solicitudes de su servicio de fondo (como un encabezado HTTP).
-	Debe enviar todas las solicitudes a su servicio de fondo al punto final en el que se implementó el Proxy PEP.
-	Si el token incluido en la solicitud es válido, PEP Proxy redireccionará la solicitud al back-end. Si no, responderá con un código no autorizado.

## Notes on the installation
En la documentación oficial no se especifica como descargar la imagen y desplegar el contenedor por lo cual fue  necesario acudir al repositorio de GitHub, dentro de la documentación del repositorio indica que para desplegar en docker es necesario buscar la imagen en el Docker-Hub.
La documentación ofrecida en el Docker-Hub es suficiente para la creación del contenedor, su despliegue y su pausa pero no proporciona la información suficiente para su configuración, para configurar correctamente Wilma es necesario ir al Installation and Administration Guide o a la sección de tutoriales en FIWARE Academy.

  Note
  -	Es necesario descargar el repositorio de GitHub
  -	Al momento de desplegar el contenedor es necesario generar un volumen haciendo referencia al archivo config.js incluido en la ubicación: fiware-pep-proxy\config.js.
  -	El archivo config.js tiene que ser editado, proporcionando el Username y password obtenidos en FIWARE lab.
  -	Para generar el Token para las pruebas de cordura es necesario descargar y ejecutar el complemento oauth2-example-client.
  -	Para generar el Token y poder realizar las pruebas de una manera correcta es necesario descargar de GitHub el siguiente repositorio  oauth2-example-client, en el cual es necesario editar el archivo config.js.template con el Username y password obtenidos previamente de FIWERE lab. El servicio se levanta con sudo node server.js y es necesario acceder a http://localhost:80 para generar y obtener el Token.

## Final Evaluation
El habilitador genérico PEP-Proxy (Wilma) funciono correctamente, su despliegue es sencillo aunque se requiere ingresar al FIWARE lab para obtener el Userneme y el password.
Se realizaron las pruebas propuestas  en sanity-check-procedures para comprobar su correcto funcionamiento, obteniendo un correcto desempeño de la herramienta.
La documentación proporcionada está incompleta, es necesario recurrir a diversas páginas para complementarla.
