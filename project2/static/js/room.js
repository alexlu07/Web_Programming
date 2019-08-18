document.addEventListener("DOMContentLoaded", () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    //console.log("1");
    socket.on('connect' , () => {
      socket.emit("get_all_messages");
      //console.log("2");
      document.querySelector("form").onsubmit = () => {
          //console.log("3");
          const message = document.querySelector("#input_message").value;
          socket.emit('return_message', {'message': message});

      };
    });

    socket.on("append_message", user_message => {
        console.log("4");
        const p = document.createElement("p");
        p.innerHTML = `${user_message["username"]}: ${user_message["message"]}`;
        document.querySelector("#messages").append(p);
    });

    socket.on("all_messages", data => {
        document.querySelector("#messages").innerHTML = "";
        console.log(messages);
        users = data.users;
        messages = data.messages;
        for(var x = 0; x < messages.length; x++) {
            console.log(x);
            let username = users[x];
            let message = messages[x];
            const p = document.createElement("p");
            p.innerHTML = `${username}: ${message}`;
            document.querySelector("#messages").append(p);

        }
        console.log("5");
    });
    //console.log("6");
    return false;

});
