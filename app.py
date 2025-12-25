from flask import Flask,render_template
app=Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI']= 'sqllite:///Database01.db'

db=SQLAlchemy()
db.init_app(app)
app.app_context.push()





class User(db.Model):
    __table_name__= 'User'
    id = db.column(db.Interger,primary_key=True,autoincrement=True)
    email=db.column(db.String(120),unique=True,nullable=False)
    password_hash=db.column(db.String(120),nullable=False)
    role=db.column(db.string(10),nullable=False)
    patient=db.relationship('Appointemnt',backref='User',lazy=True)
    doctor=db.relationship('Appointemnt',backref='User',lazy=True)


class DoctorProfile(db.Model):
    __table_name__='DoctorProfile'
    id=db.column(db.Integer,primary_key=True)
    user_id=db.column(db.Integer,db.ForeignKey(User.id))
    first_name=db.column(db.String(100),nullable=False)
    last_name=db.column(db.String(100),nullable=False)
    specialization=db.column(db.String(100),nullable=False)
    user=db.relationship('User',backref='doctorprofile',uselist=False)




class PatientProfile(db.Model):
    __table_name__='PatientProfile'
    id=db.column(db.Integer,primary_key=True)
    user_id=db.column(db.Integer,db.ForeignKey(User.id))
    first_name=db.column(db.String(100),nullable=False)
    last_name=db.column(db.String(100),nullable=False)
    dob=db.column(db.Date,nullable=False)
    contact_number=db.column(db.String(20))
    user=db.relationship('User',backref='patientprofile',uselist=False)
    





class Appointment(db.Model):
    __table_name__='Appointment'
    id=db.column(db.Integer,primary_key=True)
    patient_id=db.column(db.Integer,db.ForeginKey(User.id))
    doctor_id=db.column(db.Integer,db.ForeginKey(User.id))
    status=db.column(db.String(100),nullable=False,default='Scheduled')
    reason=db.column(db.Text)


class MedicalRecord(db.Model):
    __table_name__='MedicalRecord'
    id=db.column(db.Integer,primary_key=True)
    appointment_id=db.column(db.Integer,db.ForeginKey(Appointment.id))
    diagnosis=db.column(db.Text,nullable=False)
    treatment_notes=db.column(db.Text)
    created_at=db.column(db.DateTime,default=now())
    appointment=db.relationship('Appointment',backref='mediaclrecord',uselist=False)




@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html')



@app.route("/about")
def about():
    return render_template('about.html')





if __name__ == '__main__':
    app.run(debug=True)