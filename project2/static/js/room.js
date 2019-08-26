
document.addEventListener("DOMContentLoaded", () => {

    function submitOnEnter(event){
        if(event.which === 13 && !event.shiftKey ){
            event.target.form.dispatchEvent(new Event("submit", {cancelable: true}));
            event.preventDefault(); // Prevents the addition of a new line in the text field (not needed in a lot of cases)
        }
    }

    document.getElementById("input_message").addEventListener("keypress", submitOnEnter);

    function createDiv(username, message) {
        let div_container = document.createElement("div");
        let div_username = document.createElement("div");
        let div_message = document.createElement("div");
        div_container.className = "div_container";
        div_username.className = "div_username";
        div_message.className = "div_message";
        div_container.append(div_username);
        div_container.append(div_message);
        div_username.append(username + ": ");
        div_message.append(message);
        document.querySelector("#messages").append(div_container);
    }

    function updateScroll(){
        var element = document.getElementById("messages");
        if(element.scrollHeight - element.scrollTop <= 1220) {
            element.scrollTop = element.scrollHeight;
        }
    }

    var element = document.getElementById("messages");
    element.scrollTop = element.scrollHeight;


    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    //console.log("1");
    socket.on('connect' , () => {

        socket.emit("join")
        socket.emit("get_all_messages");
        document.querySelector("form").onsubmit = () => {
            const message = $.trim($("textarea").val());
            $("textarea").val("");
            socket.emit('return_message', {'message': message});
        };


    });



    socket.on("append_message", user_message => {
        const username = user_message["username"];
        const message = user_message["message"];
        createDiv(username, message);
        updateScroll();

    });

    socket.on("all_messages", data => {
        document.querySelector("#messages").innerHTML = "";
        users = data.users;
        messages = data.messages;
        for(var x = 0; x < messages.length; x++) {
            let username = users[x];
            let message = messages[x];
            createDiv(username, message);


            //console.log(document.cookie)
        }
    });

    socket.on("update_users", data => {
        console.log("hi");
        username = data["username"];
        users = data["users"];
        active_users = data["active_users"];
        console.log(users);
        for(var x = 0; x < users.length; x++) {
            if(document.querySelector("#userlist").querySelectorAll("p").length < users.length) {
                let p = document.createElement("p");
                p.innerHTML = users[x]
                document.querySelector("#userlist").append(p)
            }
        }
        document.querySelector("#userlist").querySelectorAll("p").forEach(element => {
            if(active_users.includes(element.innerHTML)) {
                element.className = "connected";
            } else {
                element.className = "disconnected";
            }
        });

        function get_connection_length(a) {
            return a.className.length;
        }

        function sort_by_connection(a, b) {
            return get_connection_length(a) - get_connection_length(b);
        }

        $userlist = $("div#userlist");
        var element_list = $userlist.children();
        element_list.sort(sort_by_connection);
        $userlist.html(element_list);
    });


    window.onbeforeunload = () => {
        console.log("left");
        socket.emit("leave");
    };

    return false;

});
