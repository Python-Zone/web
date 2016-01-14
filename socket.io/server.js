/**
 * Created by yijingping on 16/1/13.
 */
var server = require('http').createServer();
var io = require('socket.io')(server);

var users = {};
io.on('connection', function(socket){
  socket.on('setUserId', function (userId) {
    console.log('userId:', userId);
    users[parseInt(userId)]=socket;
  });
  socket.on('send notification', function (userId) {
     console.log('userId:', userId, ' have a new message');
     users[parseInt(userId)].emit('notification', "you have a new message");
  });
  socket.on('disconnect', function(){});
});
server.listen(3000);