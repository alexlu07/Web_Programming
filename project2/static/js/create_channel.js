document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit').disabled = true;

    // Enable button only if there is text in the input field
    document.querySelector('#input_channel_name').onkeyup = () => {
        if (document.querySelector('#input_channel_name').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
    };
});
