from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

# Base 클래스 정의
Base = declarative_base()

#  2. 테이블 생성: User 모델 정의
class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name})>"

#  3. 데이터베이스 연결 (SQLite 사용)
engine = create_engine("sqlite:///users.db", echo=True) #DB 생성및 연결

# 4. 테이블 생성
Base.metadata.create_all(bind=engine) # 테이블이 있으면 수정까지 해줌

# 5. session 준비(cur=connect.cursor())
SessionLocal = sessionmaker(bind=engine)

def run_single():
    """데이터베이스 실제 핸들링 코드"""
    db = SessionLocal()

    # create
    new_user = User(name="OZ")
    db.add(new_user)
    db.commit()

    # read
    # users = db.query(User).all() # 여러 유저 한번에 조회
    user = db.query(User).first()
    print("유저 조회 완료 : ", user)
    

    # updata
    user.name = "환율"
    db.commit()

    user = db.query(User).first()
    print("수정된 유저 조회 완료 : ", user)


    # delete
    db.delete(user)
    db.commit()

# 복수 데이터 핸들링
def run_bulk():
    db = SessionLocal()
    #### create
    new_users = [User(name="OZ_BE1"), User(name="OZ_BE2"), User(name="OV_BE3")]
    db.add_all(new_users)
    db.commit()

    #### read
    users = db.query(User).all()
    for user in users:
        print(user)

    # read : 조건부
    oz_user = db.query(User).filter(User.name == "OZ_BE1").first()
    print(oz_user)

    # read : 조건부 패턴 검색
    oz_user = db.query(User).filter(User.name.like("OZ_%")).all()
    print("OZ포함된 이름 찾기:", oz_user)

    #### update
    for u in oz_user:
        u.name = u.name + "_NEW"
    db.commit()

    users=db.query(User).all()
    for u in users:
        print(u)

    #### delete
    oz_user = db.query(User).filter(User.name.like("OZ_%")).all()
    for u in oz_user:
        db.delete(u)

    db.query(User).delete() # 테이블 전체 데이터 삭제
    db.commit()

    db.close()
if __name__ == "__main__":
    # run_single()
    run_bulk()