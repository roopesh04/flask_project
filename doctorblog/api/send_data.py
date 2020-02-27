from flask import Flask,Blueprint,jsonify
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from doctorblog.models import Medicine

data=Blueprint('data',__name__)

#data_of_patient=Api(data)

def return_data(name_of_patient):
    patients=Medicine.query.order_by(Medicine.date.desc())
    a={}
    i=0
    for post in patients:
        if post.patient_name==name_of_patient:
            i=i+1
#            a[i]=[post.author.username,post.medicine,post]
            b={}
            b["doctor_name"]=post.author.username
            b["medicine_name"]=post.medicine
            b["description"]=post.description
            b["allergy_data"]=post.allergy
            b["morning"]=post.morning
            b['afternoon']=post.afternoon
            b['evening']=post.evening
            a[i]=b
        a[0]=i
    return a

@data.route('/get_data/<string:name>',methods=['GET'])
def get_data(name):
    return jsonify(return_data(name))