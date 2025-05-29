printf '\033[5;31m'
base64 -d './config/name_base64.txt'
printf '\033[0m'

file_path="./logs/ims.log"

if [ ! -f "$file_path" ]; then
  mkdir "logs"
  touch "./logs/ims.log"
fi

if command -v title &>/dev/null; then
  title "IMS"
else
  echo ""
fi

echo ""

# bash pylint_run.sh outside

python manage.py runserver 0.0.0.0:8000
