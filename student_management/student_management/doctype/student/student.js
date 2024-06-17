// Copyright (c) 2024, AMan and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Student", {
	onload_post_render(frm) {
       if(frm.doc.joining_date===undefined){

        var currentDate=new Date();
       var year=currentDate.getFullYear();
       var month=currentDate.getMonth()+1;
       var day=currentDate.getDate();
       var joiningDate=year+"-"+ month+"-"+day;
       frm.set_value("joining_date",joiningDate)
       }
       	},

    validate: function(frm) {
        let dateOfBirth = frm.doc.date_of_birth;

        if (dateOfBirth) {
            let dobDate = new Date(dateOfBirth);
            let today = new Date();

            // Ensure the date is parsed correctly
            if (isNaN(dobDate.getTime())) {
                frappe.msgprint(__('Please enter a valid date of birth.'));
                frappe.validated = false;
                return;
            }

            // Check if the date is in the future
            if (dobDate > today) {
                frappe.msgprint(__('Please enter a valid date of birth. You cannot select a future date.'));
                frappe.validated = false;
                return;
            }

           
        }
    }
    ,
    // create_user:function(frm){
    //     frm.save()
    //     .then(() => {
    //         frappe.msgprint(__('Document saved successfully.'));
    //     })
    //     .catch((error) => {
    //         frappe.msgprint({
    //             title: __('Error'),
    //             indicator: 'red',
    //             message: __('There was an error saving the document: ') + error.message
    //         });
    //     });
    // }
    create_user: function(frm) {
        frm.save()
        .then(() => {
        frappe.msgprint(__('Document saved successfully.'));
        
                    // Prepare the user data
                    let user_data = {
                        "doctype": "User",
                        "send_welcome_email": 0,
                        "email": frm.doc.email,
                        "first_name": frm.doc.first_name,
                        "user_type": "Website User"
                    };
        
                    // Create the user
                    frappe.call({
                        method: "frappe.client.insert",
                        args: {
                            doc: user_data
                        },
                        callback: function(response) {
                            if (response.message) {
                                let user = response.message;
        
                                // Generate reset password link
                                frappe.call({
                                    method: "frappe.core.doctype.user.user.reset_password",
                                    args: {
                                        user: user.name
                                    },
                                    callback: function(reset_response) {
                                        if (reset_response.message) {
                                            let update_password_link = reset_response.message;
                                            frappe.msgprint(__('User created successfully. Password reset link: ') + update_password_link);
                                        } else {
                                            frappe.msgprint({
                                                title: __('Error'),
                                                indicator: 'red',
                                                message: __('Failed to generate reset password link.')
                                            });
                                        }
                                    }
                                });
                            } else {
                                frappe.msgprint({
                                    title: __('Error'),
                                    indicator: 'red',
                                    message: __('Failed to create user.')
                                });
                            }
                        }
                    });
                })
                .catch((error) => {
                    frappe.msgprint({
                        title: __('Error'),
                        indicator: 'red',
                        message: __('There was an error saving the document: ') + error.message
                    });
                });
            }
    ,
    address: function(frm) {
        if(frm.doc.address) {
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Address",
                    name: frm.doc.address
                },
                callback: function(r) {
                    if(r.message) {
                      
                        frm.fields_dict['combined_address'].html('<p>' + r.message.address_line1 + '<span>,</span>' + 
                                                                       r.message.address_line2 + '<span>,</span> ' + 
                                                                       r.message.city + '<span>,</span> ' + 
                                                                       r.message.state + ' <span>,</span>' + 
                                                                       r.message.country + ' <span>,</span>' + 
                                                                       r.message.pincode + '</p>');
                    }
                }
            });
        }
    }
});

