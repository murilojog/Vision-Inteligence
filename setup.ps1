# PowerShell script to fully automate setup
$zipUrl = "https://raw.githubusercontent.com/SEU_USUARIO/vision-intelligence/main/vision_intelligence_repo_v2.zip"
$output = "$env:TEMP\vision_setup.zip"
Invoke-WebRequest -Uri $zipUrl -OutFile $output
Expand-Archive -LiteralPath $output -DestinationPath "$env:USERPROFILE\vision-intelligence"
cd "$env:USERPROFILE\vision-intelligence"
git init
git add .
git commit -m "Initial commit"
gh repo create SEU_USUARIO/vision-intelligence --public --source=. --remote=origin
git push -u origin main
Start-Process "https://github.com/SEU_USUARIO/vision-intelligence/releases"