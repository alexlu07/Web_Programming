document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('button').disabled = true;

    // Enable button only if there is text in the input field
    document.querySelector('#username').onkeyup = () => {
        if (document.querySelector('#username').value.length > 0 &&
            document.querySelector('#password').value.length > 0) {
            document.querySelector('button').disabled = false;
        } else {
            document.querySelector('button').disabled = true;
        }
    };

    document.querySelector('#password').onkeyup = () => {
        if (document.querySelector('#username').value.length > 0 &&
            document.querySelector('#password').value.length > 0) {
            document.querySelector('button').disabled = false;
        } else {
            document.querySelector('button').disabled = true;
        }
    };


    document.querySelector('#form').onsubmit = () => {
        document.querySelector('button').disabled = true;
        // Initialize new request
        const request = new XMLHttpRequest();
        const username = document.querySelector("#username").value;
        const password = document.querySelector("#password").value;
        document.querySelector('#form').reset();
        request.open('POST', '/login');
        // Callback function for when request completes
        request.onload = () => {
            const users = JSON.parse(request.responseText);
            console.log(users);
            console.log(users["users"]);
               if (users["success"] == false) {
                  document.querySelector("#message").innerHTML = "Username and/or password is incorrect";
                  console.log("hii");
               }
               else {
                 window.location.replace("http://192.168.86.35:5000/channels");
               }
            }


        request.onerror = function(e) {
            console.log("request.error called. Error: " + e);
        };
        const data = new FormData();
        data.append('username', username);
        data.append('password', password);
        request.send(data);
        return false;
      };
});
