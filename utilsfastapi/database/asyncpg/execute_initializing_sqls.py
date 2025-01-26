from fastapi import FastAPI


async def execute_initializing_sqls(app: FastAPI, initializing_sqls: list[str]):
    async with app.state.pool.acquire() as connection:
        for initializing_sql in initializing_sqls:
            await connection.execute(initializing_sql)