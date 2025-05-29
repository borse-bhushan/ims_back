printf '\033[5;31m'
base64 -d './config/name_base64.txt'
printf '\033[0m'

echo ""

coverage run -m pytest --cov-report=term-missing
coverage report
coverage html
