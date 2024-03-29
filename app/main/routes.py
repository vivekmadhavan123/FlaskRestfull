from flask_restful import Resource


class Main(Resource):
    response = {
        "status" : 200,
        "message" : "Ok",
        "data" : None
    }


    def get(self):
        response = self.response.copy()
        response["message"] = "GET"
        return response, response["status"]
    
    def post(self):
        response = self.response.copy()
        response["message"] = "POST"
        response["status"] = 201
        return response, response["status"]
    
    def put(self, pk):
        response = self.response.copy()
        response["message"] = "PUT"
        return response, response["status"]
    
    def delete(self, pk):
        response = self.response.copy()
        response["message"] = "DELETE"
        return response, response["status"]
    
    def patch(self, pk):
        response = self.response.copy()
        response["message"] = "PATCH"
        return response, response["status"]
