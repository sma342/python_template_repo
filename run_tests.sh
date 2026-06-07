#!/bin/bash
echo "=== Odpalanie mrocznych testów na oryginalnym kodzie ==="

# Wymuszenie szukania modułów w bieżącym katalogu projektu
export PYTHONPATH=.

"/c/Program Files/Python313/python.exe" -m unittest discover -s tests

echo "Testy zakończone."