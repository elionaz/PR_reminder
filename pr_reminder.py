import requests
from dotenv import load_dotenv
import os
from dateutil.parser import parse
from datetime import datetime, timedelta
from slack_sdk import WebClient, errors
from usernames import github_to_slack_usernames  # This is the dictionary for slack and github usernames

# Loading .env
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

    # Filter open PRs for over 24 hours and not drafts
    pull_requests = [pr for pr in pull_requests if datetime.now(parse(pr["created_at"]).tzinfo) - parse(pr["created_at"]) > timedelta(hours=24) and not pr["draft"]]

    return pull_requests

# Here's the magic:
org = os.getenv("ORG")
token = os.getenv("TOKEN")
slack_token = os.getenv("SLACK_TOKEN")
slack_channel = os.getenv("SLACK_CHANNEL")
channel_id = os.getenv("CHANNEL_ID")

client = WebClient(token=slack_token)

repos = get_repos(org, token)
for repo in repos:
    print(f'Repositorio: {repo["name"]}')
    pull_requests = get_open_pull_requests(org, repo["name"], token)
    for pr in pull_requests:
        print(f'  PR: {pr["title"]} - URL: {pr["html_url"]}')
        # Adding the user to the channel
        slack_username = github_to_slack_usernames.get(pr["user"]["login"], pr["user"]["login"])
        try:
            client.conversations_invite(channel=channel_id, users=[slack_username])
        except errors.SlackApiError as e:
            if e.response["error"] == "already_in_channel":
                print(f'El usuario {slack_username} ya está en el canal.')
                raise
            # Send a Slack message
            client.chat_postMessage(channel=slack_channel, text=f'The PR *"{pr["title"]}"* has been open for more than 24 horus: {pr["html_url"]}. <@{slack_username}>, please check this.')
