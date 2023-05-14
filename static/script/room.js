$(document).ready(function() {
  // namespace = '/message';
  var socket = io('/')
  socket.emit('join', {'user_id': user_id, 'room': room_id})
  // socket.on('connect', function() {
  //   socket.emit('connected', {data: 'connected to the server'})
  //   // alert('connected')
  // });
  socket.on('msg', function(msg) {
    var msgDiv = document.querySelector('#messages')
    var cls = 'this-user';
    if (msg.user_id === user_id) {
      cls = 'this-user';
    } else {
      cls = 'other-user';
    }
    msgDiv.insertAdjacentHTML('beforeend', '<div class="msg-wrapper"><p class="msg ' + cls + '"/>' + msg.data + '</p></div>')
    // alert('getting callback')
    $("#messages").scrollTop(function () {return this.scrollHeight;});

  })

  var msgForm = document.getElementById('sendmsg');
  msgForm.addEventListener("submit", (e) =>  {
    e.preventDefault()
    socket.emit('message', {msg: $('#imsginput').val(), room: room_id});
    // alert('test')
    textInput = document.getElementById('imsginput')
    textInput.value = '';
    $("#messages").scrollTop(function () {return this.scrollHeight;});
    return false;
  }) 

})
