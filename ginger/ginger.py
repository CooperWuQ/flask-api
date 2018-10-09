from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()

@app.errorhandler(Exception)
def framework_error(e):
    # flask 1.0
    # 0.12
    # APIException
    # HTTPException
    # Exception
    if isinstance(e,APIException):
        return e
    if isinstance(e,HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg,code,error_code)
    else:
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e
        return ServerError()


# @app.route('/v1/user/get')
# def get_user():
#     return ' I am wuyue'
#
# @app.route('/v1/book/get')
# def get_book():
#     return 'get book'


if __name__ =='__main__':
    app.run(debug=False)