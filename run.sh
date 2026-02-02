#!/bin/bash
# Run FastAPI application (uses port from src/config.py)

source venv/bin/activate
# Use the venv's Python directly to avoid shell alias issues
"$VIRTUAL_ENV/bin/python" run.py
