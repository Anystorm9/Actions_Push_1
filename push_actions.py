#!/usr/bin/env python3

import os
import time
import subprocess

# GitHub API configuration
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "Anystorm9"  # Replace with your username
REPO_NAME = "Actions_Push_1"  # Replace with your repository name
GITHUB_TOKEN = "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"  # Set your GitHub token as environment variable

def main():
    print("Script para hacer 7 commits y pushear al repositorio")

    # Configurar git si es necesario
    os.system('git config --global user.name "Automated User"')
    os.system('git config --global user.email "automated@example.com"')

    # Check if GitHub token is set
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set")
        print("Set your GitHub token as an environment variable:")
        print("export GITHUB_TOKEN='your_github_token'")
        return
# Configurar token de GitHub
    # Configurar URL del repositorio con token para autenticación automática
    repo_url = f"https://{GITHUB_TOKEN}@github.com/{REPO_OWNER}/{REPO_NAME}.git"

    # Hacer 7 commits
    for i in range(1, 8):
        print(f"Commit {i} de 7")

# Crear archivo de cambios
        with open('changes.txt', 'a') as f:
            f.write(f"Cambio {i}\n")

        # Agregar cambios y hacer commit
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', f'Commit automático update {i}'])

        # Pushear usando el token para autenticación automática
        subprocess.run(['git', 'push', repo_url, 'main'])

        print(f"Esperando 1 segundos antes del siguiente commit...")
        time.sleep(1)

    print("Proceso completado: 7 commits realizados y pusheados")

if __name__ == "__main__":
    main()