from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', now=datetime.now())

if __name__ == '__main__':
  app.run()
  
'''
echo "# flask_deployment" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Kelvin-Data/flask_deployment.git
git push -u origin main


git init
git remote add origin https://github.com/Kelvin-Data/flask_deployment.git
git status
'''