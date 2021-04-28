$(document).ready(function () {
   var fetchOptions = {
      method: 'GET'
   }

   fetchURL = "/employee/getEmployees/"

   var employeeInfo;

   fetch(fetchURL, fetchOptions)
	.then((data) => {
	   return data.json();
	})
	.then((dataJson) => {
	   insertEmployeeInfo(dataJson);
	})
});

function insertEmployeeInfo(employeeInfo){
   var employeeHtml = "";

   employeeInfo.forEach((employee) => {
      employeeHtml += createEmployeeDiv(employee);
   })

   $("#employee-info").append(employeeHtml);
}

function createEmployeeDiv(employee){
   var html = ""

   html += "<div class='employee'>"
   html += "<h4>Employee Name: " + employee.name + "</h4>"
   html += "<h4>Position: " + employee.position + "</h4>"
   html += "<h4>Salary: " + employee.salary + "</h4>"
   html += "<h4>Email: " + employee.email + "</h4>"
   html += "<h4>Phone: " + employee.phone + "</h4>"
   html += "<hr/>"
   html += "</div>"

   return html
}
