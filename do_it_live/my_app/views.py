from flask import Blueprint, flash, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import requests

views = Blueprint('views', __name__)

url = "https://app.ticketmaster.com/discovery/v2/"
api_key = "Bp0o0LwAEIR2zOwa7h1eoT7BnylC1kst"


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    locales = {}
    events = {}

    if request.method == 'POST':
        note = request.form.get('note')
        keyword = request.form.get("keyword")

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
                f"{url}events.json?apikey={api_key}&keyword={keyword}&locale=*&size=20&city={note}").json()
            events = resp['_embedded']['events']
            for event in events:
                locales = event['_embedded']['venues']

    return render_template("home.html", user=current_user, items=events, locations=locales)


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
