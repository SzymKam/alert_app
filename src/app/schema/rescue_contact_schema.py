import graphene
from graphene_django import DjangoObjectType

from ..models import RescueContact


class RescueContactType(DjangoObjectType):
    class Meta:
        model = RescueContact
        fields = "__all__"


class Query(graphene.ObjectType):
    list_rescue_contacts = graphene.List(RescueContactType)
    get_rescue_contacts = graphene.Field(RescueContactType, id=graphene.Int())

    def resolve_list_rescue_contacts(self, info):
        return RescueContact.objects.all()

    def resolve_get_rescue_contacts(self, info, id):
        return RescueContact.objects.get(id=id)


class CreateRescueContact(graphene.Mutation):
    rescue_contact = graphene.Field(RescueContactType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        medical_qualifications = graphene.String()
        is_driver = graphene.Boolean()
        has_vehicle_driving_privileges = graphene.Boolean()
        is_navigator = graphene.Boolean()
        is_planner = graphene.Boolean()

    def mutate(
        self,
        info,
        first_name,
        last_name,
        medical_qualifications,
        is_driver,
        has_vehicle_driving_privileges,
        is_navigator,
        is_planner,
        email,
        phone,
    ):
        new_rescue_contact = RescueContact(
            first_name=first_name,
            last_name=last_name,
            medical_qualifications=medical_qualifications,
            is_driver=is_driver,
            has_vehicle_driving_privileges=has_vehicle_driving_privileges,
            is_navigator=is_navigator,
            is_planner=is_planner,
            email=email,
            phone=phone,
        )
        new_rescue_contact.save()
        return CreateRescueContact(rescue_contact=new_rescue_contact)


class UpdateRescueContact(graphene.Mutation):
    ok = graphene.Boolean()
    rescue_contact = graphene.Field(RescueContactType)

    class Arguments:
        id = graphene.ID()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        medical_qualifications = graphene.String()
        is_driver = graphene.Boolean()
        has_vehicle_driving_privileges = graphene.Boolean()
        is_navigator = graphene.Boolean()
        is_planner = graphene.Boolean()

    def mutate(
        self,
        info,
        first_name,
        last_name,
        medical_qualifications,
        is_driver,
        has_vehicle_driving_privileges,
        is_navigator,
        is_planner,
        id,
        email,
        phone,
    ):
        update_rescue_contact = RescueContact.objects.get(id=id)
        update_rescue_contact.first_name = first_name
        update_rescue_contact.last_name = last_name
        update_rescue_contact.medical_qualifications = medical_qualifications
        update_rescue_contact.is_driver = is_driver
        update_rescue_contact.has_vehicle_driving_privileges = has_vehicle_driving_privileges
        update_rescue_contact.is_navigator = is_navigator
        update_rescue_contact.is_planner = is_planner
        update_rescue_contact.email = email
        update_rescue_contact.phone = phone
        update_rescue_contact.save()
        return UpdateRescueContact(ok=True, rescue_contact=update_rescue_contact)


class DeleteRescueContact(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):
        delete_rescue_contact = RescueContact.objects.get(id=id)
        delete_rescue_contact.delete()
        return DeleteRescueContact(ok=True)


class Mutation(graphene.ObjectType):
    create_rescue_contact = CreateRescueContact.Field()
    update_rescue_contact = UpdateRescueContact.Field()
    delete_rescue_contact = DeleteRescueContact.Field()
