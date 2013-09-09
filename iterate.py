import sys, datetime, time
from github import Github
import csv

def getrepos(username):
    user_repos = gh.get_user(username).get_repos()
    for user_repo in user_repos:
        print user_repo.name
        getcommits(username, user_repo.name, user_repo)
        #outputter.writerow([username,(str(user_repo).strip('<Repo (')).strip(')>')])

def getcommits(username, repo_name, user_repo):
    #gh.repos.commits.list(user=username, repo=user_repo)
    user_commits = user_repo.get_commits()
    i = 0
    for commit in user_commits:
        if (commit.committer.name == username):
            i = i + 1
            print commit + ' belongs to ' + username
    languages = user_repo.get_languages()
    for language in languages:
        print language
        outputter.writerow([username,repo_name,i,language])

pass_string = open('pass.txt', 'r').read()
gh = Github('wikiteams',pass_string)

with open('top-users-final.csv', 'rb') as source_csvfile:
    usersReader = csv.reader(source_csvfile, delimiter=',', quotechar='\'')
    with open('users-repos-skills.csv', 'wb') as csvfile:
        outputter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in usersReader:
            print row[0]
            getrepos(str(row[0]))

outputter.close()
csvfile.close()