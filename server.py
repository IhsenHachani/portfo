from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/templates")
def my_home():
    return render_template("index.html")

@app.route('/templates/<string:page_name>')
def other_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject=data["subject"]
        message=data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_csv_file(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer = csv.writer(database2,  delimiter='|', lineterminator='\n', quotechar=',',  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        try:
            data = request.form.to_dict()
            write_csv_file(data)
            return redirect('/templates/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again'




@app.route("/")
def hello():
    return "WELCOME WEBSERVER THANKS"
    