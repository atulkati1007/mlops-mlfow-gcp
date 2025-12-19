# Official uv image with Python 3.11 (slim Debian base)
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

# Recommended for logs
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Optional: Avoid random hashes if needed
# ENV PYTHONHASHSEED=0

# Avoid this unless you have a specific reason (it hurts performance)
# ENV PYTHONDONTWRITEBYTECODE=1

# Install the only system dependency LightGBM needs at runtime
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgomp1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY  requirements.txt .

RUN uv pip install --system --no-cache -r requirements.txt

COPY . .

RUN python pipeline/training_pipeline.py

EXPOSE 5000

CMD ["python", "application.py"]