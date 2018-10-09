from flask import g
from flask.json import jsonify

from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')

# class QiYue:
#     name = "wuqi"
#     age = 18
#
#     def __init__(self):
#         self.gender = 'male'
#
#     def keys(self):
#         return('name','age')
#
#     def __getitem__(self, item):
#         return getattr(self,item)




@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

@api.route('',methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>',methods=['DELETE'])
def super_delete_user(uid):

    pass

@api.route('',methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

@api.route('',methods = ['PUT'])
def update_user():
    return 'update wuqi'



