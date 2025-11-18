#!/bin/bash
set -e

git config --global --add safe.directory /home/jovyan/kafka-spark

pip install -r work/requirements.txt
