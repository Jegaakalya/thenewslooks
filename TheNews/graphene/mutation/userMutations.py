import graphene

from thenewslooks.TheNews.models import CustomUser
from thenewslooks.TheNews.serializers import CustomUserSerializer


class userCreateMutation(graphene.Mutation):
    """Mutation to create or update a CustomUser"""

    class Arguments:
        id = graphene.ID()
        username = graphene.String(required=True)
        phone_number = graphene.String()
        location = graphene.String()
        date_of_birth = graphene.String()
        is_admin = graphene.Boolean()
        is_user = graphene.Boolean()
        is_reporter = graphene.Boolean()

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        success = False
        errors = []
        serializer= ""

        if 'id' in kwargs and kwargs['id']:
            # Update operation
            user_instance = CustomUser.objects.filter(id=kwargs['id']).first()
            if not user_instance:
                errors.append("CustomUser not found.")
            else:
                serializer = CustomUserSerializer(user_instance, data=kwargs, partial=True)
        else:
            # Create operation
            serializer = CustomUserSerializer(data=kwargs)

        if serializer.is_valid():
            try:
                serializer.save()
                user_instance = serializer.instance
                success = True
            except Exception as e:
                errors.append(str(e))
        else:
            errors = [f"{field}: {'; '.join([str(e) for e in error])}" for field, error in serializer.errors.items()]

        return userCreateMutation(success=success, errors=errors)
