# serializers.py
from rest_framework import serializers

from gamelib.models import Game, Requirement
class RequirementSerializer(serializers.ModelSerializer):
    requirements = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field=('__all__')
     )

    class Meta:
        model = Requirement
        fields = ('__all__')
class GameSerializer(serializers.ModelSerializer):
    #category_name = serializers.CharField(source='requirement_id.os')
    requirement_os = serializers.CharField(source='requirement_id.os')
    requirement_ram = serializers.CharField(source='requirement_id.ram')
    requirement_storage = serializers.CharField(source='requirement_id.storage')
    requirement_processor = serializers.CharField(source='requirement_id.processor')
    requirement_graphic = serializers.CharField(source='requirement_id.graphic')
    #category_name = serializers.RelatedField(source='requirement_id', read_only=True)
    #requirements = serializers.StringRelatedField(many=True)
    class Meta:
        model = Game
        fields = ('id' , 'name' , 'description' , 'producer' , 'publisher' ,'home_page' , 'release_date' , 'images' , 'categories' , 
        'requirement_os' , 'requirement_ram','requirement_storage','requirement_processor','requirement_graphic')
    def to_representation(self, instance):
        ret = super(GameSerializer, self).to_representation(instance)
        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        extra_ret = {'message': 'get game successfully' , 'status' : True} if is_list_view else {'message': 'get game successfully' , 'status' : True}
        ret.update(extra_ret)
        return ret

    #     name = models.CharField(max_length=len_medium)
    # description = models.CharField(max_length=len_max)
    # producer = models.CharField(max_length=len_medium)
    # publisher = models.CharField(max_length=len_medium)
    # home_page = models.CharField(max_length=len_medium)
    # requirement_id = ForeignKey(Requirement , on_delete=models.CASCADE)
    # release_date = models.DateTimeField(blank=None,null=None)
    # images = ArrayField(ArrayField(models.CharField(max_length=len_medium)))
    # categories = models.ManyToManyField(Category)