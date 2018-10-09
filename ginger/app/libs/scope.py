
class Scope:
    allow_api = []
    allow_mudule = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = set(self.allow_api)

        self.allow_mudule = self.allow_mudule + other.allow_module
        self.allow_mudule = list(set(self.allow_mudule))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self

class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user','v1.user + super_delete_user']
    allow_mudule = ['v1.user']

    def __init__(self):
        # self +UserScope()

       pass

class UserScope(Scope):
    forbidden = ['v1.user+super_get_user','v1.user+super_delete_user']
    allow_api=['v1.user+get_user','v1.user+delete_user']

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope,endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_mudule:
        return True
    else:
        return False
