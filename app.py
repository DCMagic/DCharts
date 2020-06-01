# -*- coding: UTF-8 -*-
'''
@Project -> File   ：DCharts -> app
@IDE    ：PyCharm
@Author ：Mr. Dong
@Date   ：2020/6/1 19:09
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
