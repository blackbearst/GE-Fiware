GE-Fiware
=========
Este manual tiene como finalidad ayudar a los usuarios interesado en utilizar los scripts ofrecidos en https://github.com/blackbearst/GE-Fiware los cuales han sido diseñados para la automatización y despliegue de los siguientes GE de FIWARE:
-	Kurento
-	Orion
-	Wirecloud
-	Wilma pep proxy
-	Knowage
-	KeyRock
-	AuthzForce
-	AEON
## Requerimientos de software para la utilización de Aut-GE-FIWARE:
-	Sistema operativo: cualquier distribución de Linux de 64 bits, se recomienda (Ubuntu 16 o versiones posteriores).
-	Docker (necesario agregar su usuario al grupo de acopladores para evitar el uso de sudo junto con los comandos docker).
-	Python.
## Implementación:
En la siguiente figura se  muestra la estructura de los archivos incluidos en cada directorio del repositorio de Github.
<p align="center">
   <img src="extras/img/1_estructura_proyecto.png">
</p>
Para ejecutar Aut-GE-FIWARE es necesario abrir una nueva terminal de comandos. 
Los scripts están adaptados para evitar el uso de sudo por lo cual es necesario agregar su usuario al grupo de acopladores con el siguiente comando:
 <pre>
 $ sudo usermode –aG docker $USER //Remplazar USER por su usario.
 </pre>

En la terminal se ubicara en la ruta en la cual desee guardar el directorio a clonar, introducirá el siguiente comando para clonar el directorio alojado en el repositorio de Github  a su máquina host:
 <pre>
 $ git clone https://github.com/blackbearst/GE-Fiware.git
 </pre>

+ Si ya había clonado el repositorio previamente y desea actualizarlo deberá posicionarse dentro del directorio “GE-Fiware” e ingresar el siguiente comando:
       <pre>
       $ git pull
       </pre>
<p align="center">
    <img src="extras/img/2_gitpull.png">
</p>

Una vez clonado el directorio “GE-Fiware” para poder hacer uso de Aut-GE-FIWARE, ubicarse dentro del directorio e introducir el siguiente comando:
 <pre>
 python index.py
 </pre>
Con este comando se iniciara el script index.py el cual incluye las instrucciones para ejecutar cada uno de los scripts que automatiza el despliegue de cada uno de los diferentes GE incluidos en mencionado script.
<p align="center">
    <img src="extras/img/3_gitclone.png">
</p>

## Edición:
Para comodidad del usuario se puede elegir que GE desee desplegar, bastara con abrir el archivo “index.py” y ubicarse en la siguiente sección:

 <pre>
 os.system('cd ge_fiware/Kurento && python Kurento.py') #run KMS
 os.system('cd ge_fiware/Orion && python Orion.py') #run Orion
 os.system('cd ge_fiware/Wirecloud && python Wirecloud.py') #run Wirecloud
 os.system('cd ge_fiware/Wilma && python Wilma.py') #run Wilma
 os.system('cd ge_fiware/AuthzForce && python authzforce.py') #run AuthzForce
 os.system('cd ge_fiware/KeyRock && python keyrock.py') #run KeyRock
 os.system('cd ge_fiware/Knowage && python knowage.py') #run Knowage
 </pre>
En esta sección como se observa están indicados cada uno de los scripts por separado de cada GE, bastara con comentar la línea de código del GE que no queremos que sea ejecutado poniendo un “#” delante de la línea de código.

## Solución de problemas:
Si una vez iniciado el script “index.py” observa que al desplegar cualquier GE se queda el prompt parpadeando por mucho tiempo sin realizar ninguna acción.
<p align="center">
    <img src="extras/img/4_promptInactivo.png">
</p>
Acceda a su navegador predeterminado e introduzca en la barra de direcciones la siguiente dirección: 
 <pre>
 http://localhost:4444
 </pre>
Esto lo redireccionará a la página de servicios del contenedor de Selenium el cual es utilizado por los GE para su automatización.
<p align="center">
  <img src="extras/img/5_seleniumGrid.png">
</p>

Ingrese a la opción de "console" y compruebe que el icono de chrome se encuentre activo <img src="extras/img/chromeUp.png">, si se encuentra sombreado significa que el nodo se ha cerrado <img src="extras/img/chromeDown.png">.
<p align="center">
   <img src="extras/img/6_NodoUpDown.png">
</p>

Para solucionar este problema:
1.	Detenga la ejecución del script en la terminal introduciendo el juego de teclas “control + c”.
2.	En la consola introduzca el siguiente comando:
   <pre>
   $ docker-compose down
   </pre>
Este comando removerá los contenedores incluidos en el docker-compose.
3.	Vuelva a iniciar el script con el comando:
   <pre>
   $ python index.py
   </pre>
<p align="center">
   <img src="extras/img/7_restartNChrome.png">
</p>

## Que incluye el docker-compose?
El docker-compose.yml está diseñado para levantar tres servicios diferentes por un lado  levanta un contenedor Selenium el cual a su vez se conecta con otro contenedor el cual es un nodo de Chrome, si este nodo de chrome se cierra durante la ejecución del script ocasionara que  el prompt se quede pasmado evitando continuar con la ejecución.
Por último se levanta un tercer servicio el cual es un contenedor con MongDB para guardar los reportes generados por cada una de las pruebas para asegurar la persistencia de los datos.
<p align="center">
   <img src="extras/img/8_dockerCompose.png">
</p>

## Puertos de contenedores:
docker-compose.yml
-	Selenium puerto: 4444
-	Mongo puerto: 27017
-	Chrome puerto: null

Kurento 
-	Kms puerto: 8888

Orion 
-	Orion pueto: null
-	Mongo puerto: 1026

Wirecloud
-	Ngnix puerto: 80
-	Postgres puerto: 5432
-	Elasticsearch puerto: null
-	Wirecloud puerto: null

Wilma pep proxy
-	Pep-proxy puerto:80

Knowage
-	Knowage puerto: 8080
-	My SQL puerto: null

KeyRock
-	My SQL puerto: 3306
-	Fiware idm puertos: 3000, 443

AuthzForce
-	AuthzForce puerto: 8080

AEON
-	Mongo puerto: 27017
-	Rabbittmq puertos: 5672, 15672
-	Events puerto: 7789
-	Dashboard puerto: 8080
-	Rest puerto: 3000

## Observaciones:
-	Los tiempos de ejecución varían dependiendo el GE y el equipo host sobre el cual se ejecuta el script.
-	Si la conexión a internet es lenta tardara en descargar las imágenes correspondientes de los GE en docker.
-	 La primera corrida tardara más debido a la clonación y descarga de los diferentes repositorios de Github correspondiente a cada GE. 
## Recomendaciones:
-	Contar con una conexión a internet rápida y estable.
-	Contar con las últimas versiones de docker y python.
-	Verificar que los puertos utilizados por los GE no interfieran con algún contendor ya desplegado en su máquina host.

