from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db, app
from .models import Note
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@views.route('/home', methods=['GET','POST'])
@login_required
def home_page():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('The note is too short!', category='error')
        else:
            with app.app_context():
                new_note = Note(data=note, user=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note is added successfully', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    note_id = note['note_id']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            with app.app_context():
                db.session.delete(note)
                db.session.commit()
                flash("Note has been deleted successfully", category='success')
                return jsonify({})