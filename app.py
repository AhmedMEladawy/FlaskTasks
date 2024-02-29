from flask import Flask,render_template,request,redirect,jsonify
from forms import SignupForm
app = Flask(__name__)
app.config["SECRET_KEY"]= 'ADAWY'

allemp = [
    
]



@app.route('/', methods=['GET'])
def home():
    return render_template('home.html',emps=allemp)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)

    elif request.method == 'POST' and form.validate_on_submit():
        fullname = form.fullname.data
        age = form.age.data
        department = form.department.data
        salary = form.salary.data
        allemp.append({"fullname": fullname,'age':age, "department": department, "salary": salary})
        return redirect('/')
app.run(debug=True,port=5000,host='127.0.0.1')

