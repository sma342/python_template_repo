#!/bin/bash
echo "=== Analiza statyczna oryginalnego kodu (Pylint) ==="

export PYTHONPATH=.

"/c/Program Files/Python313/python.exe" -m pylint main.py logic/