from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import ImageSerializer
from PIL import Image, ImageEnhance
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from rest_framework import status

class EnhanceImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_file = serializer.validated_data['image']
            
            # Open the original image
            with Image.open(image_file) as img:
                # Apply enhancements
                enhancer = ImageEnhance.Sharpness(img)
                img = enhancer.enhance(2.0)  # sharpness
                
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(1.5)  # contrast
                
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(1.1)  # brightness
                
                enhancer = ImageEnhance.Color(img)
                img = enhancer.enhance(1.5)  # color

                # Save the enhanced image to a BytesIO object
                img_io = BytesIO()
                img.save(img_io, format='JPEG', quality=85)
                img_io.seek(0)
                img_file = InMemoryUploadedFile(img_io, None, 'enhanced.jpg', 'image/jpeg', img_io.tell(), None)
                
                response = HttpResponse(img_file, content_type='image/jpeg')
                response['Content-Disposition'] = 'attachment; filename="enhanced.jpg"'
                return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)