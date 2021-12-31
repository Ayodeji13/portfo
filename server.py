from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
#function for homepage route
def my_home():
    return render_template('index.html')

#to dynamically route web pages
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#function to write data from website to txt file
def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write(f'\n{email},{subject},{message}')

#function to write data from website to csv file
def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
#function to submit form and save data
def submit_form():
    if request.method == 'POST':
      #to handle the rewuest
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
      except:
        return 'did not save to database'
    else:
      return 'something went wrong. Try again!'
