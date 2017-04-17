def make_car(product, type, **orther_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['product_name'] = product
    profile['type_name'] = type
    for key, value in orther_info.items():
        profile[key] = value
        #return profile
    return profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)