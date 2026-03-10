# Stage 1: Get the traffmonetizer binary from its official image
FROM docker.io/traffmonetizer/cli_v2:latest AS builder

# Stage 2: Set up our final Python environment
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the traffmonetizer binary from the first stage into our final image
COPY --from=builder /usr/local/bin/cli /usr/local/bin/traffmonetizer
RUN chmod +x /usr/local/bin/traffmonetizer

#@## Copy our application files
COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py
COPY ./start.sh /app/start.sh

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make the start script executable
RUN chmod +x /app/start.sh

# Expose the port our FastAPI app runs on
EXPOSE 7860

# Run our start script
CMD ["/app/start.sh"]
