#!/usr/bin/env bash
set -e

cd backend

# На всякий случай выводим версию Python, чтобы видеть, что он есть
python --version || python3 --version

# Запуск через модуль, а не через бинарь uvicorn
python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
