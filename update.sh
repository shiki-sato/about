hugo --environment GithubProjectPage
mv docs/index.html docs/index.html_
python update.py
rm docs/index.html_
