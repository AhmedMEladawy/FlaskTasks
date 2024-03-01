from flask import Flask, render_template, request, redirect, jsonify
from forms import LoginForm, SignupForm
from flask_sqlalchemy import SQLAlchemy

DATABASE_URL = 'sqlite:///day2lab.db'
# DATABASE_URL='postgres://username:password@localhost:5432/dbname'
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
db = SQLAlchemy(app)

class Department(db.Model):
    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    employees = db.relationship("Employee", backref="department")

    def __repr__(self):
        return f'Department id={self.id}, name={self.name}' 
    
class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    salary = db.Column(db.Float)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    # department = db.relationship("Department", foreign_keys=[department_id])
    def __repr__(self):
                
                return f"{self.name}"

@app.route('/departments', methods=['GET', 'POST'])
def departments():
    if request.method == "GET":
        dept_list = Department.query.all()
        dept_list_data = []
        for i in dept_list:
            dept_list_data.append({
                "id": i.id,
                "name": i.name,
            })
        return jsonify({"departments": dept_list_data})

    if request.method == "POST":
        name=request.json.get("name")
        dept = Department(name=name)
        db.session.add(dept)
        db.session.commit()
        return jsonify({"msg": "Department added successfully"})

@app.route('/department/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def department(id):
    try:
        department = Department.query.filter_by(id=id).first()
        if request.method == "GET":
            return jsonify({"Department": {"name": department.name}})

        if request.method == "DELETE":
            db.session.delete(department)
            db.session.commit()
            return jsonify({"msg": "Department deleted successfully"})
        
        if request.method == "PUT":
            name = request.json.get('name')
            department.name = name
            db.session.commit()
            return jsonify({"msg": "Department updated successfully"})
    except:
        return jsonify({"msg": "Department not found"})


@app.route('/employees', methods=['GET', 'POST'])
def employees():
    emp_list = Employee.query.all()
    emp_list_data = []
    for i in emp_list:
        emp_list_data.append({
            "id": i.id,
            "name": i.name,
            "salary": i.salary,
            "department": i.department.name if i.department else None  # Check if department exists
        })
    if request.method == "GET":
        return jsonify({"employees": emp_list_data})
    
    if request.method == "POST":
        name = request.json.get('name')
        age = request.json.get('age')
        salary = request.json.get('salary')
        department_id = request.json.get('department_id')
        employee = Employee(name=name, age=age, salary=salary, department_id=department_id)
        db.session.add(employee)
        db.session.commit()
        return jsonify({"msg": "Employee added successfully"})


@app.route('/employees/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def employee(id):
    try:
        employee = Employee.query.filter_by(id=id).first()
        if request.method == "GET":
            return jsonify({"Employee": {"id": employee.id, "name": employee.name, "salary": employee.salary, "department": Department.query.filter_by(id=employee.department_id).first().name}})
        if request.method == "PUT":
            name = request.json.get('name')
            age = request.json.get('age')
            salary = request.json.get('salary')
            department_id = request.json.get('department_id')

            employee.name = name
            employee.age = age
            employee.salary = salary
            employee.department_id = department_id
            db.session.commit()
            return jsonify({"msg": "Employee updated successfully"})
        
        if request.method == "DELETE":
            db.session.delete(employee)
            db.session.commit()
            return jsonify({"msg": "Employee deleted successfully"})
    except:
        return jsonify({"msg": "Employee not found"})
    


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5005, debug=True)