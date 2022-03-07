. .\.venv\Scripts\Activate.ps1

if ($?) {
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
}
