# ---------- Build Stage ----------
FROM python:3.14.0-slim AS builder

WORKDIR /app

# Copy only what's needed to install dependencies
COPY requirements .

# Install packages into /app/.local using --prefix 
RUN pip install --upgrade pip \
  && pip install --no-cache-dir --prefix=/app/.local -r requirements

# ---------- Final Stage ----------
FROM python:3.14.0-slim

# Create non-root user
RUN useradd --create-home appuser

# Set environment variables for Python and PATH
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/home/appuser/.local/bin:$PATH \
    PYTHONPATH=/home/appuser/.local/lib/python3.14/site-packages

WORKDIR /app

# Copy installed packages and app code
COPY --from=builder /app/.local /home/appuser/.local
COPY greet.py .
COPY requirements .

# Set ownership and switch to non-root user
RUN chown -R appuser /app /home/appuser
USER appuser

EXPOSE 8080

ENTRYPOINT ["python", "/app/greet.py"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:8080 || exit 1