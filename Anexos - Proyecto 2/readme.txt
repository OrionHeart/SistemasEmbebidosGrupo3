+ alexaCheck.service: Es el daemon que desarollamos para reiniciar el servicio alexa-pi cuando se requiere en caso de desconexión de internet o de la tarjeta de sonido externa USB.
+ AlexaPi.service: El es daemon que desarorollamos para el servicio alexa-pi.
+ checkScript: Es el script que revisa el estado de la conexión a internet y a la tarjeta de sonido externa USB, y en caso de que suceda una reconexión a internet o una reconexión a la tarjeta de sonido externa, reinicia el servicio "AlexaPi.service"
+ VID001: Pruebas de alexa-pi. Disponible en https://youtu.be/bMKm_GXY-c8
+ VID002: Escenarios de falla de alexa-pi. Disponible en https://youtu.be/Vagk_pU9mag
+ VID003: Pruebas de la solución con crontab. Disponible en https://youtu.be/MsRgHkdhlfA
+ VID004: Pruebas de la solución con systemd y el script de checkeo. Disponible en https://youtu.be/CtPk5NswGCY