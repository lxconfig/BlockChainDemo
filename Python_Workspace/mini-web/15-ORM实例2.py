class ModelMetaclass(type):
    '''定义一个元类'''
    # name=User, bases=()表示User类没有父类, attrs={'uid': ('uid', 'int unsigned')...}表示User类的类属性
    def __new__(cls, name, bases, attrs):
        # print(attrs)
        mappings = dict()
        for k, v in attrs.items():
            # 过滤掉不是元组的类属性
            if isinstance(v, tuple):
                print("Found mapping: %s ==> %s" % (k, v))
                # mappings = {'uid': ('uid', 'int unsigned').....}
                mappings[k] = v
        
        # 从attrs中删除掉这些键 uid/name/email/password
        for k in mappings.keys():
            attrs.pop(k)
        
        # 新建两个类属性 __mappings__和__table__
        # 分别用于 保存字典 和 设置数据表的名字
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        # 创建类对象，即创建User类的类对象
        return type.__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMetaclass):
    '''定义父类，将可重用的部分放到父类中'''
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            # 给实例对象设置实例属性(再调用__init__前，先调用了__new__方法，即实例对象已经存在)
            # 格式是: uid=123, name='lx'...
            setattr(self, name, value)
    
    def save(self):
        # fields用于保存字段名  ['uid', 'name', 'email', 'password']
        # args用于保存字段名对应的值  [123, 'lx', 'lx@163.com', '12345']
        fields, args = [], []
        # 再实例属性中找不到__mappings__，就回去类属性中找
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))
        
        # 输出时，字符没有双引号
        # sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        args_temp = list()
        for temp in args:
            if isinstance(temp, int):
                # 如果是数字
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        # ','.join(x): 将x中的每个值取出，再去掉双引号，添加,  返回一个新的字符串
        # x必须是一个可迭代的对象, 如果是列表，则每个元素都要是字符
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print("SQL: %s" % sql)


# 在创建类a时，遇到metaclass=xxx，就表示用xxx类来生成这个类a
class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(30)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')

    # 经过元类创建类对象之后，此类对象至少包含两个类属性： __mappings__  __table__
    # 而上面的uid...将不存在与类中，而是存在与 mappings 这个字典中
    '''
    __mappings__ = {
        'uid': ('uid', 'int unsigned'),
        'name': ('username', 'varchar(30)'),
        'email': ('email', 'varchar(30)'),
        'password': ('password', 'varchar(30)')
    }
    __table__ = 'User'
    '''


def main():
    '''
        ORM框架:不用写SQL语句，也能操作数据表(即Django中的模型类)
    '''
    u = User(uid=123, name='lx', email='lx@163.com', password='12345')
    u.save()


if __name__ == "__main__":
    main()