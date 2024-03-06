import graphene

from ..views import SendingAlarmMessages


class SendAlarm(graphene.Mutation):
    confirmation = graphene.String()

    class Arguments:
        ids = graphene.List(graphene.String)
        message = graphene.String()

    def mutate(self, info, ids, message):
        sending_alarm = SendingAlarmMessages(ids=ids, message=message)
        alarmed_contacts = sending_alarm.main()

        return SendAlarm(confirmation=alarmed_contacts)


class Mutation(graphene.ObjectType):
    send_alarm = SendAlarm.Field()
