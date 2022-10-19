# holded-filler
- Ingresar a Holded normalmente.
- Ir a control horario.
- Apretar F12 en Chrome para tener las herramientas de desarrollo activas. Ir a la pestaña "Network".
- Añadir un registro horario cualquiera.
- Aparecerán varios objetos en el log de "Network".
- Seleccionar el que tenga el nombre "updateday".
- Copiar de la 'request', dentro de sus headers, la 'cookie'.
- Sustituir por la cookie definida en el script de python, dentro del diccionario de headers.

- Poner una fecha de inicio en start_date y la final en end_date.
- Ajustar si se quiere las horas de inicio y final de cada día. 

- Ejecutar el script e ir a comprobar que se han rellenado los días.

- WARNING: Sobreescribir días ya aceptados por el supervisor es posible.
- WARNING: El script evita escribir los sábados y domingos, pero no sabe si tenías vacaciones o estabas de baja.
- INFO: El panel de "Ausencias" de Holded nos permitirá ver fácilmente que días no hay que rellenar.
