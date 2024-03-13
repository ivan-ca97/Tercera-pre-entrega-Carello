# Iván Carello - Preentrega 3 - Comisión  50215

El proyecto funciona como precursor del proyecto final, con la idea de generar una página web de administración de finanzas personales o familiares.

## Descripción

El proyecto contiene 4 modelos, con sus respectivos campos:

* Persona
    * nombre
    * apellido
    * dni
    * email

* FormaDePago
    * nombre
    * credito (indica si se trata de una forma de pago con tarjeta de crédito)
    * descripcion

* Ingreso
    * nombreIngreso
    * descripcion
    * monto
    * titularNombre
    * fecha

* Egreso
    * nombreIngrenombreso
    * descripcion
    * monto
    * titularNombre
    * fecha
    * formaDePago

Cada modelo tiene una URL dedicada a las que se puede acceder desde la barra de navegación que está a la izquierda.

Las 4 pantallas tienen en común:
* Una tabla que muestra todos los objetos creados del objeto, con todos los campos
* Un botón con un "+" color verde que permite crear objetos nuevos
* Sobre la derecha de cada entrada en la tabla, un botón gris con el dibujo de una persona y un lapiz, para editar los objetos
* A la derecha del botón de editar, un botón rojo con un tacho de basura para eliminar el objeto de la base de datos

Además, Ingreso y Egreso permiten filtrar los objetos en la base de datos según el titular de la compra
* Se ingresa el patrón de búsqueda (por ejemplo si se quiere encontrar aquellos ingresos/egresos con "st" en el nombre de titular), luego se presiona el botón "Buscar". Si se presiona "Buscar" con el campo vacio, o si se presiona "Restablecer filtro", se muestran todos los objetos

## Comenzando
Para abrir el servidor, estando sobre la carpeta del repositorio, se ejecuta:
```bash
python manage.py runserver
```

Luego, se accede a la página introduciendo 128.0.0.1/8000 en la barra de un buscador dentro de la misma PC donde se encuentra el servidor

De está forma se accede a la página principal. Se pueden explorar las funcionalidades como se explicó en el apartado anterior.