import graphene
from graphene_mongo import MongoengineObjectType

from ..models import RescueContact


class RescueContactType(MongoengineObjectType):
    class Meta:
        model = RescueContact
        fields = "__all__"


class Query(graphene.ObjectType):
    list_rescue_contacts = graphene.List(RescueContactType)
    get_rescue_contacts = graphene.Field(RescueContactType, id=graphene.String())

    def resolve_list_rescue_contacts(self, info) -> list[RescueContact]:
        return RescueContact.objects.all()

    def resolve_get_rescue_contacts(self, info, id) -> RescueContact:
        return RescueContact.objects.get(id=id)


class CreateRescueContact(graphene.Mutation):
    rescue_contact = graphene.Field(RescueContactType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        medical_qualifications = graphene.String()
        driver = graphene.Boolean()
        driving_privileges = graphene.Boolean()
        navigator = graphene.Boolean()
        planner = graphene.Boolean()

    def mutate(
        self,
        info,
        first_name,
        last_name,
        medical_qualifications,
        driver,
        driving_privileges,
        navigator,
        planner,
        email,
        phone,
    ):
        new_rescue_contact = RescueContact(
            first_name=first_name,
            last_name=last_name,
            medical_qualifications=medical_qualifications,
            driver=driver,
            driving_privileges=driving_privileges,
            navigator=navigator,
            planner=planner,
            email=email,
            phone=phone,
        )
        new_rescue_contact.save()
        return CreateRescueContact(rescue_contact=new_rescue_contact)


class UpdateRescueContact(graphene.Mutation):
    ok = graphene.Boolean()
    rescue_contact = graphene.Field(RescueContactType)

    class Arguments:
        id = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        medical_qualifications = graphene.String()
        driver = graphene.Boolean()
        driving_privileges = graphene.Boolean()
        navigator = graphene.Boolean()
        planner = graphene.Boolean()

    def mutate(
        self,
        info,
        first_name,
        last_name,
        medical_qualifications,
        driver,
        driving_privileges,
        navigator,
        planner,
        id,
        email,
        phone,
    ):
        update_rescue_contact = RescueContact.objects.get(id=id)
        update_rescue_contact.first_name = first_name
        update_rescue_contact.last_name = last_name
        update_rescue_contact.medical_qualifications = medical_qualifications
        update_rescue_contact.driver = driver
        update_rescue_contact.driving_privileges = driving_privileges
        update_rescue_contact.navigator = navigator
        update_rescue_contact.planner = planner
        update_rescue_contact.email = email
        update_rescue_contact.phone = phone
        update_rescue_contact.save()
        return UpdateRescueContact(ok=True, rescue_contact=update_rescue_contact)


class DeleteRescueContact(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String()

    def mutate(self, info, id):
        delete_rescue_contact = RescueContact.objects.get(id=id)
        delete_rescue_contact.delete()
        return DeleteRescueContact(ok=True)


class Mutation(graphene.ObjectType):
    create_rescue_contact = CreateRescueContact.Field()
    update_rescue_contact = UpdateRescueContact.Field()
    delete_rescue_contact = DeleteRescueContact.Field()
