def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        #return profile
    return profile
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
print('\n')
my_profile = build_profile('bj', 'cao', locatio='sh', city='sh', country='zg')
print(my_profile)