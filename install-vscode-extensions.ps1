# VS Code Extensions Installation Script for Python Web Development on Azure

Write-Host "Installing VS Code Extensions..." -ForegroundColor Green

# Define extensions to install
$extensions = @(
    "ms-python.python",
    "GitHub.copilot", 
    "GitHub.copilot-chat",
    "ms-azuretools.vscode-azureappservice",
    "ms-azuretools.vscode-bicep"
)

# Install each extension for current user
foreach ($ext in $extensions) {
    Write-Host "Installing: $ext" -ForegroundColor Cyan
    code --install-extension $ext
}

Write-Host "Extensions installation completed!" -ForegroundColor Green
