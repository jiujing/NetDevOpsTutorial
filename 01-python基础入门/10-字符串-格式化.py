if __name__ == '__main__':
    """
    推荐使用format
    用于格式化输出
    展开的值可以是复杂的对象，会调用str(对象)展开，避免传统字符串格式化报错的问题。
    """
    # {}占位，后续提供占位的实际值，默认按需依次展开
    somebody_info_templ = 'name is:{},age is {}'
    somebody_info = somebody_info_templ.format('xiaoming', '18')
    # 等同somebody_info = 'name is:{},age is {}'.format('xiaoming', '18')
    print(somebody_info)

    # 可以指定顺序
    somebody_info_templ = 'name is:{1},age is {0}'
    somebody_info = somebody_info_templ.format('18', 'xiaoming')
    print(somebody_info)

    # 指定字段值
    somebody_info_templ = 'name is:{name},age is {age}'
    name = 'xiaoming'
    age = 18
    # format的函数的参数顺序可以打乱，模板里的字符串必须都有对应赋值
    somebody_info = somebody_info_templ.format(name=name, age=age, sex='male')
    # 等同somebody_info = 'name is:{},age is {}'.format('xiaoming', '18')
    print(somebody_info)
