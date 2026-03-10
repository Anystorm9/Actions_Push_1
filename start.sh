#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Start Traffmonetizer in the background using the new (v2) command format ---
echo "Attempting to start Traffmonetizer client..." > /tmp/traffmonetizer.log

# The command 'start accept --token TOKEN' is the correct format for cli_v2
# All output (stdout & stderr) is redirected to the log file.
/usr/local/bin/traffmonetizer start accept --token nRH23jIoKQmwkBaKpB98aPUNZ/82fWIDEpfhjuWPodg= >> /tmp/traffmonetizer.log 2>&1 &

echo "Traffmonetizer v2 client started in background. Check /logs for status."

# --- Start Uvicorn in the foreground ---
echo "Starting web server..."
uvicorn app:app --host 0.0.0.0 --port 7860
