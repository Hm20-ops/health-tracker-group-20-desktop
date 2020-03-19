from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import *

from ModelHandler import *


class UserExercise(Base):
	__tablename__ = 'UserExercise'

	activityId = Column(Integer, primary_key=True)
	exerciseId = Column(ForeignKey('ExerciseDictionary.exerciseId'))
	username = Column(ForeignKey('User.username'), nullable=False)
	caloriesBurnt = Column(Float, nullable=False)
	activityDate = Column(Text, server_default=text("NULL"))

	FoodDictionary = relationship('ExerciseDictionary')
	User = relationship('User')

	def totalCaloriesBurnt(self, username):
		session = make_session()
		calBurntResult = session.query(func.sum(UserExercise.caloriesBurnt).label('caloriesBurnt'))\
								.filter(UserExercise.username == username,
							            UserExercise.activityDate == datetime.today().strftime('%d/%m/%Y'))\
								.group_by(UserExercise.username).first()[0]
		session.close()
		return calBurntResult
