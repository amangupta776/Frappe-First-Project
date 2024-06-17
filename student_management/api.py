# Importing the frappe module
import frappe
# Importing the _ function from frappe
from frappe import _

# Allowing this function to be accessed via a web request
@frappe.whitelist()
def handle_request():
    """
    Handle different HTTP methods (GET, POST, DELETE, UPDATE) on a single URL.
    """
    # Get the HTTP method from the request
    method = frappe.local.request.method

    # Handle different methods
    if method == "GET":
        return get_items()
    elif method == "POST":
        return create_record()
    elif method == "PUT":
        return update_record()
    elif method == "DELETE":
        return delete_record()
    else:
        # Return an error for unsupported methods
        return {"error": "Invalid request method"}, 405

# Function to handle GET requests
def get_items():
    # Get the doctype from the request
    doctype = frappe.local.form_dict.get('doctype')

    # Get the name from the request
    name = frappe.local.form_dict.get("name")
    if not doctype:
        # Return an error if doctype is not provided
        return {"error": "doctype is required"}, 400

    if name:
        try:
            # Fetch a single document if name is provided
            item = frappe.get_doc(doctype, name)
            return item
        except Exception as e:
            # Return an error if fetching fails
            return {"error": str(e)}, 500

    all_items = []

    try:
        # Fetch all documents if name is not provided
        records = frappe.get_all(doctype, fields=["*"])
        for record in records:
            all_items.append(frappe.get_doc(doctype, record))
        return all_items
    except Exception as e:
        # Return an error if fetching fails
        return {"error": str(e)}, 500

# Function to handle POST requests
def create_record():
    # Get the data from the request
    data = frappe.local.form_dict
    # Get the doctype from the data
    doctype = data.get('doctype')
    if not doctype:
        # Return an error if doctype is not provided
        return {"error": "doctype is required"}, 400

    try:
        # Create a new document with the provided data
        doc = frappe.get_doc({
            "doctype": doctype,
            **data
        })
        # Insert the document into the database
        doc.insert()
        return doc.as_dict()
    except Exception as e:
        # Return an error if creation fails
        return {"error": str(e)}, 500

# Function to handle PUT requests
def update_record():
    # Get the data from the request
    data = frappe.local.form_dict
    # Get the doctype and name from the data
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        # Return an error if doctype or name is not provided
        return {"error": "doctype and name are required"}, 400

    try:
        # Fetch the document to be updated
        doc = frappe.get_doc(doctype, name)
        # Update the document with the new data
        doc.update(data)
        # Save the updated document
        doc.save()
        return doc.as_dict()
    except Exception as e:
        # Return an error if update fails
        return {"error": str(e)}, 500

# Function to handle DELETE requests
def delete_record():
    # Get the data from the request
    data = frappe.local.form_dict
    # Get the doctype and name from the data
    doctype = data.get('doctype')
    name = data.get('name')
    if not doctype or not name:
        # Return an error if doctype or name is not provided
        return {"error": "doctype and name are required"}, 400

    try:
        # Delete the specified document
        frappe.delete_doc(doctype, name)
        return {"message": f"Record {name} deleted successfully"}
    except Exception as e:
        # Return an error if deletion fails
        return {"error": str(e)}, 500
