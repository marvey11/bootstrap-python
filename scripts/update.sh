#! /bin/bash

source .venv/Scripts/activate || exit

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
