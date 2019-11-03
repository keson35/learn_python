# 对象既包含数据，也包含方法。对象就是某一类具体事物的实例，
# 例如 7就是一个包含数据整数7和加法、乘法等方法的对象
# __init__ 是对象初始化方法，作用是根据类的定义创建实例对象
class Person1():
    def __init__(self, name):# 传入实例本身 self和实例名字 name，
        self.name = name # 将实例名字 name 赋值给实例 .name 属性

hunter = Person1('Bob') # 实例化 Person类
print('The hunter: ', hunter.name)


# 类的继承和覆盖及调用父类中方法


# 类的继承
class Car1():
    def exclaim(self): # 父类定义 exclaim()方法
        print("I'm a car.")

class Bmw1(Car1):
    pass # 子类未定义任何方法

give_me_a_car1 = Car1()
give_me_a_bmw1 = Bmw1()

give_me_a_car1.exclaim()
give_me_a_bmw1.exclaim() # 但子类实例仍然可以调用父类方法 exclaim()    


# 类的覆盖

class Person2():
    def __init__(self, name):
        self.name = name

class MDPerson(Person2):
    def __init__(self, name): # 覆盖父类中的对象初始化方法
        self.name = 'Doctor ' + name

class JDPerson(Person2):
    def __init__(self, name): # 覆盖父类中的对象初始化方法
        self.name = name + ' Esquie'

# 相同的name参数传递产生不同实例对象
person = Person2('Bob')
doctor = MDPerson('Bob')
lowyer = JDPerson('Bob')

print(person.name)
print(doctor.name)
print(lowyer.name)


# 覆盖后如何从子类调用父类方法
class Car2():
    def exclaim(self): # 父类定义 exclaim()方法
        print("I'm a car.")

class Bmw2(Car2):
    def exclaim(self): # 子类中的新 exclaim()方法覆盖父类中的 exclaim()方法 
        print("I'm a bmw.")
        super().exclaim() # super的作用是找到父类，然后把子类的对象变成父类的对象以调用父类的方法
        super(Bmw2, self).exclaim()   # 另一种描述更清晰的super()方法使用方式，功能同上

give_me_a_car2 = Car2()
give_me_a_bmw2 = Bmw2()

give_me_a_car2.exclaim()
give_me_a_bmw2.exclaim()


# self 参数的的意义在于让python找到正确的对象实例并调用它的方法及特性
car = Car1() # 本行的作用是实例化Car类，相当于把对象car作为 self参数传递给Car类所包含的所有方法
car.exclaim() # 通过car实例调用Car类 exclaim()方法
Car1.exclaim(car) # 另一种将对象car传递给Car类 exclaim()方法的方式，两种功能相同，但第一种更好


# 
class Person3():
    def __init__(self, name):
        self.name = name + ' jons' # 类似加字符串' jons'这种改动将被子类super()方法直接体现在子类 name特性中

class EmailPerson(Person3):
    def __init__(self, name, email):
        super().__init__(name) # 功能同下，更简洁
        super(EmailPerson, self).__init__(name) # 子类 EmailPerson 未创建 name 特性，
                                                # 采用初始化方法super()__init__调用父类name特性
                                                # 好处是将来对父类 Person3的变动将直接通过super()反应到子类上
        self.email = email

bob = EmailPerson('Bob', 'Bob@gmail.com')
bob.name
bob.email


