frappe.ready(function() {
	// bind events here
	var bookButton = document.querySelector('button[type="submit"]');

	bookButton.addEventListener('click', function(event) {
		var memberName = frappe.web_form.get_value('member_name');
		var childTable = frappe.web_form.get_value('booking_class');

		if (memberName && childTable) {
			var childTableData = [];
			
			childTable.forEach(function(row) {
				FormattedRow = {
					'date': row.date,
					'group_class': row.group_class,
				};
				childTableData.push(FormattedRow);
			});

			// Call the whitelisted function using frappe.call
			frappe.call({
				method: 'gymasy.gym_management.web_form.group_class_booking.group_class_booking.submit_data',
				args: {
					member_name: memberName,
					child_table_data: childTableData
				},
				callback: function(response) {
					// Handle the response or perform any required actions
					console.log(response.message);
				}
			});
		}
		event.preventDefault();
	});
});


// var memberName = frappe.web_form.get_value('member_name');
// var childTableData = frappe.web_form.get_value('child_table');

// if (memberName && childTableData) {
//   // Call the whitelisted function using frappe.call
//   frappe.call({
//     method: 'my_app.my_module.submit_data',
//     args: {
//       member_name: memberName,
//       child_table_data: childTableData
//     },
//     callback: function(response) {
//       // Handle the response or perform any required actions
//       console.log(response.message);
//     }
//   });
// }
