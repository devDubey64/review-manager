from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tag, Review
from .serializers import TagSerializer, ReviewSerializer, AddRemoveTagSerializer

class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

	def create(self, request, *args, **kwargs):
		tags_data = request.data.pop('tags', [])

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)

		review_instance = serializer.instance
		tags = []
		for tag_data in tags_data:
			try:
				tag = Tag.objects.get(name=tag_data)
				tags.insert(len(tags), tag)
			except Tag.DoesNotExist:
				pass
		review_instance.tags.set(tags)

		return Response(serializer.data)

	def update(self, request, *args, **kwargs):
		tags_data = request.data.pop('tags', [])
		request.data['tags'] = [tag.lower() for tag in tags_data]
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

	def partial_update(self, request, *args, **kwargs):
		tags_data = request.data.pop('tags', [])
		if tags_data:
			request.data['tags'] = [tag.lower() for tag in tags_data]
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

class AddRemoveTag(APIView):

	def post(self, request, *args, **kwargs):
		serializer = AddRemoveTagSerializer(data=request.data)

		if serializer.is_valid(raise_exception=True):
			review_id = serializer.validated_data['review_id']
			tag_names = serializer.validated_data['tag_names']
			action = serializer.validated_data['action']

			try:
				review = Review.objects.get(pk=review_id)
				for tag_name in tag_names:
					try:
						tag_name = tag_name.lower()
						tag = Tag.objects.get(name=tag_name)
						if(action.lower() == 'add'):
							review.tags.add(tag)
						else:
							try:
								review.tags.remove(tag)
							except KeyError:
								pass
					except Tag.DoesNotExist:
						pass

				serialized_review = ReviewSerializer(review)
				return Response(serialized_review.data, status=status.HTTP_200_OK)
			except Review.DoesNotExist:
				return Response({'detail': 'Review not found.'}, status=status.HTTP_404_NOT_FOUND)