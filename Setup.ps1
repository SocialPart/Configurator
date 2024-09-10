# Проверка, установлен ли pyenv
if (Get-Command pyenv -ErrorAction SilentlyContinue) {
    Write-Host "pyenv уже установлен."
} else {
    Write-Host "pyenv не установлен. Устанавливаем pyenv..."

    # Установка pyenv-win
    git clone https://github.com/pyenv-win/pyenv-win.git $env:USERPROFILE\.pyenv

    # Добавление pyenv в PATH
    [System.Environment]::SetEnvironmentVariable('PYENV', "$env:USERPROFILE\.pyenv", [System.EnvironmentVariableTarget]::User)
    [System.Environment]::SetEnvironmentVariable('Path', "$env:USERPROFILE\.pyenv\pyenv-win\bin;$env:USERPROFILE\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('Path', [System.EnvironmentVariableTarget]::User), [System.EnvironmentVariableTarget]::User)

    Write-Host "pyenv установлен. Перезапустите терминал для применения изменений."
}

# Установка нужной версии Python, если она указана в .python-version или используется версия по умолчанию
$pythonVersion = Get-Content .python-version -ErrorAction SilentlyContinue
if (-not $pythonVersion) {
    $pythonVersion = "3.9.5"
}

# Проверка, установлена ли нужная версия Python
if (pyenv versions | Select-String $pythonVersion) {
    Write-Host "Python $pythonVersion уже установлен."
} else {
    Write-Host "Устанавливаем Python $pythonVersion..."
    pyenv install $pythonVersion
}

# Установка локальной версии Python для проекта
pyenv local $pythonVersion

Write-Host "Установка завершена. Версия Python $pythonVersion активирована для проекта."
