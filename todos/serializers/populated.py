from jwt_auth.serializers.common import NestedUserSerializer
from ..serializers.common import TodoSerializer

class PopulatedCommentSerializer(TodoSerializer):
    user = NestedUserSerializer()