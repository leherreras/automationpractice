# automationpractice
Esta es una prueba practica de QA automation 

Despues de clonado el repositorio de git por favor instale los paquetes necesarios usando el siguiente comando
`pip install -r requirements.txt`

Para correr los test unitatios usu el siguiente comando
`python -m unittest discover -s /home/leherreras/PycharmProjects/automationpractice/`

En estas pruebas se realizaron las validaciones de QA con el patron de diseño Page Object Model
Se crearon pruebas a las siguientes vistas
Autenticacion
Contact us
Index

Se encontraron los siguientes errores:

Al momento de realizar los filtros de las prendas la pagina se queda cargando aun asi no se bloquea.

Aunque el aplicativo dice que se envio el correo electronico correctamente no se esta enviando copia del resivido a la persona quien lo envio.

En las imagenes principales del index esta redireccionando a paginas externas las cuales no hacen referencia a la pagina
 