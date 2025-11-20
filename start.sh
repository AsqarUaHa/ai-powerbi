#!/usr/bin/env bash
set -e

cd backend

# Railway обычно даёт порт через переменную PORT
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
