function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        window.location.href = "/";
    });
}

function addToList(event_id) {
    $.ajax({
        type:"GET",
        url:`https://app.ticketmaster.com/discovery/v2/events/${event_id}.json?apikey=zmHIGC4DGRbZkiLCi3kAbhARDALDK36a`,
        async:true,
        dataType: "json",
        success: function(json) {
                    console.log(json);
                 },
        error: function(xhr, status, err) {
                 }
      });
    console.log(e);
}