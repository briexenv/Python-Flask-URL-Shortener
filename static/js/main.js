var input = document.querySelector("#url");

input.addEventListener("keyup", function(event) {
  if(event.keyCode === 13) {
    var xhr = new XMLHttpRequest();
    var route = randomRoute(4);
    xhr.open("POST", "/short", true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onload = function () {
      var message = JSON.parse(xhr.responseText);
      var result = document.querySelector(".result");
      if (message.status === "OK") {
        result.innerHTML = '<span class="result-success">success : </span>' + "http://flaskmicro.herokuapp.com/" + route;
      } else {
        result.innerHTML = '<span class="result-error">error : </span>please check your input!';
      }
    };
    xhr.send('submit&key=' + route + '&url=' + input.value);
    
    var history = document.querySelector(".history");
    var span = document.createElement("SPAN");
    var t = document.createTextNode("[root@localhost]~>" + input.value);
    span.className = "text";
    span.appendChild(t);
    history.appendChild(span);
    input.value = "";
    
    var bash = document.querySelector(".bash");
    bash.scrollTop = bash.scrollHeight;
    
  }
})

function randomRoute(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * 
 charactersLength));
   }
   return result;
}