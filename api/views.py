
from unicodedata import name
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from main.models import Category, Location, Company, Image, Counter, Banner, ContactUs
from .serializers import CategorySerializer, ContactSerializer, CompanySerializer, LocationSerializer, VipCompany, CounterSerializer, CompanyVisitedSerializer


class ContactFormListView(APIView):
    def post(self, request):
        contact = ContactUs.objects.all()
        data = request.data
        data['email'] = data['email']
        data['message'] = data['message']

        serializer = ContactSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyView(APIView):
    def get(self, request, pk):
        try:
            company = Company.objects.get(id=pk)
            serializer = CompanySerializer(company, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Company does not exist'}, status=status.HTTP_404_NOT_FOUND)
            


class CategoryView(APIView):
    def get(self, request, pk):
        try:
            categories = Category.objects.get(id=pk)
            product = Company.objects.filter(category=categories)
            serializer = CompanySerializer(product, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)


class BannerListView(APIView):
    def get(self, request):
        banner = Banner.objects.all()
        serializer = CategorySerializer(banner, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LocationListView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyListView(APIView):
    def get(self, request):
        title = None
        category_id = None
        location_id = None
        companies = Company.objects.all()
        if request.query_params.get('title', None):
            title = request.query_params.get('title', None)
            companies = companies.filter(title__icontains=title)
        if request.query_params.get('category_id', None):
            category_id = request.query_params.get('category_id', None)
            companies = companies.filter(category_id=category_id)
        if request.query_params.get('location_id', None):
            location_id = request.query_params.get('location_id', None)
            companies = companies.filter(location_id=location_id)
            print(companies)

        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VipListView(APIView):
    def get(self, request):
        vip_companies = Company.objects.filter(status="VIP")
        serializer = VipCompany(vip_companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CounterView(APIView):
    def put(self, request):
        try:
            counter = Counter.objects.latest('id')
            data = request.data
            data['visited_counter'] = counter.visited_counter + 1
            serializer = CounterSerializer(counter, data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)


class CompanyVisitedView(APIView):
    def put(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
            counter = company.seen_count + 1
            data = request.data
            data['seen_count'] = counter
            data['title'] = company.title
            data['logo'] = company.logo
            data['status'] = company.status
            data['like_count'] = company.like_count
            serializer = CompanyVisitedSerializer(company, data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Error': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)


class CompanyLikedView(APIView):
    def put(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
            counter = company.like_count + 1
            data = request.data
            data['seen_count'] = company.seen_count
            data['title'] = company.title
            data['logo'] = company.logo
            data['status'] = company.status
            data['like_count'] = counter
            serializer = CompanyVisitedSerializer(company, data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Error': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)
