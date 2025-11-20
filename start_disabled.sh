#!/usr/bin/env bash
set -e

cd backend

# Просто на всякий случай покажем версию Python в логах
python --version || python3 --version

# ВАЖНО: запуск через python -m uvicorn, а не просто "uvicorn"
python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
