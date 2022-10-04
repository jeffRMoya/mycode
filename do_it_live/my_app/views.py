from flask import Blueprint, flash, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import requests

views = Blueprint('views', __name__)
kitsu_url = "https://kitsu.io/api/edge"
headers = {"Accept": "application/vnd.api+json",
           "Content-Type": "application/vnd.api+json"}


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        keyword = request.form["keyword"]

        if note:
            if len(note) < 1:
                flash("Note is too short!", category='error')
            else:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='success')
        if keyword:
            resp = requests.get(
                kitsu_url + "/anime?filter[categories]=" + keyword, headers=headers)
            print(type(resp))

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
