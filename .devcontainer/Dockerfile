# .devcontainer/Dockerfile

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first to use Docker caching
COPY ../requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Optional: install extra dev tools
RUN pip install streamlit fastapi uvicorn

# Keep container running (for dev environment)
CMD ["sleep", "infinity"]
