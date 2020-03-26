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
            medicines=post.medicine
            list_of_medicines=medicines.split(',')
            c={}
            time=post.timing
            list_of_timing=time.split(',')
            d={}
            for k in range(0,len(list_of_medicines)):
                c[k]=list_of_medicines[k]
            for k in range(0,len(list_of_timing)):
                d[k]=list_of_timing[k]
            i=i+1
#            a[i]=[post.author.username,post.medicine,post]
            b={}
            b["doctor_name"]=post.author.username
            b["medicine_name"]=c
            b["number_of_medicines"]=len(list_of_medicines)
            b["description"]=post.description
            b["allergy_data"]=post.allergy
            b["timing"]=d
            a[i]=b
        a[0]=i
    return a

@data.route('/get_data/<string:name>/<string:name2>',methods=['GET'])
def get_data(name,name2):
    return jsonify(return_data(name))