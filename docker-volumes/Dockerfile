# Use a minimal, stable base image
FROM python:3.14.0-slim

# Set a non-root user for runtime security
RUN useradd --create-home appuser

# Create volume directory with correct permissions
RUN mkdir -p /data && chown appuser:appuser /data

# Declare volume
VOLUME ["/data"]

# Set working directory and copy app code
WORKDIR /app
COPY . /app

# Set ownership of app files
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Install only what's needed, and pin versions
RUN pip install --no-cache-dir flask==3.0.0

# Expose only the required port
EXPOSE 8080

# Use ENTRYPOINT for fixed behavior
ENTRYPOINT ["python", "/app/greet.py"]

# Add a basic healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:8080 || exit 1