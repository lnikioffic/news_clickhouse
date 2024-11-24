#!/bin/sh

python3 migration.py

python3 fill_db.py

uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4