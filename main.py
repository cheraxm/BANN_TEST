# Flask
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import Flask, render_template, request
import json
app = Flask(__name__, template_folder='templates')

# Python.file Import
from _getRandom import *
from _sendEmail import *


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/', methods =["GET", "POST"])
def homepage():
    if request.method == "POST":
        if list(request.form.keys())[0] == 'bouquet_email_submit':
            pass
            # email_inerhtmlData = request.form['bouquet_email_submit']
            # sendCustomEmail(email_inerhtmlData)

        # elif list(request.form.keys())[0] == 'random_flower_repeat':
        elif request.form.get('random_flower_repeat') == 'REPEAT':
            mytest = createRandomSortedList()
            print(mytest[0])
            # return render_template('index.html', value= mytest[0])
            # return ('index.html', value= mytest[0]), 204
            return mytest[0]
            


        elif list(request.form.keys())[1] == 'random_flower_submit':
            username = request.form.get("username")
            receiver = request.form.get("receiver")
            createRandomSortedList()
            # print(username, receiver)



        # elif list(request.form.keys())[0] == 'mytest':
        #     username = request.form.get("username")
        #     receiver = request.form.get("receiver")
        #     print(username, receiver)

        # if request.form['action'] == 'bouquet_email_submit':
        #     emain_innerhtml = json.loads()    
        #     print(emain_innerhtml)
            # sendCustomEmail()
        # elif request.form['action'] == 'random_flower_submit':
        #     createRandomSortedList()
        return (''), 204

    else:
        return render_template('index.html')




@app.route('/mytest', methods =["GET", "POST"])
def mytest():
    if request.method == "POST":
       PriceInput = request.form.get("PriceInput")
       print(int(PriceInput) * 2)
       return (''), 204
    else:
        return render_template("mytest.html")


@app.route('/emailtemplate', methods =["GET", "POST"])
def emailtemplate():

    return render_template("emailtemplate.html")
        

    

if __name__ == '__main__':
    app.run(debug=True)

