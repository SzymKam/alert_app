import graphene

from app.schema.rescue_contact_schema import Mutation as RescueContactMutation
from app.schema.rescue_contact_schema import Query as RescueContactQuery
from app.schema.send_alarm_schema import Mutation as SendAlarmMutation


class Query(RescueContactQuery, graphene.ObjectType):
    pass


class Mutation(RescueContactMutation, SendAlarmMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
