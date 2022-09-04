from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import BaseCRUD
from app.models.charity_project import CharityProject


class CRUDCharityProject(BaseCRUD):

    async def get_charity_project_by_name(
        self,
        charity_project_name: str,
        session: AsyncSession
    ):
        charity_project = await session.scalar(
            select(self.model).where(
                self.model.name == charity_project_name
            )
        )
        return charity_project


charity_project_crud = CRUDCharityProject(CharityProject)
