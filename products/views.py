from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Description, ProductDescription, ProductUser
from .serializers import ProductSerializer, DescriptionSerializer, ProductDescriptionSerializer, ProductUserSerializer 
from rest_framework import status


# Create your views here.

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "Product List",
            "data": serializer.data
        })
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "Product Created",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "Product not created",
            "data": serializer.errors
        })
    
    def delete(self, request):
        product = Product.objects.get(id=request.data['id'])
        if product:
            product.delete()
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Product Deleted",
                "data": []
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "Product not found",
            "data": []
        })
    
class ProductOneView(APIView):
    def get(self, request):
        product = Product.objects.get(id=request.GET.get('id'))
        if product:
            serializer = ProductSerializer(product)
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Product",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "Product not found",
            "data": []
        })
    
    def put(self, request):
        product = Product.objects.get(id=request.data['id'])
        if product:
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": status.HTTP_200_OK,
                    "success": True,
                    "message": "Product Updated",
                    "data": serializer.data
                })
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "message": "Product not updated",
                "data": serializer.errors
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "Product not found",
            "data": []
        })
    
class DescriptionView(APIView):
    def get(self, request):
        descriptions = Description.objects.all()
        serializer = DescriptionSerializer(descriptions, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "Description List",
            "data": serializer.data
        })
    
    def post(self, request):
        serializer = DescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "Description Created",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "Description not created",
            "data": serializer.errors
        })
    
    def delete(self, request):
        description = Description.objects.get(id=request.data['id'])
        if description:
            description.delete()
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Description Deleted",
                "data": []
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "Description not found",
            "data": []
        })
    

class DescriptionOneView(APIView):
    def get(self, request):
        description = Description.objects.get(id=request.GET.get('id'))
        if description:
            serializer = DescriptionSerializer(description)
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "Description",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "Description not found",
            "data": []
        })
    
    def put(self, request):
        description = Description.objects.get(id=request.data['id'])
        if description:
            serializer = DescriptionSerializer(description, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": status.HTTP_200_OK,
                    "success": True,
                    "message": "Description Updated",
                    "data": serializer.data
                })
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "message": "Description not updated",
                "data": serializer.errors
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "Description not found",
            "data": []
        })
    
class ProductDescriptionView(APIView):
    def get(self, request):
        productDescriptions = ProductDescription.objects.all()
        serializer = ProductDescriptionSerializer(productDescriptions, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "ProductDescription List",
            "data": serializer.data
        })
    
    def post(self, request):
        serializer = ProductDescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "ProductDescription Created",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "ProductDescription not created",
            "data": serializer.errors
        })
    
    def delete(self, request):
        productDescription = ProductDescription.objects.get(id=request.data['id'])
        if productDescription:
            productDescription.delete()
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "ProductDescription Deleted",
                "data": []
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "ProductDescription not found",
            "data": []
        })
    

class ProductDescriptionOneView(APIView):
    def get(self, request):
        productDescription = ProductDescription.objects.get(id=request.GET.get('id'))
        if productDescription:
            serializer = ProductDescriptionSerializer(productDescription)
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "ProductDescription",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "ProductDescription not found",
            "data": []
        })
    
    def put(self, request):
        productDescription = ProductDescription.objects.get(id=request.data['id'])
        if productDescription:
            serializer = ProductDescriptionSerializer(productDescription, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": status.HTTP_200_OK,
                    "success": True,
                    "message": "ProductDescription Updated",
                    "data": serializer.data
                })
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "message": "ProductDescription not updated",
                "data": serializer.errors
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "ProductDescription not found",
            "data": []
        })
    
class ProductUserView(APIView):
    def get(self, request):
        productUsers = ProductUser.objects.all()
        serializer = ProductUserSerializer(productUsers, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "success": True,
            "message": "ProductUser List",
            "data": serializer.data
        })
    def post(self, request):
        serializer = ProductUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True,
                "message": "ProductUser Created",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "ProductUser not created",
            "data": serializer.errors
        })
    
    def delete(self, request):
        productUser = ProductUser.objects.get(id=request.data['id'])
        if productUser:
            productUser.delete()
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "ProductUser Deleted",
                "data": []
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "ProductUser not found",
            "data": []
        })
    
class ProductUserOneView(APIView):
    def get(self, request):
        productUser = ProductUser.objects.get(id=request.GET.get('id'))
        if productUser:
            serializer = ProductUserSerializer(productUser)
            return Response({
                "status": status.HTTP_200_OK,
                "success": True,
                "message": "ProductUser",
                "data": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "ProductUser not found",
            "data": []
        })
    
    def put(self, request):
        productUser = ProductUser.objects.get(id=request.data['id'])
        if productUser:
            serializer = ProductUserSerializer(productUser, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": status.HTTP_200_OK,
                    "success": True,
                    "message": "ProductUser Updated",
                    "data": serializer.data
                })
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "success": False,
                "message": "ProductUser not updated",
                "data": serializer.errors
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": "ProductUser not found",
            "data": []
        })