## Orion context broker
Orion Context Broker es una implementación del Publish / Subscribe Context Broker GE, que proporciona las interfaces NGSI9 y NGSI10. Usando estas interfaces, los clientes pueden hacer varias operaciones:
•	Registrar aplicaciones de productor de contexto, p. un sensor de temperatura dentro de una habitación
•	Actualizar la información de contexto, p. enviar actualizaciones de temperatura
•	Recibir una notificación cuando se producen cambios en la información de contexto (por ejemplo, la temperatura ha cambiado) o con una frecuencia determinada (por ejemplo, obtener la temperatura por minuto)
•	Consultar información de contexto. Orion Context Broker almacena información de contexto actualizada de las aplicaciones, por lo que las consultas se resuelven en función de esa información.
Orion Context Broker le permite administrar todo el ciclo de vida de la información de contexto, incluidas actualizaciones, consultas, registros y suscripciones. Es una implementación de servidor NGSIv2 para administrar la información de contexto y su disponibilidad. Con Orion Context Broker, puede crear elementos de contexto y administrarlos a través de actualizaciones y consultas. Además, puede suscribirse a la información de contexto para que cuando ocurra alguna condición (por ejemplo, los elementos de contexto hayan cambiado) reciba una notificación.

## Notes on the installation
El enlace para poder descargar el docker file se encuentra en un repositorio de github en la sección de descargas del catálogo FIWARE, también disponible en el docker hub.  En este último nos muestra varias maneras para poder ejecutar orion. 

## Final Evaluation
Para poder realizar pruebas al contenedor fue necesario de un archivo docker-compose ya que orion requiere de mongodb, además fue necesario instalar Postman (Extensión Chrome) para interactuar con el contenedor. 
