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
    msgDiv.insertAdjacentHTML('beforeend', '<p class="' + cls + '"/>' + msg.data + '</p>')
    // alert('getting callback')

  })

  var msgForm = document.getElementById('sendmsg');
  msgForm.addEventListener("submit", (e) =>  {
    e.preventDefault()
    socket.emit('message', {msg: $('#imsginput').val(), room: room_id});
    // alert('test')
    textInput = document.getElementById('imsginput')
    textInput.value = '';
    return false;
  }) 

})
