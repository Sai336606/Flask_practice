from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# now the Data is adding in this variable
Jobs = [
  {
    'id': 1,
    'title': 'Python Developer',
    'company': 'Google',
    'location': 'Banglore',
    'salary': '10LPA'
  },
  {
    'id': 2,
      'title': 'Front-end Developer',
      'company': 'Meta',
      'location': 'usa',
      'salary': '$120,000'
    },
  {
  'id': 3,
    'title': 'Back-End Developer',
    'company': 'Volvo',
    'location': 'India',
    'salary': '12 lpa'
  },
  {
  'id': 4,
    'title': 'AI Developer',
    'company': 'Open Ai',
    'location': 'usa',
    # 'salary': '$180,000'
  }
]
@app.route('/')
def hello_world():
  return render_template("home.html",jobs=Jobs,company='Mostly AI')


# api route using json alternative to HTML 
@app.route('/api/jobs')
def jobs():
  return jsonify(Jobs)

if __name__ == "__main__":
  app.run('0.0.0.0',debug=True)