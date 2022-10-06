function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        window.location.href = "/";
    });
}

function addToList(eventId) {
    fetch('/add-to-list', {
        method: 'POST',
        body: JSON.stringify({eventId: eventId})
    }).then((_res) => {
        console.log(_res);
    });
}