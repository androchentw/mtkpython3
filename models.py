from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Mobile(Base):
    __tablename__ = "mobiles"

    id = Column(Integer, primary_key=True)
    number = Column(String(32))
    student_id = Column(Integer, ForeignKey("students.id"))

    def __repr__(self):
        return self.number

    def __str__(self):
        return self.number

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    mobiles = relationship("Mobile", backref="student")

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import os
    fn = "data.sqlite"
    dn = os.path.dirname(__file__)
    # engine: process
    engine = create_engine("sqlite:///" + os.path.join(dn, fn),
                            echo=True)
    # session: 連線, 保持連線所有改動
    Session = sessionmaker(bind=engine)
    s = Session()

    # 先把資料庫表格創造出來
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


    m = [Mobile(number="0912345678"),
         Mobile(number="0922222222")]
    student1 = Student(name="Elwing", mobiles=m)
    s.add(student1)

    s.commit()

    s1 = s.query(Student).filter_by(name="Elwing").first()
    print("查詢到的學生", s1)
    print("這學生的電話", s1.mobiles)

    m1 = s.query(Mobile).filter_by(number="0912345678").first()
    print("查詢到的電話", m1)
    print("這電話屬於誰", m1.student)