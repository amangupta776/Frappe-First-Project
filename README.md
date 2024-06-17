# Frappe  Documentation

## Overview
This Frappe application provides a unified API endpoint to handle CRUD operations (Create, Read, Update, Delete) for different doctypes.

## Objective
- Understand the Frappe structure.
- Learn how to create doctype, child doctype, file structure.
- Explore all types of customization and CRUD operations.

## Steps

### 1. Create a DocType named “Student”
With the following fields:
- **First Name**: Data
- **Middle Name**: Data
- **Last Name**: Data
- **Full Name**: Read Only (fetched by concatenating First Name, Middle Name, Last Name)
- **Naming Series**: Select (at least 3 naming series, e.g., STU-YYYY-MM-DATE-0001)
- **Student Email Address**: Data (with validations)
- **Date of Birth**: Date (with validations)
- **Gender**: Select
- **Nationality**: Data
- **Blood Group**: Select
- **Address**: Link (link to Default Address DocType in the CRM Module of ERPNext)
- **HTML Field**: (to show the combined address fetched from the Address DocType)
- **Joining Date**: Date (prefilled with today’s date)
- **Active**: Checkbox (to check if the student is active)

### 2. Create a DocType named "Program"
With the following fields:
- **Program Name**: Data (to store the name of the program)
- **Description**: Text (to provide a description of the program)
- **Start Date**: Date (to store the start date of the program)
- **End Date**: Date (to store the end date of the program)
- **Duration**: Float (to specify the duration of the program in months)
- **Total Credits**: Float (to store the total credits associated with the program)
- **Status**: Select (to indicate the status of the program: Planned, Ongoing, Completed)
- **Instructor**: Link (MultiTable link field to the "Employee" doctype, filtered by Instructor type)
- **Courses**: Table (contains subfield "course" which links to the "Course" doctype)

### 3. Create a DocType named “Course”
With the following fields:
- **Course Name**: Data
- **Course Code**: Data
- **Credits**: Float
- **Academic Year**: Link (to another doctype)
- **Topics**: Table (child table to add topics)

### 4. Create a DocType named "Topics"
With the following fields:
- **Topic Name**: Data
- **Topic Description**: Text

## API Endpoints

### Handle Request
Handles different HTTP methods (GET, POST, PUT, DELETE) on a single URL.

**URL:** `/api/method/handle_request`

**Methods:**
- `GET`: Retrieve records
- `POST`: Create a new record
- `PUT`: Update an existing record
- `DELETE`: Delete an existing record

### GET Request
Retrieve records of a specified doctype.

**Parameters:**
- `doctype` (required): The name of the doctype.
- `name` (optional): The name of a specific record.

**Example Request:**
```bash
curl -X GET 'http://your-site/api/method/handle_request?doctype=YourDoctype'
Example Response:

[
  {
    "name": "record1",
    "field1": "value1",
    "field2": "value2"
  },
  ...
]
POST Request
Create a new record in the specified doctype.

Parameters:

doctype (required): The name of the doctype.
Additional fields as required by the doctype.
Example Request:

curl -X POST 'http://your-site/api/method/handle_request' \
-H 'Content-Type: application/json' \
-d '{"doctype": "YourDoctype", "field1": "value1", "field2": "value2"}'
Example Response:

{
  "name": "new_record_name",
  "field1": "value1",
  "field2": "value2"
}
PUT Request
Update an existing record in the specified doctype.

Parameters:

doctype (required): The name of the doctype.
name (required): The name of the record to update.
Additional fields to update.
Example Request:

curl -X PUT 'http://your-site/api/method/handle_request' \
-H 'Content-Type: application/json' \
-d '{"doctype": "YourDoctype", "name": "record_name", "field1": "new_value1"}'
Example Response:


{
  "name": "record_name",
  "field1": "new_value1",
  "field2": "value2"
}
DELETE Request
Delete an existing record in the specified doctype.

Parameters:

doctype (required): The name of the doctype.
name (required): The name of the record to delete.
Example Request:


curl -X DELETE 'http://your-site/api/method/handle_request' \
-H 'Content-Type: application/json' \
-d '{"doctype": "YourDoctype", "name": "record_name"}'
Example Response:


{
  "message": "Record record_name deleted successfully"
}
Authentication
To use the API, you need to authenticate using API keys or basic authentication.

Generating API Keys
Log in to your Frappe application.
Go to your user profile.
Generate an API key and API secret.
Using API Keys
Pass the API key and secret in the request headers.

Example Request with API Keys:

curl -X GET 'http://your-site/api/method/handle_request?doctype=YourDoctype' \
-H 'Authorization: token api_key:api_secret'
Basic Authentication
Alternatively, you can use basic authentication with your Frappe username and password.

Example Request with Basic Authentication:


curl -X GET 'http://your-site/api/method/handle_request?doctype=YourDoctype' \
-u 'username:password'
Using Postman
Step-by-Step Guide
1. Set Up Your Environment
Open Postman and create a new environment for your Frappe application.
Add environment variables for base_url, api_key, and api_secret.
2. Generating API Keys
To interact with the Frappe API, you need to generate API keys from the Frappe user profile.

Log in to your Frappe application.
Go to your user profile.
Generate an API key and API secret.
3. Making API Requests
Example: GET Request
Set Up Request:

In Postman, create a new GET request.
Set the URL to {{base_url}}/api/method/handle_request?doctype=YourDoctype.
Add Authorization:

Go to the Authorization tab.
Choose API Key as the type.
Set the key to Authorization and the value to token {{api_key}}:{{api_secret}}.
Send Request:

Click Send to make the request.
You should see the response in the Postman response section.
Example: POST Request
Set Up Request:

In Postman, create a new POST request.
Set the URL to {{base_url}}/api/method/handle_request.
Add Authorization:

Go to the Authorization tab.
Choose API Key as the type.
Set the key to Authorization and the value to token {{api_key}}:{{api_secret}}.
Set Body:

Go to the Body tab.
Choose raw and select JSON from the dropdown.
Enter your JSON data, e.g.:
{
  "doctype": "YourDoctype",
  "field1": "value1",
  "field2": "value2"
}
Send Request:

Click Send to make the request.
You should see the response in the Postman response section.
Example: PUT Request
Set Up Request:

In Postman, create a new PUT request.
Set the URL to {{base_url}}/api/method/handle_request.
Add Authorization:

Go to the Authorization tab.
Choose API Key as the type.
Set the key to Authorization and the value to token {{api_key}}:{{api_secret}}.
Set Body:

Go to the Body tab.
Choose raw and select JSON from the dropdown.
Enter your JSON data, e.g.:

{
  "doctype": "YourDoctype",
  "name": "record_name",
  "field1": "new_value1"
}
Send Request:

Click Send to make the request.
You should see the response in the Postman response section.
Example: DELETE Request
Set Up Request:

In Postman, create a new DELETE request.
Set the URL to {{base_url}}/api/method/handle_request.
Add Authorization:

Go to the Authorization tab.
Choose API Key as the type.
Set the key to Authorization and the value to token {{api_key}}:{{api_secret}}.
Set Body:

Go to the Body tab.
Choose raw and select JSON from the dropdown.
Enter your JSON data, e.g.:

{
  "doctype": "YourDoctype",
  "name": "record_name"
}
Send Request:

Click Send to make the request.
You should see the response in the Postman response section.
Error Handling
The API returns appropriate HTTP status codes and error messages in case of failures.

Common Error Responses
400 Bad Request: Missing or invalid parameters.
401 Unauthorized: Authentication failed.
404 Not Found: Resource not found.
500 Internal Server Error: An error occurred on the server.
