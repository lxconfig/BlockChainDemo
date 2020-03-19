class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 要把Student中的sid,name属性单独保存
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, tuple):
                # 找到了sid和name属性
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        # 新建两个类属性
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases,attrs)


class Student(metaclass=ModelMetaclass):
    # 类属性
    sid = ('sid', 'int unsigned')
    name = ('username', 'varchar(30)')

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            # 给实例对象创建属性
            setattr(self, k, v)

    def save(self):
        fields, args = [], []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k))
        
        args_temp = list()
        for temp in args:
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print("SQL: %s" % sql)

def main():
    student = Student(sid='123', name='张三')
    student.save()


if __name__ == "__main__":
    main()