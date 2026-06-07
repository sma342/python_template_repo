#!/bin/bash
echo "=== Sprzątanie londyńskiego smogu (Czyszczenie repo) ==="

find . -type d -name "__pycache__" -exec rm -rf {} +
rm -rf .black_cache
rm -rf .pylint.d

echo "Repozytorium jest czyste i puste... jak dusza poety."