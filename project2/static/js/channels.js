document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit').disabled = true;

    // Enable button only if there is text in the input field
    document.querySelector('#search').onkeyup = () => {
        if (document.querySelector('#search_input').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
    };

    document.querySelector('#search').onsubmit = () => {
        // Initialize new request
        console.log("1");
        const request = new XMLHttpRequest();
        const search = document.querySelector("#search_input").value;

        request.open('POST', '/search');
        // Callback function for when request completes
        request.onload = () => {
          const data = JSON.parse(request.responseText);
          const array = data.results;

          if(array.length > 0) {
              document.querySelector("#new_channel").outerHTML = "<select id = 'new_channel' name = 'channel'></select>"
              const op = document.createElement('option');

              for(var i = 0; i < array.length; i++) {
                  document.querySelector("#new_channel").append(op);
                  op.outerHTML = "<option value = " + array[i] + ">" + array[i] + "</option>";

              }

              document.querySelector("#new_channel").hidden = false;
              document.querySelector("#submit_new_channel").hidden = false;
              console.log(op.value);
          } else {
              document.querySelector("#new_channel").outerHTML = "<h3 id = 'new_channel'>No search results found</h3>";
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

});
