from flask import Flask, render_template, url_for, request, redirect, flash
import pandas as pd
app = Flask(__name__)


@app.route('/')
def solution_print():
    return render_template("imp.html")


@app.route('/food_table/', methods=["GET", "POST"])
def food_table():
    return render_template('food_table.html')
    # text_document = open(" logindetails.txt " 'a')
    # text_document.write(request.form['email'])
    # text_document.write(request.form['password'])
    # text_document.write(20*'----')
    # text_document.close()

# return '%s'%format(data)
if __name__=='__main__':
    app.run(debug=True)
