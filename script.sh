#!/bin/bash

set -euxo pipefail

if [ "$#" -eq 0 ]; then
  echo "Usage: $0 <function_name>"
  exit 1
fi

function lint() {
  uv run ruff check ./**/**.py
  uv run pyright
}

function format() {
  uv run ruff format
}

function check() {
  uv run ruff format --check
  lint
}

case "$1" in
lint)
  lint
  ;;
format)
  format
  ;;
check)
  check
  ;;
*)
  echo "Unknown function: $1"
  exit 1
  ;;
esac
