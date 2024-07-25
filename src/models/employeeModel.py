from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = 'employee'
   
    
    id = db.Column(db.Integer, primary_key= True)
    cpf = db.Column(db.String(11), unique = True)
    name = db.Column(db.String(100))
    position = db.Column(db.String(20))
    
    def __init__(self, cpf, name, position):
        self.cpf = cpf
        self.name = name
        self.position = position
    def __repr__(self):
        return f"{self.id}:{self.name}-{self.position}"
