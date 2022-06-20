from flask import Flask
from flask_restful import Api

from resources.recipe import RecipeListResource
from resources.recipe_info import RecipeResource
from resources.recipe_publish import RecipePublishResource
from resources.user import UserLoginResource, UserRegisterResource

app = Flask(__name__)

api = Api(app)

# 경로와 리소시(API 코드)를 연결한다.
api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')
api.add_resource(UserRegisterResource, '/users/register')
api.add_resource(UserLoginResource, '/users/login')

if __name__ == '__main__' :
    app.run()


### 단위테스트 (unit test)
# API 함수 만들고
# 포스트맨으로 실행해서 테스트하고
# DB에 정확히 반영되었는지 MySQL Workbench로 확인하면서 개발