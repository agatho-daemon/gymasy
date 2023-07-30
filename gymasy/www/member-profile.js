frappe
    .call({
        method: "frappe.client.get_list",
        args: {
            doctype: "Gymasy Member",
        },
    })
    .then((response) => {
        console.log(response);
    });
