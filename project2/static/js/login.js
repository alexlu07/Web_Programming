console.log("0");
document.addEventListener('DOMContentLoaded', () => {
    console.log("1");
    document.querySelector('#form').onsubmit = () => {
      console.log("2");
      // Initialize new request
      const request = new XMLHttpRequest();
      const username = document.querySelector("#exampleInputEmail1").value;
      const password = document.querySelector("#exampleInputPassword1").value;
      console.log(username);
      console.log(password);
      request.open('POST', '/login');
      console.log("3");
      // Callback function for when request completes
      request.onload = () => {
          console.log("4");
          const users = JSON.parse(request.responseText);
          document.querySelector("#message").innerHTML = "Username and/or password is incorrect";
          if (users[name].indexOf(username) >= 0) {
            document.querySelector("#message").innerHTML = "Username and/or password is incorrect";
          }
      }

      console.log("6");

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
