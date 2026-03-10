from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    logger.info("--- FastAPI Application Startup ---")
    logger.info("The Traffmonetizer client should be running in the background, managed by the Docker CMD.")
    logger.info("Log file is expected at: /tmp/traffmonetizer.log")

@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "FastAPI server is running. Traffmonetizer client is managed in the background.\n"

@app.get("/logs", response_class=PlainTextResponse)
def get_logs():
    log_path = "/tmp/traffmonetizer.log"
    try:
        with open(log_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Log file not found at {log_path}. The client might still be initializing or may have failed to start.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while reading the log file: {e}")
