// Get a reference to the database service
var database = firebase.database();
var bus_details=database.ref('bus_details');
var ref = firebase.database().ref();

ref.on("value", function(snapshot) {
   console.log(snapshot.val());
}, function (error) {
   console.log("Error: " + error.code);
});