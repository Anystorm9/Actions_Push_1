#!/bin/bash

# Script para gestionar el ciclo de vida de los contenedores rds

while true
do
    echo "-------------------------------------"
    echo "INICIANDO NUEVO CICLO..."
    echo "-------------------------------------"

    # 1. Iniciar 1 contenedor en segundo plano
    echo "Iniciando contenedor rds usando la imagen 'rds'..."
    docker run -d --name rds rds
    if [ $? -eq 0 ]; then
        echo "✅ Contenedor rds iniciado correctamente."
    else
        echo "❌ Error al iniciar el contenedor rds. Asegúrate de que no haya un contenedor con el mismo nombre (incluso detenido)."
    fi

    # 2. Mantenerlo abierto por 4 minutos
    echo -e "\nContenedor iniciado. Esperando 4 minutos..."
    sleep 240

    # 3. Detener el contenedor
    echo -e "\nDeteniendo el contenedor..."
    docker stop rds
    echo "Contenedor rds detenido."

    # 4. Eliminar el contenedor
    echo -e "\nEliminando el contenedor..."
    docker rm rds
    echo "Contenedor rds eliminado."

    echo -e "\nCiclo completado. El próximo ciclo comenzará en 10 segundos."
    sleep 10
done
