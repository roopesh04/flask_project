#blog_post/views.py

from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import current_user,login_required
from doctorblog import db
from doctorblog.models import Medicine
from doctorblog.blog_posts.forms import postform

posts=Blueprint('posts',__name__)

@posts.route("/create_post",methods=['GET','POST'])
@login_required
def create_post():
    form =postform()

    if form.validate_on_submit():
        medicine=Medicine(patient_name=form.patient_name.data,
                                medicine=form.medicine.data,
                                user_id=current_user.id,
                                description=form.description.data,
                                allergy=form.allergy.data,
                                morning=form.morning.data,
                                afternoon=form.afternoon.data,
                                evening=form.evening.data
                                )
        db.session.add(medicine)
        db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('post.html',form=form)
   
