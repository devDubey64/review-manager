PROJECT : review_manager
APP : review_manager_app
Author : Anubhav Dubey

Python version : 3.11.5
Django version : 4.2.5

Run the application : 

Navigate to the project folder and run command ~~~py manage.py runserver~~~
Hit URL : http://localhost:8000/api/ and check to see no errors.

APIs : 

GET /api/tags/ - returns all existing tags in order of id - ascending order
GET /api/tags/<id>/ - returns tag with given id
POST /api/tags/ - creates a new tag with given name
	Request Payload : 
		{
    		"name": string
		}

PUT /api/tags/<id>/ - updates the tag with given id
	Request Payload : 
		{
    		"name": string
		}

DELETE /api/tags/<id>/ - removes the tag with given id


GET /api/reviews/ - returns all existing reviews in order of updated_at - descending order
GET /api/reviews/<review_id>/ - returns review with given review_id
POST /api/reviews/ - creates a new review with given data
	Request Payload :
		{
		    "text": string,
		    "author": string,
		    "tags": [
		    	...
		    	string  --> should be an existing tag name. else it is ignored.
		    	...
		    ]
		}


PUT /api/reviews/<review-id>/ - updates the review with given id
	Request Payload :
		{
		    "text": string,
		    "author": string,
		    "tags": [
		    	...
		    	string  --> should be existing tag name. else error is displayed.
		    	...
		    ]
		}

PATCH /api/reviews/<review-id>/ - updates the review with given id
	Request Payload : // fields are optional.
		{
		    "text": string,
		    "author": string,
		    "tags": [
		    	...
		    	string  --> should be existing tag name. else error is displayed.
		    	...
		    ]
		}

DELETE /api/reviews/<review-id>/ - removes the review with given id

POST /api/add-remove-tag - adds or removes list of given tags to the review
	Request Payload : 
	{
	    "review_id" : integer, -- valid review_id
	    "tag_names" : "tags": [
			    	...
			    	string  --> (non existent / unmapped (for remove) tags will be ignored)
			    	...
			    ]
	    "action" : string (add / remove based on required action, case insensitive)
	}