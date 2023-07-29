frappe.call(
    {
        method: "frappe.client.get_list",
        args: {
            doctype: "Gymasy Member",
        },
    })
    .then((r) => {
    console.log(r.message);
});