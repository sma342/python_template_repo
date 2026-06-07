#!/bin/bash
echo "=== Formatowanie kodu (Black) ==="

"/c/Program Files/Python313/python.exe" -m black .

echo "=== Sprawdzanie poprawności formatowania ==="
"/c/Program Files/Python313/python.exe" -m black --check .