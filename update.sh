hugo --environment GithubProjectPage
mv docs/index.html docs/index.html_
python3 update.py
rm docs/index.html_
