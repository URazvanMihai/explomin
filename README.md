# <b>Explomin</b>

# Commands
## GIT
Clone repository from GitHub<br>
<code>git clone repo-url</code>

Create new branch<br>
<code>git checkout -b branch-name</code>

Change branch<br>
<code>git checkout branch-name</code>

Show current changes<br>
<code>git status</code>

Add all files for commit<br>
<code>git add .</code>

Add specific file for commit<br>
<code>git add file-name</code>

Add file for commit<br>
<code>git commit -m "insert message"</code>

Push to GitHub<br>
<code>git push</code>

Pull from GitHub<br>
<code>git pull</code>

Merge branch into another branch<br>
Example: merge <b>main</b> into <b>pontaj</b>

1. Pull new changes from <b>main</b><br>
<code>git checkout main </code><br>
<code>git pull </code>

1. Switch to <b>pontaj</b> (commit/stash all changes before merge)<br>
<code>git checkout pontaj </code><br>
<code>git merge main </code>

## Python

### Create virtual env
1. Install virtual env (tool to setup Python environments)<br>
<code>pip install virtualenv</code>
2. Create virtual environment [How to setup virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)<br>
<code> python -m venv venv</code>
3. Activate virtual environment<br>
<code>source venv/bin/activate (mac)</code><br>
<code>source venv/Scripts/activate (windows)</code>
4. Install project packages (make sure venv is activated)<br>
<code>pip install -r requirements.txt</code>

## Django

### Database
Create migrations<br>
<code>python manage.py makemigrations</code><br>

Apply migrations<br>
<code>python manage.py migrate</code>

Start server<br>
<code>python manage.py runserver</code>
