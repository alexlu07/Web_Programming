document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit').disabled = true;

    // Enable button only if there is text in the input field
    document.querySelector('#search').onkeyup = () => {
        if (document.querySelector('#search').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
    };

    document.querySelector('#enter').onsubmit = () => {
        // Initialize new request
        const request = new XMLHttpRequest();
        const channel = document.querySelector("select").value;

        request.open('POST', '/join');
        // Callback function for when request completes
        request.onload = () => {
          console.log("hi");
        };


        request.onerror = function(e) {
            console.log("request.error called. Error: " + e);
        };

        console.log(channel);
        const data = new FormData();
        data.append('channel', channel);
        request.send(data);
        return false;
    };

    document.querySelector('#join').onsubmit = () => {
        // Initialize new request
        console.log("1");
        const request = new XMLHttpRequest();
        const search = document.querySelector("#search").value;

        request.open('POST', '/join');
        // Callback function for when request completes
        request.onload = () => {
          const data = JSON.parse(request.responseText);
          const array = data.results;

          if(array.length > 0) {
              const op = document.createElement('option');

              for(var i = 0; i < array.length; i++) {
                  document.querySelector("#new_channel").append(op);
                  op.outerHTML = "<option value = " + array[i] + ">" + array[i] + "</option>";

              }

              document.querySelector("#new_channel").hidden = false;
              document.querySelector("#submit_new_channel").hidden = false;
              console.log(op.value);
          }

        };

        request.onerror = function(e) {
            console.log("request.error called. Error: " + e);
        };

        const data = new FormData();
        data.append('search', search);
        request.send(data);
        return false;
    };

    document.querySelector('#channels').onsubmit = () => {
        // Initialize new request
        console.log("hi");
        const request = new XMLHttpRequest();
        const new_channel = document.querySelector('#new_channel').value;

        request.open('POST', '/join');

        request.onload = () => {
            console.log("hi");

        };

        request.onerror = function(e) {
            console.log("request.error called. Error: " + e);
        };

        const data = new FormData();
        data.append('new_channel', new_channel);
        request.send(data);
        return false;
    };
});
