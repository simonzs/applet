# -*- encoding: utf-8 -*-
'''
@File    :   userticket.py
@Time    :   2019/12/03 20:13:58
@Author  :   Simon 
@Version :   1.0
@Desc    :   None
'''

# from app.v1.model.base import DataObject, MongoBase
# from app.v1.driver.mongo import mongodb, mongo_id_to_str
# from app.v1.settings import settings


# class UserTicketObject(DataObject):

#     @property
#     def ticket(self):
#         return self.data.get("ticket", None)


# class MongoUserTicket(MongoBase):

#     def object(self, data):
#         return UserTicketObject(data)
        
#     def collection(self):
#         return mongodb.userticket()

#     def get_by_user_id(self, user_id):
#         # 底层查询
#         db_filter = {"user_id": user_id}
#         data = self.collection().find_one(db_filter)
#         if data:
#             data = self.deal_node(mongo_id_to_str(data))
#             data =self.object(data)
#         return data if data else None

#     def create_one(self, data):
#         return self.save(data)

# Data = MongoUserTicket()