import sqlalchemy
from sqlalchemy.orm import Session
from models.pc import *
from models.users import *


class ClubService:
    def __init__(self, db: Session):
        self.db = db

    def add_pc(self, pc_name: str):
        try:
            new_pc = Pcs(
                pc_name=pc_name,
            )
            self.db.add(new_pc)
            self.db.commit()
            self.db.refresh(new_pc)
            print(f"Added PC: {new_pc.pc_name}")
        except Exception as e:
            print(e)
        return new_pc

    def add_user(self, user_name_surname: str, pc_id: str, user_time: str):
        try:
            new_user = Users(
                user_name_surname=user_name_surname,
                pc_id=pc_id,
                user_time=user_time
            )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            print(f"Added User: {new_user.user_name_surname}")
        except Exception as e:
            print(e)
        return new_user

    def get_all_users(self):
        users = self.db.query(Users.user_id, Users.user_name_surname, Pcs.pc_name, Users.user_time).join(Pcs).all()
        return users
    def get_all_pc(self):
        pc = self.db.query(Pcs.pc_id, Pcs.pc_name).all()
        return pc

    def delete_user(self, user_id: int):
        user_to_delete = self.db.query(Users).get(user_id)

        if user_to_delete:
            self.db.delete(user_to_delete)
            self.db.commit()
            print(f"Deleted User: {user_to_delete.user_id}")
        else:
            print("User not found.")

    def update_data(self, user_id, user_name_surname, pc_id, user_time):
        user_updete = self.db.query(Users).filter(Users.user_id == user_id).first()
        user_updete.user_id = user_id
        user_updete.user_name_surname = user_name_surname
        user_updete.pc_id = pc_id
        user_updete.user_time = user_time
        self.db.commit()

