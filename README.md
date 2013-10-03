GitHub skills dataset creator
===================

This software is available to public

Copyright (C) 2013 - **WikiTeams contributors**

py-github-wikiteams is for free. You don't have to pay for it, and you can use it any way you want. It is developed as an Open Source project under the GNU General Public License (GPL). That means you have full access to the source code of this program. You can find it on our website at https://github.com/wikiteams/py-github-wikiteams Should you wish to modify or redistribute this program, or any part of it, you should read the full terms and conditions set out in the license agreement before doing so. A copy of the license is available on our website. If you simply wish to install and use this software, you need only be aware of the disclaimer conditions in the license, which are set out below. NO WARRANTY Because the program is licensed free of charge, there is no warranty for the program, to the extent permitted by applicable law. Except when otherwise stated in writing the copyright holders and/or other parties provide the program "as is" without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of the program is with you. Should the program prove defective, you assume the cost of all necessary servicing, repair or correction. In no event unless required by applicable law or agreed to in writing will any copyright holder, or any other party who may modify and/or redistribute the program as permitted above, be liable to you for damages, including any general, special, incidental or consequential damages arising out of the use or inability to use the program (including but not limited to loss of data or data being rendered inaccurate or losses sustained by you or third parties or a failure of the program to operate with any other programs), even if such holder or other party has been advised of the possibility of such damages.

<p align="center"><img src="http://liveexpert.pl/github-mascote-skills.png" /></p>

#### This project allows to parse big number of users skills statistics (by pull requests) of "most active GitHub users" using (by choice) GitHub API (with CoffeeScript) and/or Google BigQuery. Data is later used for machine learning and predicting on which project a hypotetical new GitHub user would like to work on.

*Branches: head, pygithub*

Merged to head (as on 19.09.2013), pygithub is a dev-branch

##### Data already collected:

###### users and their pull requests.csv

*It's a base for big data analysis and machine learning*

*It holds all PULL REQUESTS, in a format: `repository name`, `count of skill (language)`, `skill (language) name`, `user`*

###### top-users-final.csv

*It holds most active GitHub users (by paulmillr conditions) and their 3 most often used languages*

###### users-repos-skills.csv

*It holds also their repos*

######logins-only.csv

*It holds only their logins*

##### Google bigquery

*It works by querying Google GitHub timeline for fields:* `repository_name`, `count(payload_pull_request_head_repo_language)`, `payload_pull_request_head_repo_language`, `payload_pull_request_head_user_login`
and grouping them by `payload_pull_request_head_user_login`, `payload_pull_request_head_repo_language`, `repository_name`

##### Input for iterate.py script

CSV file in format:

`'fabpot'`

`'weierophinney'`

`'visionmedia'`

etc. (plain username)

##### Output

CSV file in format:

username, repo

example:

`fabpot, linux_kernel3`

`fabpot, swap_unix`

#### Learning function

This is the data we input to the learning machine during LEARNING PHASE:

`{user: {Skills:experience}, label}` , `{repository: {Skills:statistics}, label}`

which means a set of users and their contribution to repositories characterized by language and intensivity (how many times contributed)

and later for standard input we enter hypothetical users:

`{user: {Skills:experience}}`

for every user, we want on output a repository which he will probably would enjoy (repo already existing in dataset from learning phase)
