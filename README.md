Explicación del código:
Interfaz principal: Se crea una ventana principal con un título y dimensiones definidas utilizando la librería Tkinter.
Componentes GUI:
Label: Muestra una etiqueta que indica al usuario que debe ingresar un elemento.
Entry: Campo de texto donde el usuario puede escribir el dato.
Button: Un botón "Agregar" para agregar el dato ingresado a la lista, y otro botón "Limpiar" para borrar todos los datos de la lista.
Listbox: Una lista que muestra los elementos agregados por el usuario.
Funcionalidad:
Al hacer clic en el botón "Agregar", se toma el contenido del campo de texto, se agrega a la lista y se limpia el campo de texto.
El botón "Limpiar" borra todos los elementos en la lista.
Eventos: La aplicación responde a los clics de los botones mediante las funciones agregar_item y limpiar_lista.
