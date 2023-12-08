import typing as t

import motor.motor_asyncio

from app.repository.db.base import BaseDB


class MongoDB(BaseDB):
    db: motor.motor_asyncio.AsyncIOMotorDatabase  # type: ignore[valid-type]

    def __init__(
        self,
        *,
        client: motor.motor_asyncio.AsyncIOMotorClient,  # type: ignore[valid-type]
        database_name: str,
    ) -> None:
        super().__init__()
        self._client = client
        self._database_name = database_name
        self.db = self._client[self._database_name]  # type: ignore[index]

    async def is_alive(self) -> bool:
        return t.cast(bool, await self._client.admin.command("ping"))  # type: ignore[attr-defined]