# 使用属性对特性进行访问和设置,隐藏 hidden_name特性
class Duck1():
    def __init__(self,input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter: ',input_name)
        self.hidden_name = input_name
    
    name = property(get_name, set_name)

fowl = Duck1('Howard')
fowl.name # 获取hidden_name特性值可使用 self.name属性，不再需要使用 self.hidden_name显式获取方式
fowl.get_name() # 调用 self.get_name()获取特性值与直接调用 self.name属性功能相同
fowl.hidden_name # 调用 self.hidden_name获取特性值与上面两种功能相同


fowl.name = 'Daffe' # 设置hidden_name特性使用 self.name属性，不再需要使用 self.hidden_name显式获取方式
fowl.name
fowl.set_name('Daffy') # 调用 self.set_name()方法设置特性值与直接调用 self.name属性设置特性值功能相同
fowl.name
fowl.hidden_name = 'Daffz'# 调用 self.hidden_name设置特性值与上面两种功能相同
fowl.name
          

# 另一种定义属性的方式是使用 @property 和 @name.setter 装饰器
class Duck2():
    def __init__(self,input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter: ',input_name)
        self.hidden_name = input_name

fowl = Duck2('Howard')
fowl.name

fowl.name = 'Daffe' 
fowl.name


# 使用名称重整保护私有特性
class Duck3():
    def __init__(self,input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter: ',input_name)
        self.__name = input_name

fowl = Duck3('Howard')
fowl.name

fowl.name = 'Daffe' 
fowl.name

# fowl.__name # 报错，已经无法从外部直接访问__name 特性了
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Duck2' object has no attribute '__name'
fowl._Duck3__name # 特性名称重整后__name 特性名称变成 _Duck3__name
                  # 使用重整后名称仍可以访问特性值


# 方法的类型

# 1.实例方法：实例方法的首个参数是 self, 当实例方法被调用时，
#   python会把调用该方法的对象作为 self参数传入

# 2.类方法：作用于整个类，第一个参数是类本身 cls，使用前缀装饰器 @classmethod指定

# 3.静态方法：不会影响实例对象，也不会影响类，使用前缀装饰器 @staticmethod指定

class A():
    count = 0
    def __init__(self): # 实例方法——初始化
        A.count += 1
    def exclaim(self): # 实例方法——声明
        print("I'm a A!")
    @classmethod
    def kid(cls): # 类方法，对实例化次数进行统计
        print("A has", cls.count, "little object." )
    @staticmethod
    def commercial(): # 静态方法，对类和实例都没有影响
        print('This CoyoteWeapon has been brought to you by Acme.')

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kid()
A.commercial()


# 鸭子类型

class Quote(): # 父类，有 person特性和 words特性 who()方法、says()方法
    def __init__(self, person, words):
        self.person = person
        self.words = words
    
    def who(self):
        return self.person
    
    def says(self):
        return self.words + '.'
    
class QuestionQuote(Quote): # 子类 QuestionQuote 继承父类 Quote原有特性及方法并覆盖 says()方法
    def says(self):
        return self.words + '?'
    
class ExclaimQuote(Quote): # 子类 ExclaimQuote 继承父类 Quote原有特性及方法并覆盖 says()方法
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits") # 父类 Quote 实例化
print(hunter.who(), 'says:', hunter.says())         # 调用父类 Quote 实例中的who()方法，says()方法

hunter1 = QuestionQuote('Bugs Bunny', "What's up, doc") # 子类 QuestionQuote 实例化
print(hunter1.who(), 'says:', hunter1.says())           # 调用子类 QuestionQuote 实例中的who()方法，says()方法

hunter2 = ExclaimQuote('Daffy Duck', "It's rabbit season") # 子类 ExclaimQuote 实例化
print(hunter2.who(), 'says:', hunter2.says())              # 调用子类 ExclaimQuote 实例中的who()方法，says()方法

class BabblingBrook():
    
    def who(self):
        return 'Brook'
    
    def says(self):
        return 'Babble'
    
brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())
    
who_says(hunter)
who_says(hunter1)
who_says(hunter2)
who_says(brook) # 无论对象的类型是什么，只要它有 who()方法，
                # says()方法， 我们就可以调用它


# 特殊方法————魔术方法 用于实现等价于操作符的功能，例如 等于 "=="操作符

class Word():
    def __init__(self, text):
        self.text = text
    def equal(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

first.equal(second)
first.equal(third)

class Word1():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2): # 将__eq__ 定义为魔术方法，等同于 "=="操作符
        return self.text.lower() == word2.text.lower()

first = Word1('ha')
second = Word1('HA')
third = Word1('eh')

first == second 
first == third 


# 类的组合： 利用其它类的实例，组合后作为参数传入新类，新类将获得其它类的特性及方法
# 是一种除了继承之外的另一种获得子类的方法

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck(): # 组合Bill及Tail的特性
    def __init__(self, bill ,tail): # 将Bill及Tail的实例作为参数传入Duck类
        self.bill = bill
        self.tail = tail
    def about(self): # 通过传入的实例调用Bill及Tail类的实例特性 description及length
        print('The duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')

bill = Bill('wide orange')
tail = Tail('long')
duck = Duck(bill, tail)
duck.about()

