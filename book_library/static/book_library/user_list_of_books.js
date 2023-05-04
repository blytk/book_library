document.addEventListener('DOMContentLoaded', function() {
    // Add functionality to all Remove buttons (that will remove the book from the reading, read or wish list for that user (request.user))
    removeButtons = document.querySelectorAll('.remove-button')

    removeButtons.forEach(function(removeButton) {
        removeButton.addEventListener('click', function() {             
            fetch(`/remove_from_list/${removeButton.id}/${what_list}`, {
                method: 'POST'
            }).then(() => {
                window.location.reload();
            })
        })
    })
})