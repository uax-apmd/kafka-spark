#!/bin/bash
set -e

git config --global --add safe.directory /home/jovyan/work

pip install -r work/requirements.txt
