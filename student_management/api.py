import frappe
from frappe import _

@frappe.whitelist()
def handle_request():
    """
    Handle different HTTP methods (GET, POST, DELETE, UPDATE) on a single URL.
    """
    method = frappe.local.request.method

    if method == "GET":
        return get_items()
    elif method == "POST":
        return create_record()
    elif method == "PUT":
        return update_record()
    elif method == "DELETE":
        return delete_record()
    else:
        return {"error": "Invalid request method"}, 405

# def get_tasks():
#     doctype = frappe.local.form_dict.get('doctype')
#     if not doctype:
#         return {"error": "doctype is required"}, 400

#     try:
#         records = frappe.get_all(doctype, fields=["*"])
#         return records
#     except Exception as e:
#         return {"error": str(e)}, 500
def get_items():
    doctype = frappe.local.form_dict.get('doctype')
    name = frappe.local.form_dict.get("name")
    if not doctype:
        return {"error": "doctype is required"}, 400

    if(name):
        try:
            item = frappe.get_doc(doctype, name)
            return item
        except Exception as e:
            return {"error": str(e)}, 500
        
    all_items=[]
   
    try:
        records = frappe.get_all(doctype, fields=["*"])
        for record in records:
            all_items.append(frappe.get_doc(doctype,record))
        return all_items
    except Exception as e:
        return {"error": str(e)}, 500

def create_record():
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    if not doctype:
        return {"error": "doctype is required"}, 400

    try:
        doc = frappe.get_doc({
            "doctype": doctype,
            **data
        })
        doc.insert()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500

def update_record():
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        return {"error": "doctype and name are required"}, 400

    try:
        doc = frappe.get_doc(doctype, name)
        doc.update(data)
        doc.save()
        return doc.as_dict()
    except Exception as e:
        return {"error": str(e)}, 500

def delete_record():
    data = frappe.local.form_dict
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        return {"error": "doctype and name are required"}, 400

    try:
        frappe.delete_doc(doctype, name)
        return {"message": f"Record {name} deleted successfully"}
    except Exception as e:
        return {"error": str(e)}, 500
