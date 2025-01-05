*** A RESTful API implementing JWT Authentication and Role-Based Access Control (RBAC). Built with FastAPI and MongoDB, this API supports user management and role-based access to resources.
* 
* Features
* JWT Authentication: Secure user login with tokens.
* RBAC:
* admin: Full access (CRUD).
* user: Read-only access.
* MongoDB Integration: Managed with MongoEngine.
* Setup
* Prerequisites
* Python 3.9+
* MongoDB cluster (e.g., MongoDB Atlas)
* Steps
* Clone Repository:
* 
* git clone https://github.com/Manishsingh89716/Backend_Engineer_Task
* cd CodingSphere_Backend_Task
* Install Dependencies:
* pip install -r requirements.txt
* 
* Configure MongoDB: Update connection string in app/__init__.py:
* connect(host="mongodb+srv://mongoDBusername:mongoDBpassword@cluster0.qridz.mongodb.net/mongoDBdatabase?retryWrites=true&w=majority&appName=Cluster0")
* Run the API:
*
* uvicorn app.main:app --reload
* API Endpoints
* User Registration:
* POST /users/register
*
* { "username": "admin_user", "password": "secure123", "role": "admin" }
* User Login:
* POST /users/login
*
* { "username": "admin_user", "password": "secure123" }
* Get Projects (All Users):
* GET /projects
* Header:
* Authorization: Bearer <jwt_token>
* 
* Create Project (Admins Only):
* POST /projects
* Header:
* Authorization: Bearer <jwt_token>
* Body:
*
* { "name": "Project Alpha", "description": "First project" }**
