#!/usr/bin/env python3
import requests
import os
from datetime import datetime

# Repository info (replace with your repo details)
OWNER = "Knoph1"
REPO = "your-repo-name"  # <- replace with your actual repo name

# GitHub API setup
TOKEN = os.getenv("GITHUB_TOKEN")
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

def fetch_stats():
    repo_data = requests.get(API_URL, headers=HEADERS).json()
    commits_data = requests.get(API_URL + "/commits", headers=HEADERS).json()
    issues_data = requests.get(API_URL + "/issues", headers=HEADERS, params={"state": "all"}).json()
    pulls_data = requests.get(API_URL + "/pulls", headers=HEADERS, params={"state": "all"}).json()

    stats = {
        "repo_name": repo_data.get("name", "Unknown"),
        "stars": repo_data.get("stargazers_count", 0),
        "forks": repo_data.get("forks_count", 0),
        "watchers": repo_data.get("subscribers_count", 0),
        "open_issues": repo_data.get("open_issues_count", 0),
        "total_commits": len(commits_data) if isinstance(commits_data, list) else 0,
        "total_issues": len(issues_data) if isinstance(issues_data, list) else 0,
        "total_pull_requests": len(pulls_data) if isinstance(pulls_data, list) else 0,
        "last_updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
    }
    return stats

def update_stats_md(stats):
    content = f"""# 📊 Repository Stats: {stats['repo_name']}

- ⭐ Stars: {stats['stars']}
- 🍴 Forks: {stats['forks']}
- 👀 Watchers: {stats['watchers']}
- 🐛 Open Issues: {stats['open_issues']}
- 📝 Total Issues (All States): {stats['total_issues']}
- 🔃 Pull Requests: {stats['total_pull_requests']}
- 📜 Commits (Latest Batch): {stats['total_commits']}

_Last Updated: {stats['last_updated']}_

"""
    with open("STATS.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    stats = fetch_stats()
    update_stats_md(stats)
    print("✅ STATS.md updated successfully!")
