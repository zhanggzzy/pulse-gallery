# phase 1: frontend
FROM node:18 AS frontend-builder

WORKDIR /app
COPY src/frontend ./frontend
WORKDIR /app/frontend
RUN npm install
RUN npm run build

# phase 2: backend
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy backend source code
COPY src/backend ./src/backend

# copy frontend build output
COPY --from=frontend-builder /app/frontend/dist ./static

# copy database
COPY data/database ./data/database
ENV DB_PATH=/app/data/database/database.db


CMD ["uvicorn", "src.backend.main:app", "--host", "0.0.0.0", "--port", "8000"]