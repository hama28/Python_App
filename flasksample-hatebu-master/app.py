from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    hatebu_array = []

    r = requests.get('http://b.hatena.ne.jp/')
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.select("div.entrylist-contents-main"):
        title = div.h3
        url = div.a
        user = div.span
        user_num = user.getText().split(" ")
        keisai = div.p

        if int(user_num[0]) >= 300:
            data_list = []
            data_list.append(title.getText())
            data_list.append(url.get('href'))
            data_list.append(user.getText())
            data_list.append(keisai.getText())
            hatebu_array.append(data_list)
        else:
        	next

    return render_template('index.html',hatebu_array=hatebu_array)

if __name__ == '__main__':
    app.debug = True
    app.run()
