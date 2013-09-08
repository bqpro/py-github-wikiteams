import sys, datetime, time
from pygithub3 import Github, exceptions
import csv

def getrepos(username):
    user_repos = gh.repos.list(username).all()
    for user_repo in user_repos:
        print user_repo
        #getcommits(username, user_repo)
        outputter.writerow([username,(str(user_repo).strip('<Repo (')).strip(')>')])

def getcommits(username, user_repo):
    #gh.repos.commits.list(user=username, repo=user_repo)
    for user_commit in gh.repos.commits.list(user=username, repo=user_repo):
        print user_commit
        #gives error 404.. time to move to https://github.com/jacquev6/PyGithub instead of pygithub3

pass_string = open('pass.txt', 'r').read()
gh = Github(user='wikiteams',login='wikiteams',password=pass_string)

with open('top-users-final.csv', 'rb') as source_csvfile:
    usersReader = csv.reader(source_csvfile, delimiter=',', quotechar='\'')
    with open('users-repos-skills.csv', 'wb') as csvfile:
        outputter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in usersReader:
            print row[0]
            getrepos(str(row[0]))

outputter.close()
csvfile.close()