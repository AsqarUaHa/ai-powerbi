#!/usr/bin/env bash
set -e

cd backend
pip install -r requirements.txt

# Запуск сервера (подставь свой модуль и app при необходимости)
uvicorn main:app --host 0.0.0.0 --port 8000
