from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Digital Artist',
  'location': 'Baguio, Philippines',
  'salary': '₱ 32,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Manila, Philippines',
  'salary': '₱ 55,000'
}, {
  'id': 3,
  'title': 'Layout Artist',
  'location': 'Ifugao, Philippines',
  'salary': '₱ 28,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'California, USA',
  'salary': '$ 120,000'
}]


@app.route("/")
def hello_world():
  return render_template('Home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
