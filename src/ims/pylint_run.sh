if [[ "outside" != "$1" ]]; then
  echo
  printf '\033[5;31m'
  base64 -d './config/name_base64.txt'
  printf '\033[0m'
fi

if command -v title &>/dev/null; then
  title "IMS"
fi

echo ""

python -m pylint ./
echo "--------------------------------------------------------------------"
