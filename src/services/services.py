from config.database import mongo
from flask import request



def create_user():
	data = request.get_json()
	title = data.get('title', None)
	description = data.get('description', None)
	if title:
		response = mongo.db.users.insert_one({
			'title': title,
			'description': description,
			'donde': False
			})

		result = {
		'id': str(response.inserted_id),
		'title': title,
		'description': description,
		'done': False
		}
		return result
	else:
		return 'Invalid payload', 400




