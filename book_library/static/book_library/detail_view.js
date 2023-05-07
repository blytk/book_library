document.addEventListener('DOMContentLoaded', function() {
    
    // This function fetches the add_note URL, sends inside of body: the value of the #new_note_text textarea field (not created yet)(it needs to be created dynamically)
    function new_note() {
        fetch('/add_note', {
            method: 'POST',
            body: JSON.stringify({
                body: document.querySelector('#new_note_text').value
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            document.querySelector('#new_note_text').value = "";
        })
    };

    // I need a function that, is added to add-new-note-button
    // When button is clicked, button is replaced by textarea #new_note_text and a save button
    // When save button is clicked, calls for new_note (that sends the information to the url as json)
    function create_text_area() {
        //get the button
        const add_button = document.querySelector('#add-new-note-button');
        
        //create textarea element and set some attributes
        const newTextArea = document.createElement('textarea');
        newTextArea.setAttribute('rows', '5');
        

        //need the parent element to replaceChild
        const elPariente = add_button.parentElement;
        elPariente.replaceChild(newTextArea, add_button)

        
        row = document.createElement('div')
        row.setAttribute('class', 'row')
        row.setAttribute('id', 'row-with-text-and-buttons')

        col1 = document.createElement('div')
        col1.setAttribute('class', 'col d-grid gap-2')
        save_button = document.createElement('button')
        save_button.setAttribute('class', 'btn btn-outline-success blink')
        save_button.setAttribute('id', 'save-button')
        save_button.innerHTML = "Save"
        col1.appendChild(save_button)

        col2 = document.createElement('div')
        col2.setAttribute('class', 'col d-grid gap-2')
        cancel_button = document.createElement('button')
        cancel_button.setAttribute('class', 'btn btn-outline-danger blink')
        cancel_button.setAttribute('id', 'cancel-button')
        cancel_button.innerHTML = "Cancel"
        col2.appendChild(cancel_button)

        row.appendChild(col1)
        row.appendChild(col2)

        elPariente.appendChild(row)
        /*
        save_button = document.createElement('button')
        save_button.setAttribute('class', 'btn btn-sm btn-light')
        save_button.innerHTML = "Save"
        newTextArea.after(save_button)
        */

        // Event Listeners for Save and Cancel button
       document.querySelector('#save-button').addEventListener('click', function() {
        console.log('save-button clicked')
        if (newTextArea.value !== "") {
            save();
        }
        

       })
       document.querySelector('#cancel-button').addEventListener('click', function() {
        cancel();
        play_erase();
       })


       function save() {
        fetch(`/add_note/${current_book_id}`, {
            method: 'POST',
            body: JSON.stringify({
                note_text: newTextArea.value
            })
        }).then(() => {
            window.location.reload();
        })
        
       }


       function cancel() {
        // window.location.reload(); //This works but sucks as a solution and it's bad for the user as it goes back to the beginning, not good if you have many notes
        // I have been testing a bit and it's very difficult for me at the time, I'm going to revisit this one when I feel a bit more comfortable and other stuff
        // that it's more important has been taken care of
        theDiv = document.querySelector('#div-to-replace')
        newAddButton = document.createElement('button')
        newAddButton.setAttribute('class', 'btn btn-outline-light')
        newAddButton.setAttribute('id', 'add-new-note-button')
        newAddButton.innerHTML = "Add new note +"

        document.querySelector('#row-with-text-and-buttons').remove()
        theDiv.replaceChild(newAddButton, newTextArea)
        document.querySelector('#add-new-note-button').addEventListener('click', create_text_area);
        document.querySelector('#add-new-note-button').addEventListener('click', play_write);
       }
       newTextArea.focus();
       document.querySelector('#div-to-replace').scrollIntoView({ behavior: 'smooth', block: 'end' });
    }

    
    // Event listener for the add-new-note-button button (to add new notes)
    document.querySelector('#add-new-note-button').addEventListener('click', create_text_area);
    document.querySelector('#add-new-note-button').addEventListener('click', play_write);

    // Add event listener for the remove note button (to remove each note)
    all_remove_buttons = document.querySelectorAll('.remove-note-button')
    
    all_remove_buttons.forEach(function(current_remove_button) {
        current_remove_button.addEventListener('click', function() {
            fetch(`/remove_note/${current_remove_button.id}`, {
                method: 'POST',
            })
            .then(() => {
                window.location.reload();
            })
        })
    })

    let allButtons = document.querySelectorAll('button')
    allButtons.forEach(_button => {
        _button.addEventListener('mouseover', () => { 
            _button.classList.add('blink');
        })
        _button.addEventListener('mouseout', () => { 
            _button.classList.remove('blink');
        })  
    });

    // Download button should allow user to download all notes in a formatted way (.txt for starters)
    // document.querySelector('#download-button').addEventListener('click', download_notes)

})

function play_write() {
    var audio = new Audio('/static/book_library/sounds/type-writer.mp3')
    audio.play();
};

function play_erase() {
    var audio = new Audio('/static/book_library/sounds/erase.mp3')
    audio.play();
}

/*
function download() {
    pass
}
*/