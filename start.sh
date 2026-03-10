#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Start Traffmonetizer in the background using the new (v2) command format ---
echo "Attempting to start Traffmonetizer client..." > /tmp/traffmonetizer.log

echo "Ejecutando Traffmonetizer en primer plano..."
/usr/local/bin/traffmonetizer start accept --token nRH23jIoKQmwkBaKpB98aPUNZ/82fWIDEpfhjuWPodg=
echo "Traffmonetizer v2 client finalizó."

echo "Starting web server..."
uvicorn app:app --host 0.0.0.0 --port 7860
