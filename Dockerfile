# Multi-stage build for optimized image size

# Stage 1: Build frontend
FROM node:18-alpine AS frontend-build

WORKDIR /app/frontend

# Copy frontend files
COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# Stage 2: Backend with Chrome - Using Ubuntu with Vietnam mirror
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Use Vietnam mirror for faster downloads and add retry config
RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|http://vn.archive.ubuntu.com/ubuntu/|g' /etc/apt/sources.list && \
    sed -i 's|http://security.ubuntu.com/ubuntu/|http://vn.archive.ubuntu.com/ubuntu/|g' /etc/apt/sources.list && \
    echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/80-retries && \
    echo 'Acquire::http::Timeout "20";' >> /etc/apt/apt.conf.d/80-retries && \
    echo 'Acquire::https::Timeout "20";' >> /etc/apt/apt.conf.d/80-retries && \
    echo 'Acquire::Check-Valid-Until "false";' >> /etc/apt/apt.conf.d/80-retries

# Install Python, Chrome and dependencies with retries
RUN apt-get update -o Acquire::CompressionTypes::Order::=gz && \
    apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    wget \
    gnupg \
    unzip \
    curl \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libwayland-client0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY backend/requirements.txt ./backend/
RUN pip3 install --no-cache-dir -r backend/requirements.txt

# Copy backend code
COPY backend/ ./backend/

# Copy built frontend from stage 1
COPY --from=frontend-build /app/frontend/dist ./frontend/dist

# Create directory for credentials
RUN mkdir -p /app/data

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production
ENV CHROME_BIN=/usr/bin/google-chrome-stable
ENV DISPLAY=:99

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:5000/api/health || exit 1

# Start the application
WORKDIR /app/backend
CMD ["python3", "app.py"]
