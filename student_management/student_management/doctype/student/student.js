// Copyright (c) 2024, AMan and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Student", {
    //This Function for autofill value of Joing Date
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
       //THis Function For Validate Date Of Joining is not greater than Date of Birth 
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
    //This Function For When Click on Create User Button Then Save The Date
    create_user:function(frm){
        frm.save()
        .then(() => {
            frappe.msgprint(__('Document saved successfully.'));
        })
        .catch((error) => {
            frappe.msgprint({
                title: __('Error'),
                indicator: 'red',
                message: __('There was an error saving the document: ') + error.message
            });
        });
    },
    //This Function For Show Full Address When Select Address
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

