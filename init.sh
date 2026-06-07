#!/bin/bash
echo "=== Inicjalizacja brytyjskiego padołu łez ==="

PYTHON_PATH="/c/Program Files/Python313/python.exe"

if [ -f "$PYTHON_PATH" ]; then
    echo "Znaleziono właściwego Pythona 3.13."
else
    echo "Błąd: Nie znaleziono Pythona w $PYTHON_PATH"
    exit 1
fi

"$PYTHON_PATH" -m pip install --upgrade pip
"$PYTHON_PATH" -m pip install black pylint

echo "Zależności zainstalowane pomyślnie. Cheers! ☕"