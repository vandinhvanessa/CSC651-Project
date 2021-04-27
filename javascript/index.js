$(document).ready(function () {
   var fetchOptions = {
      method: 'GET'
   }

   fetchURL = "/employee/getEmployees/"

   fetch(fetchURL, fetchOptions)
	.then((data) => {
	   return data.json();
	})
	.then((dataJson) => {
	   console.log(dataJson)
	})
});
