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
        newTextArea.setAttribute('cols', '50');
        //need the parent element to replaceChild
        const elPariente = add_button.parentElement;
        elPariente.replaceChild(newTextArea, add_button)
    }

    // Event listener for the add-new-note-button button (to add new notes)
    document.querySelector('#add-new-note-button').addEventListener('click', create_text_area);


})

