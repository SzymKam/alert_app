import graphene

from app.schema.mongo_db_rescue_contact_schema import Mutation as RescueContactMutation
from app.schema.mongo_db_rescue_contact_schema import Query as RescueContactQuery
from app.schema.send_alarm_schema import Mutation as SendAlarmMutation


class Query(RescueContactQuery, graphene.ObjectType):
    pass


class Mutation(SendAlarmMutation, RescueContactMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
