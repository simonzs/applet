
# userinfo
userinfo = user = {
    "id": str, # ID标识
    "created_time": int, # 创建数据的时间
    "updated_time": int, # 更新数据的时间

    "reset": bool, # 密码是否初始化, 后端控制
    "user_id": int, # 用户编号

    # 创建
    "name": str, # 用户名称
    "remark": str, # 用户标签
    "password": str, # 用户密码
    "role": str, # 用户角色
}