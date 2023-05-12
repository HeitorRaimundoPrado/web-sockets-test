$(document).ready(function() {
  namespace = '/message';
  var socket = io(namespace)
  socket.emit('join', {'user_id': user_id, 'room': room_id})
  socket.on('connect', function() {
    socket.emit('connected', {data: 'connected to the server'})
    // alert('connected')
  });
  socket.on('msg', function(msg) {
    var msgDiv = document.querySelector('#messages')
    msgDiv.insertAdjacentHTML('beforeend', '<p>' + msg.data + '</p>')

  })
  
  var msgForm = document.getElementById('sendmsg');
  msgForm.addEventListener("submit", (e) =>  {
    e.preventDefault()
    socket.emit('message', {msg: $('#imsginput').val(), room: room_id});
    // alert('test')
    return false;
  })
})
