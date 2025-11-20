# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

PowerBI AI Analytics is a small FastAPI-based backend service intended to provide AI-powered analytics for Power BI dashboards. The current implementation exposes only basic informational endpoints, but the stack and layout are ready to grow into a richer API.

## Repository Layout

- `backend/` — Python backend service built with FastAPI.
  - `main.py` — FastAPI app entrypoint and route definitions.
  - `requirements.txt` — Python dependencies for the backend service.
- `.gitignore` — Standard ignores for Python, Node, and common OS artifacts.

There is currently no frontend, infra, or test directory checked into the repo.

## Backend Architecture

- **Framework**: FastAPI.
- **Application entrypoint**: `backend/main.py` defines the FastAPI `app` instance.
- **Routes**:
  - `GET /health` — simple health-check endpoint returning basic service status.
  - `GET /api/v1/info` — returns static metadata about the service (name, description, list of AI modes).
- **AI Analytics behavior**: as of now, the AI-related modes are declared in the response of `/api/v1/info` but not yet implemented as separate endpoints or services.

As the project grows, additional routers, services, and models should be organized under `backend/` (e.g., `routers/`, `services/`, `models/`) and wired into `app` from `main.py`.

## Development Environment

- **Language**: Python (>=3.10 recommended for FastAPI + Pydantic v2 and modern async support).
- **Virtual environment**: use your preferred tool (e.g., `python -m venv .venv`), which will be ignored by Git via `.gitignore`.

### Dependency Management

From the repository root:

- Create and activate a virtual environment (PowerShell example):
  ```powershell path=null start=null
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

- Install backend dependencies:
  ```powershell path=null start=null
  pip install -r backend/requirements.txt
  ```

## Running the Application

All commands are assumed to be run from the repository root (`powerbi-ai-analytics`).

### Start the FastAPI server (development)

- Run with Uvicorn auto-reload:
  ```powershell path=null start=null
  uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
  ```

- After starting, key URLs:
  - `http://localhost:8000/health` — health check.
  - `http://localhost:8000/api/v1/info` — basic service info.
  - `http://localhost:8000/docs` — FastAPI Swagger UI.
  - `http://localhost:8000/redoc` — FastAPI ReDoc UI.

If `uvicorn` is not on the PATH, ensure your virtual environment is activated before running the command.

## Testing and Quality

No testing or linting configuration is currently present in the repository (no `tests/` folder or lint config files). Before using test or lint commands, verify or introduce the appropriate tooling (e.g., `pytest`, `ruff`, `black`) and update this section.

## How Warp Should Work in This Repo

- Prefer editing backend code under `backend/`, keeping `main.py` as the central place where the FastAPI app is assembled and routes are included.
- When adding new API functionality, introduce separate modules (e.g., routers or services) instead of putting all logic directly in `main.py`, and then wire them into the `app` instance from there.
- When you add tests or additional tooling (lint/type-check), also append the corresponding common commands to this `WARP.md` so future Warp instances know how to run them.
