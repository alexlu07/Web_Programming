document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('button').disabled = true;

    // Enable button only if there is text in the input field
    document.querySelector('#username').onkeyup = () => {
        if (document.querySelector('#username').value.length > 0 &&
            document.querySelector('#confirm_password').value.length > 0 &&
            document.querySelector('#password').value.length > 0) {
            document.querySelector('button').disabled = false;
        } else {
            document.querySelector('button').disabled = true;
        }
    };

    document.querySelector('#password').onkeyup = () => {
        if (document.querySelector('#username').value.length > 0 &&
            document.querySelector('#confirm_password').value.length > 0 &&
            document.querySelector('#password').value.length > 0) {
            document.querySelector('button').disabled = false;
        } else {
            document.querySelector('button').disabled = true;
        }
    };

    document.querySelector('#confirm_password').onkeyup = () => {
        if (document.querySelector('#username').value.length > 0 &&
            document.querySelector('#confirm_password').value.length > 0 &&
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
      const confirm_password = document.querySelector("#confirm_password").value;
      document.querySelector('#form').reset();
      request.open('POST', '/new');
      // Callback function for when request completes
      request.onload = () => {
          const success = JSON.parse(request.responseText);
          console.log("after");
          if (success["success"] == false) {
            document.querySelector('#message').innerHTML = success["message"];

          } else {
            window.location.href = "/channels";
          }

      }

      request.onerror = function(e) {
          console.log("request.error called. Error: " + e);
      };
      console.log("before");
      const data = new FormData();
      data.append('username', username);
      data.append('password', password);
      data.append('confirm_password', confirm_password);
      request.send(data);
      return false;
    };
});
