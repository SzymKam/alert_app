import graphene

from ..views import SendingAlarmMessages


class JSONString(graphene.Scalar):
    @staticmethod
    def serialize(json_value):
        return json_value


class SendAlarm(graphene.Mutation):
    confirmation = JSONString()

    class Arguments:
        ids = graphene.List(graphene.String)
        message = graphene.String()

    def mutate(self, info, ids, message):
        sending_alarm = SendingAlarmMessages(ids=ids, message=message)
        alarmed_result = sending_alarm.main()

        return SendAlarm(confirmation=alarmed_result)


class Mutation(graphene.ObjectType):
    send_alarm = SendAlarm.Field()
