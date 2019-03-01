#coding:utf-8
class const:

    class ConstError(TypeError):pass


    def __setattr__(self, name, value) :
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value

const=const()
const.BASE_URL='http://dingtalkjxc-test.ikcrm.com/'
const.SIGN_IN_BASE_URL='http://dingtalkjxc-test.ikcrm.com/users/sign_in?show_all_version=1'


