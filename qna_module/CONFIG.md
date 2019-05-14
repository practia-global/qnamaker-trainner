# Cómo obtener cada credencial o especificación para _config.yml_

## qna1key

Es la clave nro 1. del servicio de QnA Maker. Esta clave puede encontrarse en el portal de Azure. Dentro del Servicio de QnA Maker contratado, debe buscarse en la parte de Claves e ingresar la Clave 1.

## service

Por default: /qnamaker/v4.0

## create

#### host

Por default: westus.api.cognitive.microsoft.com
    
#### method

Por default: /knowledgebases/create

## publish

#### method

Por default: '/knowledgebases/'

#### kb

Este id debería autocompletarse cuando se genera la base de conocimiento mediante el comando CreateNewKB.py

Si esto no ocurre: se puede encontrar el kb (id de la base de conocimiento) siguiendo las instrucciones para buscar el endpoint key. Este id de la base es el número que aparece en el POST entre "/knowledgebases/" y "/generateAnswer". Por ejemplo, en el siguiente caso 

POST /knowledgebases/4a104c81-3619-4b67-86d1-efea5bc6735d/generateAnswer

el id de la base de conocimiento es 4a104c81-3619-4b67-86d1-efea5bc6735d

## answer

#### host

Es el nombre del App Service de Azure + .azurewebsites.net

Por ejemplo: si la App Service se llama PractiaADP-Bot-qnahost, el host será PractiaADP-Bot-qnahost.azurewebsites.net

#### endpointKey

Este endpoint key debería autocompletarse cuando se publica la base de conocimiento mediante el comando PublishKB.py

Si esto no sucede porque la base no fue creada utilizando este comando, existen dos vías para obtenerlo:
1. Mediante el comando [GetEndpointKey.py](./README.md) explicado en el README del módulo qna_module
2. Buscandolo en la páginade [QnA Maker](https://www.qnamaker.ai). Allí, al crear y publicar una base de conocimiento se crea un endpoint key al cual puede accederse haciendo click sobre la base de conocimiento deseada. Desde allí, se verá un botón **Settings** en la esquina superior derecha. Una vez en esta sección, al final de la página se verán las especificaciones para el despliegue (bajo el nombre "Deployment details"). Si se elige la opción "Postman", se visualiza claramente el endpoint key.