# 一些生成器方法，生成随机数，手机号，以及连续数字等
import random
from faker import Factory

fake = Factory().create('zh_CN')

# 随机手机号
def random_phone_number():
    return fake.phone_number()

# 随机姓名
def random_name():
    return fake.name()

# 随机地址
def random_address():
    return fake.address()

# 随机email
def random_email():
    return fake.email()

# 随机IPV4地址
def random_ipv4():
    return fake.ipv4()

# 长度在最大值与最小值之间的随机字符串
def random_str(min_chars=0, max_chars=9):
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)

# 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment
# 生成器为用的时候才读取数据，yield就是return返回一个值，并且记住这个返回的值，下次迭代就从这个位置后（下一行）开始
def factory_generate_ids(starting_id=1, increament=1):
    def generate_started_ids():
        val = starting_id
        local_increment = increament
        while True:
            yield val   #迭代，返回下一个值
            val += local_increment
    return generate_started_ids

# 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机选取一项。
def factoty_choice_generator(values):
    def choice_generator():
        my_list = list(values)
        rand = random.Random()
        while True:
            yield random.choice(my_list)
    return choice_generator


if __name__ == '__main__':
    print(random_phone_number())
    print(random_name())
    print(random_address())
    print(random_email())
    print(random_ipv4())
    print(random_str(min_chars=6, max_chars=9))
    id_gen = factory_generate_ids(starting_id=0, increament=2)()
    for i in range(5):
        print(next(id_gen))

    choices = ['张三', '李四', '王五', '赵六']
    choice_gen = factoty_choice_generator(choices)()
    for i in range(5):
        print(next(choice_gen))



