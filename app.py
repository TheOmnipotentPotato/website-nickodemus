from flask import Flask, request, jsonify, render_template, Response
from physics_sims import ball


app = Flask(__name__)

#Defining global constants for simulations
#Ballistic sim
Ball = ball()
Ball.reset()
ball_data =[]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chem')
def chem():
    return render_template('chem.html')

@app.route('/phys', methods=['GET', 'POST'])
def phys():
    if request.method == 'POST':
        if request.form.get('clear') == 'clear':
            ball_data.clear()
            print('request recived cock suckers')
        else:    
            Ball.reset()
            local_data=Ball.throw(float(request.form.get('theta')), float(request.form.get('magnatude')), float(request.form.get('initial height')))
            for i in range(len(local_data)):
                ball_data.append(local_data[i])
            print('Request Recived')
    return render_template('phys.jinja2', ball_data=ball_data)

@app.route('/phys_ballistic', methods=['GET', 'POST'])
def phys_1():
    if request.method == 'POST':
        if request.form.get('simulate') == 'simulate':
            labels = [row[0] for row in ball_data]
            values = [row[1] for row in ball_data]
            print(values)
            print(labels)
            return render_template('phys_ballistic.jinja2', labels=labels, values=values)
    return render_template('phys_ballistic.jinja2', labels=[], values=[])

@app.route('/math')
def math():
    return render_template('math.html')

@app.route("/form", methods=["GET", "POST"])
def form():
    a_list_of_pain =[]
    print(request.form)
    print(request.form.get("account"))
    a_list_of_pain.append((request.form.get('date'), request.form.get('amount'), request.form.get('account')))
    print(a_list_of_pain)
    return render_template("form.html")


if __name__ == '__main__':
    app.run()
