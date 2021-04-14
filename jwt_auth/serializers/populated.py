# from pics.serializers.populated import PopulatedPicSerializer
# from comments.serializers.common import CommentSerializer
from ..serializers.common import UserSerializer
from todos.serializers.common import TodoSerializer

class PopulatedUserSerializer(UserSerializer):

    todos = TodoSerializer(many=True)

