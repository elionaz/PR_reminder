import requests
from dotenv import load_dotenv
import os
from dateutil.parser import parse
from datetime import datetime, timedelta

# Carga las variables del archivo .env
load_dotenv()

def get_repos(org, token):
    url = f"https://api.github.com/orgs/{org}/repos"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # ensure we notice bad responses
    return response.json()

def get_open_pull_requests(user, repo, token):
    url = f"https://api.github.com/repos/{user}/{repo}/pulls"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers, params={"state": "open"})
    response.raise_for_status()  # ensure we notice bad responses
    pull_requests = response.json()

    # Filtra los pull requests que han estado abiertos durante más de 24 horas
    pull_requests = [pr for pr in pull_requests if datetime.now(parse(pr["created_at"]).tzinfo) - parse(pr["created_at"]) > timedelta(hours=24)]

    return pull_requests

# Uso de las funciones:
org = os.getenv("ORG")
token = os.getenv("TOKEN")
repos = get_repos(org, token)
for repo in repos:
    print(f'Repositorio: {repo["name"]}')
    pull_requests = get_open_pull_requests(org, repo["name"], token)
    for pr in pull_requests:
        print(f'  PR: {pr["title"]} - URL: {pr["html_url"]}')

