

from models.base_model import BaseModel

class CustomerModel(BaseModel):

    @classmethod
    async def find_by_login(cls, login):
        sql = """select * from aio.customer where login = $1"""
        cursor = await cls.db.fetchrow(sql, login)

        return cursor

    @classmethod
    async def create(cls, login, password):
        sql = """insert into aio.customer(login, password) values($1, $2)"""
        await cls.db.execute(sql, login, password)

        customer = await cls.find_by_login(login)
        return customer
