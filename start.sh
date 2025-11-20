#!/usr/bin/env bash
set -e

cd backend

# Только запуск приложения, БЕЗ pip install
uvicorn main:app --host 0.0.0.0 --port 8000
