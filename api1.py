from flask import Flask,jsonify, request

app=Flask(__name__)

@app.route('/',methods=['post'])
def hello():
	data=request.get_json()
	_id=data['_id']
	name=data['name']
	age=data['age']
	res=int(_id)+int(age)
	return (jsonify(res,name))
	
@app.route('/')
def details():
	return("hello")
	
app.run()	

