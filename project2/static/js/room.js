
document.addEventListener("DOMContentLoaded", () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    //console.log("1");
    socket.on('connect' , () => {
        socket.emit("join")
        socket.emit("get_all_messages");
        document.querySelector("form").onsubmit = () => {
            const message = document.querySelector("#input_message").value;
            socket.emit('return_message', {'message': message});

        };

        socket.on('disconnect' , () => {
            socket.emit("leave");
        });
    });

    socket.on('disconnect' , () => {
        socket.emit("leave");
    });

    socket.on("append_message", user_message => {
        console.log("4");
        const p = document.createElement("p");
        p.innerHTML = `${user_message["username"]}: ${user_message["message"]}`;
        document.querySelector("#messages").append(p);

        //console.log(document.cookie)
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

            //console.log(document.cookie)
        }
    });

    socket.on("joined_channel", data => {
        document.querySelector("#messages").append(data);
    });

    socket.on("left_channel", data => {
      document.querySelector("#messages").append(data);
    });


    return false;

});
