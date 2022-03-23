# newcombin-backend

Ejercicio práctico para el challenge backend de la empresa NEWCOMBIN

## Requerimientos:

- Python 3.6 o superior
- Django 4.0.3 o superior
- Djangorestframework 3.13.1 o superior

Para facilidad de ejecución el ejemplo, se usará SQLite como base de datos

## Instalación


- Instalar un entorno virtual con virtualenv (recomendado)
- Clonar el repositorio dentro del entorno virtual
- Instalar las dependencias con el comando pip usando el archivo requirements.txt provisto

    cd newcombin-backend

    pip install -r requirements.txt

- Ingresar a la carpeta del código del repositorio

    cd api-pagos

- Crear la estructura de la base de datos

    python manage.py migrate

- Iniciar el servidor web de Django en el puerto 8000

    python manage.py runserver 0.0.0.0:8000


# API

El api cuenta con 2 endpoints para ingreso de información, usando un POST request:

## Creación de nuevo importe

/create-tax/

Se debe proveer dentro del body del request, la siguiente información en formato JSON:

- tipo_servicio: String con identificador del tipo de servicio (luz, agua, telefono, etc)
- descripcion_servicio: String con detalle del servicio
- fecha_vencimiento: String con fecha de vencimiento en formato YYYY-MM-DD
- importe_servicio: Numero en formato float, con valor a pagar
- status_pago: estado de pago, que puede ser pending, paid, partial_paid

Si por ejemplo usamos CURL para enviar los datos:

    curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/create-tax/ -d '{"tipo_servicio":"telefono","descripcion_servicio":"Telefono  enero","fecha_vencimiento":"2022-04-15","importe_servicio":11.00,"status_pago":"pending"}'

Obtendremos la siguiente respuesta con el con estado 200, y la información del estado, y los datos almacenados. El valor del campo codigo_barra es el PK del objeto, y se requiere para el registro del pago

    {"status":"ok","data":{"codigo_barra":13,"tipo_servicio":"telefono","descripcion_servicio":"Telefono  enero","fecha_vencimiento":"2022-04-15","importe_servicio":11.0,"status_pago":"pending"}}

En caso de error se devolverá con estado 500 un JSON con la descripción del error

## Creeación de pago de importe

/pay-tax/

Para registrar un pago, se debe incluir en el body del request la siguiente información en formato JSON:

- codigo_barra: Entero con número asignado al importe creado previamente
- metodo_pago: String metodo de pago (cash, debit-card, credit-card)
- numero_tarjeta: String de número de tarjeta para pagos que no sean cash
- importe_pago: Numero en formato float, con valor de pago

Si por ejemplo usamos CURL para enviar los datos:

    curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/pay-tax/ -d '{"codigo_barra":13,"metodo_pago":"cash","importe_pago":11.00}'

Si el código de barra es correcto y existe en el objeto Payables, devolverá con estado 200 la siguiente respuesta:

    {"status":"ok","data":{"id":12,"codigo_barra":"Payables object (13)","metodo_pago":"cash","numero_tarjeta":"","importe_pago":11.0,"fecha_pago":"2022-03-23"}}

En caso de error se devolverá con estado 500 un JSON con la descripción del error

Si el valor de pago es igual o superior al importe generado, el estado_pago del objeto Payable cambiará a "paid". Si el pago registrado es menor al tota, se registrará como "partial_paid"

## Consulta de pagos pendientes

/pending-tax/<Str:servicio>

Genera un listado en formato JSON de los servicios que se encuentran con el campo estado_pago en "pending". Si se omite el identificador del servicio, mostrará todo el listado completo.

    curl -X GET http://127.0.0.1:8000/pending-tax/telefono

    [{"codigo_barra":1,"tipo_servicio":"telefono","descripcion_servicio":"Telefono  enero","fecha_vencimiento":"2022-04-15","importe_servicio":11.0,"status_pago":"pending"},{"codigo_barra":2,"tipo_servicio":"telefono","descripcion_servicio":"Telefono febrero","fecha_vencimiento":"2022-05-15","importe_servicio":11.0,"status_pago":"pending"},{"codigo_barra":3,"tipo_servicio":"telefono","descripcion_servicio":"Telefono marzo","fecha_vencimiento":"2022-06-15","importe_servicio":11.0,"status_pago":"pending"}]

/payments/<Str:fecha_inicio>/<Str:fecha_fin>/

Genera un reporte consolidado por fecha, detallando el total de pagos de ese día, y el número de transacciones. Si no se incluye las fechas, muestra el total de pagos registrados por día.

    curl -X GET http://127.0.0.1:8000/payments/2022-01-20/2022-03-25

    [{"fecha_pago":"2022-03-01","cantidad_transacciones":3,"importe_acumulado":33.0},{"fecha_pago":"2022-03-23","cantidad_transacciones":1,"importe_acumulado":11.0}]

## Consideraciones finales

- El ejemplo demuestra únicamente el proceso de implementación de un API sencilla usando Django, principalmente demostrando el uso del router, modelos, vistas y serializadores
- Los tipos de servicio no se encuentran parametrizados, ya que la definición del ejercicio no los define. Podría implementarse un objeto nuevo con el detalle de todos los tipos de pago existentes
- El identificador codigo_barra, por facilidad, se definió como un entero dentro del modelo.
- Por restricciones de tiempo y al ser un ejercicio práctico, no se genera la documentación del API usando herramientas como swagger, que facilitan el entendimiento de los endpoints respectivos.
- Para pruebas y validación de informaciṕn, se generaron los endpoints /payments/ y /pending-tax/ sin parámetros, a pesar de no estar especificados en el requerimiento. Esto no se realizará en un proyecto con un cliente externo, salvo requerimiento del mismo.









