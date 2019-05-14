# Índice

- [Sobre este módulo](#Sobre-este-módulo)
    - [Aclaración](#Aclaración)
- [Requisitos generales](#Requisitos-generales)
- [Estructura del módulo](#Estructura-del-módulo)
- [Comandos](#Comandos)
    - [CreateNewKB.py](#CreateNewKB.py)
        - Descripción
        - Requisitos
        - Ejecución
            - Argumentos obligatorios
            - Argumentos opcionales
            - Ejemplo de ejecución
        - Output Generado
    - [PublishKB.py](#PublishKB.py)
        - Descripción
        - Requisitos
        - Ejecución
            - Argumentos obligatorios
            - Argumentos opcionales
            - Ejemplo de ejecución
        - Output Generado
    - [GetEndpointKey.py](#GetEndpointKey.py)
        - Descripción
        - Requisitos
        - Ejecución
            - Argumentos obligatorios
            - Argumentos opcionales
            - Ejemplo de ejecución
        - Output Generado
    - [Test.py](#Test.py)
        - Descripción
        - Tips para elaborar un buen set de testo
        - Requisitos
        - Ejecución
            - Argumentos obligatorios
            - Argumentos opcionales
            - Ejemplo de ejecución
        - Output Generado
    - [UpdateKB.py](#UpdateKB.py)
        - Descripción
        - Requisitos
        - Ejecución
            - Argumentos obligatorios
            - Argumentos opcionales
            - Ejemplo de ejecución
        - Output Generado
- [Pendientes](#Pendientes)



# Sobre este módulo

Este módulo contiene los comandos básicos para crear, gestionar y testear una base de conocimiento (KB, por sus siglas en inglés: _knowledge base_). Dichos comandos aparecen listado y descriptos en el apartado [Comandos](#Comandos).

### Aclaración

Este módulo fue construido tomando como base scripts proporcionados por Microsof Azure en su [repositorio de Samples de QnA en GitHub](https://github.com/Azure-Samples/cognitive-services-qnamaker-python)

Asimismo, puede consultarse la [documentación de QnA Maker](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/) ofrecida por Microsoft para mayores especificaciones sobre este Servicio.

# Requisitos generales

Para poder ejecutar este módulo es necesario que el usuario cuente con alguna versión de Python 3.x (si bien el módulo fue testeado con Python 3.6.5, otras versiones 3.x deberían funcionar correctamente).

Además es necesario contar con las librerías listadas en el archivo _requirements.txt_
Para instalarlas, moverse dentro de la carpeta qna_module:

```shell
cd qna_module
```

Y, desde allí, ejecutar el siguiente comando

```shell
pip install -r requirements.txt
```

**Aclaración:** Se recomienda utilizar este módulo en una terminal de Ubuntu o de WSL a fin de asegurar que el encoding no rompa tildes u otros signos propios del español. De ejecutarse en una consola de Windows, verificar tanto en los archivos generados como en la interfaz gráfica de QnA que esto no ocurra.

# Estructura del módulo

- En la carpeta __src__ se encuentran los scripts para correr el módulo.
- En la carpeta __input__ se encuentran las distintas __"carpetas de contenido"__, donde están los archivos que alimentan el módulo.
- Cada carpeta contenido debe llevar el nombre del contenido que posee. Por ejemplo: dentro de input/ se encuentra la carpeta __capital_humano/__. En su interior podemos hallar todo lo referido al contenido de _capital humano_.
- Cada vez que un comando demande un argumento _content_ para su ejecución, se debe indicar el nombre de la __carpeta de contenido__ sobre la cual se desea correr el comando.
- Cada carpeta de contenido **debe** tener:
    
    1) un archivo llamado **config.yml** que posea las credenciales y especificaciones necesarias; [este](./input/capital_humano/config.yml) archivo puede tomarse como modelo y [aquí](./CONFIG.md) se detalla desde dónde se debe extraer cada credencial;
    2) una carpeta (vacía o no) llamada **test**, donde se irán volcando los resultados de algunos comandos.

- Dependiendo de cuál sea la fuente con la cual se quiera crear la base de conocimiento, cada carpeta de contenido **puede** tener alguna de las siguientes opciones o una combinación de más de una
(__aclaración:__ si se desea armar una base de conocimiento con todas las opciones, entonces se deben incluir todos los archivos descriptos a continuación; pero si solo se quiere armar una base con algunos de ellos, entonces se puede prescindir de la existencia de los archivos restantes):

    1) un archivo llamado **files.txt** donde se liste por línea cada uno de los archivos con los que se desea generar una base de conocimiento (actualemente esta opción no se encuentra disponible);
    2) <a id="url">un archivo llamado **urls.txt** donde se liste por línea cada una de las urls con formato FAQ con la que se desee generar una base de conocimiento;</a>
    3) <a id="carpetas">dos carpetas (no es posible tener solo una) llamadas **pregs** y **rttas**:</a>

        - la carpeta **pregs** debe tener el conjunto de **archivos .json** con los cuales se quieren generar las preguntas. Cada archivo .json debe tener un diccionario que tenga una key que sea el nombre del intent y un value que sea una lista de las preguntas que representan ese intent. [Este archivo](./input/capital_humano/pregs/anticipo_cuando.json) puede tomarse como ejemplo. Es importante que la key del diccionario y el archivo .json se llamen del mismo modod (en el ejemplo: el archivo se denomina *anticipo_cuando.json* y la key es *anticipo_cuando*)

        - la carpeta **rttas** debe tener el conjugno de **archivos .txt** con los cuales se quieren generar las respuestas a las preguntas de la carpeta _pregs_. Es imprescindible que cada archivo .json de la carpeta pregs tenga su archivo .txt asociado. Este, además, debe llamarse del mismo modo que el archivo de preguntas (a excepción de la extensión). Por ejemplo, el archivo asociado a las preguntas de *anticipo_cuando.json* debe llamarse *anticipo_cuando.txt*. [Este archivo](./input/capital_humano/rttas/anticipo_cuando.txt) puede tomarse como ejemplo
    
# Comandos

## CreateNewKB.py

### Descripción:

Este comando permite crear una nueva base de conocimiento a partir de archivos .json con preguntas y respuestas, de archivos y de urls que con formato FAQ.
Para más información sobre el tipo de archivos admitidos, consultar la [documentación de fuente de datos permitida de Microsoft Azure](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/concepts/data-sources-supported)

### Requisitos:

Para poder ejecutar este comando es necesario contar con un archivo **config.yml** en la carpeta de contenido que tenga especificados (click [aquí](./input/capital_humano/config.yml) para ver un ejemplo):

- una qna1key
- un service
- un main_host
- un method dentro de la sección _create_

Además, es necesario tener alguna de las opciones mencionadas en el apartado [Estructura del módulo](#Estructura-del-módulo): o bien [las carpetas _pregs_ y _rttas_](#carpetas), o bien [el archivo _urls.txt_](#url), o bien ambas opciones. De no tener ninguna, la base se creará de todos modos pero sin contenido (i.e. no tendrá ninguna pregunta ni respuesta)

### Ejecución

En una terminal, moverse dentro a la carpeta qna_module/src/ y desde allí ejecutar:

```shell
python CreateNewKB.py content [-h] [--name NAME] [--source SOURCE]
```

#### Argumentos obligatorios:

- content: debe ser el nombre exacto de la carpeta de contenido que posee las preguntas y respuestas, archivos y/o urls para generar la base de conocimiento

#### Argumentos opcionales:

- name: nombre de la base de datos que se desea crear (por default: New KB)
- source: fuente desde donde fue extraido el contenido para armar la base de conocimiento (por default: Costum Editorial)
- help: comando de ayuda

#### Ejemplo de ejcución:

```shell 
python CreateNewKB.py capital_humano -n ADP_QnA -s FAQ-ADP
```

### Output generado

Como resultado de ejecutar este comando se debe obtener la generación de:

- una nueva base de conocimiento en la [página de QnA](https://www.qnamaker.ai)
- un archivo *ID_mapper.json* ubicado en la carpeta del contenido con la cual se esté trabajando. Este archivo mapea cada intent con el id que le fue asignado en la base de conocimiento; [este archivo](./input/capital_humano/ID_mapper.json) puede tomarse como ejemplo de lo que debe esperarse
- un archivo _trainning.json_ donde se encuentra el entrenamiento de la base de conocimiento tal y como fue subido (i.e. en el formato esperado por QnA Maker); [este archivo](./input/capital_humano/trainning.json) puede tomarse como ejemplo de lo que debe esperarse

## PublishKB.py

### Descripción:

Este comando permite publicar una base de conocimiento que ya se encuentre creada.

### Requisitos:

Para poder ejecutar este comando es necesario contar con un archivo **config.yml** en la carpeta de contenido que tenga especificados (click [aquí](./input/capital_humano/config.yml) para ver un ejemplo):

- una qna1key
- un service
- un main_host
- un method dentro de la sección _publish_
- un kb dentro de la sección _publish_

### Ejecución

En una terminal, moverse dentro a la carpeta qna_module/src/ y desde allí ejecutar:

```shell
python PublishKB.py content [-h]
```

#### Argumentos obligatorios:

- content: debe ser el nombre exacto de la carpeta de contenido que posee las preguntas y respuestas, archivos y/o urls para publicar la base de conocimiento

#### Argumentos opcionales:

- help: comando de ayuda

#### Ejemplo de ejcución:

```shell
python PublishKB.py capital_humano
```

### Output generado

Como resultado de ejecutar este comando se debe obtener la publicación de la base de conocimiento deseada. Si esto sucede, en la terminal se impimirá {"result":"Success."}

## GetEndpointKey.py

### Descripción:

Este comando permite obtener el endpoint key de una base de conocimiento que ya se encuentre publicada.

**Aclaración:** al publicar una base de conocimiento desde consola, este comando se ejecuta automáticamente y completa el archivo de config.yml

### Requisitos:

Para poder ejecutar este comando es necesario contar con un archivo **config.yml** en la carpeta de contenido que tenga especificada una qna1key (click [aquí](./input/capital_humano/config.yml) para ver un ejemplo):

### Ejecución

En una terminal, moverse dentro a la carpeta qna_module/src/ y desde allí ejecutar:

```shell
python GetEndpointKey.py content [-h]
```

#### Argumentos obligatorios:

- content: debe ser el nombre exacto de la carpeta de contenido que posee las preguntas y respuestas, archivos y/o urls para publicar la base de conocimiento

#### Argumentos opcionales:

- help: comando de ayuda

#### Ejemplo de ejcución:

```shell
python GetEndpointKey.py capital_humano
```

### Output generado

Como resultado de ejecutar este comando se debe completar el parámetro _endpointKey_ de la sección _answer_ en el archivo _config.yml_

## Test.py

### Descripción:

Este comando permite testear una base de conocimiento ya existente a partir de una archivo .csv con preguntas.

### Tips para elaborar un buen test set:

 - Las **oraciones** que se incluyan en el set de testeo deben ser **distintas de aquellas utilizadas para entrenar el QnA**. Si se usan las mismas oraciones es esperable (y deseable) que todas sean correctamente reconocidas (salvo que el set de entrenamiento tenga las mismas oraciones en distintos intents). El verdadero desafío es que el QnA reconozca correctamente preguntas que nunca.
 - Es aconsejable que el set de testeo cuente con ejemplos de todos los intents posibles a fin de poder evaluarlos todos. 
 - En el set de testeo debe incluirse además preguntas que pertenezcan a un intent _none_. Las preguntas de este intent serán aquellas que no pertenezcan a ninguno de los intents con los que fue entrenado el QnA. De hecho, el QnA mismo no será entrenado con este intent _none_. El propósito aquí es evaluar que las preguntas que no pertenecen a ningún intent efectivamente no matchean con ninguno.
 - Si bien la dimensión del set de testeo dependerá de cuán grande sea la base de conocimiento (i.e. de la cantidad de intents que tenga y de la cantidad de preguntas distintas que tenga cada intent) se recomienda incluir al menos entre 5 y 10 preguntas por intent para asegurar que el QnA puede captar cierta variedad en la formulación de las preguntas.

**Aclaración:** el comando solo permite testear bases que hayan sido creadas mediante el comando CreateNewKB.py y que hayan recibido como input un conjunto de preguntas y respuestas en formato .json como se describe en el [punto 3 en la **Estructura del módulo**](#carpetas)

### Requisitos:

Antes de ejecutar este comando, se debe publicar la base de conocimiento. No es posible obtener respuestas de la base si esta solamente fue creada pero no publicada.

Para poder ejecutar este comando es necesario contar con un archivo **config.yml** en la carpeta de contenido que tenga especificados (click [aquí](./input/capital_humano/config.yml) para ver un ejemplo):

- un host dentro de la sección _answer_
- un endpoint_key dentro de la sección _answer_
- un kb dentro de la sección _publish_
 
Además es necesario tener un archivo ID_mapper.json dentro de la carpeta de contenido. Este archivo se genera automáticamente al correr el comando CreateNewKB.py. [Aquí](./input/capital_humano/ID_mapper.json) puede verse un modelo de este archivo.

También es necesario tener un archivo llamado _pregs.csv_ que se ubique dentro de la carpeta _test_ y que contenga dos columnas: una llamada _Preguntas_ y otra llamada *tag_esperado*. La columnda _Preguntas_ debe tener las preguntas con las que se quiera testear la base de datos. Y la columna *tag_esperado* debe tener el nombre del intent al que pertenece la pregunta. Este nombre debe estar escrito del mismo modod que se presenta en el archivo *ID_mapper.json*, que en última instancia es el nombre que tiene el archivo .json que contiene las preguntas de este intent. Por ejemplo: el archivo *anticipo_cuando.json* tiene preguntas que refieren a cuándo se puede pedir un anticipo. Si en la lista de preguntas para testear se incluye una pregunta del tipo "¿Cuándo puedo pedir un anticippo?", esa pregunta debe tener en la columna tag_esperado el valor *anticipo_cuando*. [Este archivo](./input/capital_humano/test/pregs.csv) puede tomarse como ejemplo.

**Aclaración:** No es obligatorio completar la columna *tag_esperado*. Esta columna debe existir pero sus valores no son obligatorios. De no hallarse completa, el programa simplemente testeará la pregunta y generará un archivo de salida con lo que la base haya respondido y completará el .csv con estos datos. Si la columna se encuentra completa en su totalidad, el programa además generará una matriz de confusión que muestre la performance de la base.

### Ejecución

En una terminal, moverse dentro a la carpeta qna_module/src/ y desde allí ejecutar:

```shell
python Test.py content [--top TOP] [-h]
```

#### Argumentos obligatorios:

- content: debe ser el nombre exacto de la carpeta de contenido que posee las preguntas y respuestas, archivos y/o urls para generar la base de conocimiento

#### Argumentos opcionales:

- top: cantidad de respuestas posibles a considerar al momento de testear una pregunta (QnA puede devolver más de una respuesta, en caso de seleccionar un número mayor a 1, las ordena por score de mayor a menor). Por dafault este valor es 1. Se sugiere no cambiar este valor a menos que se hagan las modificaciones pertinentes para que los valores se carguen adecuadamente en el archivo pregs.csv (función no testead)
- help: comando de ayuda

#### Ejemplo de ejcución:

```shell
python Test.py capital_humano
```

### Output generado

Como resultado de ejecutar este comando se debe obtener:

- la aparición de tres nuevas columnas en el archivo _prags.json_ presente en la carpeta _test_: una columna con el tag_obtenido (proveniente de la consulta a la base de conocimiento), otra con el score de ese tag y una última con la respuesta que devuelve ante ese tag
- un archivo *output.json* ubicado en la carpeta _test_ de la carpeta contenido con la cual se esté trabajando. Este archivo muestra el output generado a partir de las consultas a la base de conocimiento tal y como las devuelve QnA Maker; [este archivo](./input/capital_humano/test/output.json) puede tomarse como ejemplo de lo que debe esperarse
- un archivo *confusion_matrix.jpg* donde se puede visualizar la matriz de confusión generada a partir de la comparación entre los tags obtenidos y los tags esperados, en el caso de que las preguntas hayan estado etiquetadas; [este archivo](./input/capital_humano/test/confusion_matrix.jpg) puede tomarse como ejemplo de lo que debe esperarse

## UpdateKB.py

### Descripción:

Este comando permite actualizar una base de conocimiento ya existente a partir de una archivo .csv con preguntas.

**Aclaración:** el comando solo permite testear bases que hayan sido creadas mediante el comando CreateNewKB.py y que hayan recibido como input un conjunto de preguntas y respuestas en formato .json como se describe en el [punto 3 en la **Estructura del módulo**](#carpetas)

### Requisitos:

Para poder ejecutar este comando es necesario contar con un archivo **config.yml** en la carpeta de contenido que tenga especificados (click [aquí](./input/capital_humano/config.yml) para ver un ejemplo):

- una qna1key
- un kb dentro de la sección _publish_
- un main_host
- un service
- un method dentro de la sección _publish_
 
Además es necesario tener un archivo ID_mapper.json dentro de la carpeta de contenido. Este archivo se genera automáticamente al correr el comando CreateNewKB.py. [Aquí](./input/capital_humano/ID_mapper.json) puede verse un modelo de este archivo.

También es necesario tener una carpeta llamada _modificaciones_ dentro de la carpeta de contenido. [Esta carpeta](./input/capital_humano/modificaciones/) puede tomarse como modelo. El contenido de dicha carpeta podrá contener:
    - una carpeta llamada _agregar_ donde estarán las carpetas _pregs_, _rttas_ y el archivo _urls.txt_. Estas carpetas y archivos son análogos a los ya descriptos en la secciones anteriores (ver [urls.txt](#url) y [descripción de carpetas](#carpetas) para más información). La información contenida en estas carpetas y arhcivo deben ser las preguntas a agregar a la base de datos
    - un archivo llamado _borrar.json_ donde se detallarán los ids de las preguntas a borrar. [Este archivo](./input/capital_humano/modificaciones/borrar.json) puede tomarse como modelo

### Ejecución

En una terminal, moverse dentro a la carpeta qna_module/src/ y desde allí ejecutar:

```shell
python UpdateKB.py content content [-h] [--name NAME] [--source SOURCE]
```

#### Argumentos obligatorios:

- content: debe ser el nombre exacto de la carpeta de contenido que posee las preguntas y respuestas, archivos y/o urls para actualizar la base de conocimiento

#### Argumentos opcionales:

- name: nuevo nombre para la base de datos en caso de que se desee cambiarlo. Si no se indica nada, la base mantendrá el nombre que ya poseía.
- source: fuente desde donde fue extraido el contenido para actualizar la base de conocimiento (por default: Costum Editorial)
- help: comando de ayuda

#### Ejemplo de ejcución:

```shell
python UpdateKB.py capital_humano -n NuevoNombre
```

### Output generado

Como resultado de ejecutar este comando se debe obtener:

- la actualización de la base de datos deaseada en la [página de QnA Maker](https://www.qnamaker.ai)
- la actualización del archivo [ID_mapper.json](./input/capital_humano/ID_mapper.json) en la carpeta de contenido (se deben ver los nuevos IDs agregados o la eliminación de aquellos cuyas preguntas se hayan quitado)



# Pendientes

Queda pendiente para este módulo:

- agregar comandos que permitan: 
    1. descargar la base de datos
    2. borrar la base de datos
    3. agregar alternations para las palabras
    4. reemplazar la base de datos
    4. obtener los detalles de la base de datos para que el usuario tenga que completar a mano lo menso posible en el archivo config.yml
    5. agregar métricas de accuracy, precision y recall al comando de Test
    6. agregar números a la matriz de forma que refleje cuántos casos fueron exitosos y cuántos no
    7. armar el módulo con py env