from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import \
    WarrantySerializer,\
    TrunkSerializer,\
    MotherBoardSerializer
from .models import Warranty, Trunk, MotherBoard
from django.db import connection


class ProcessRawSqlAPIView(APIView):
    def post(self, request):
        with connection.cursor() as cursor:
            sql_query = request.data.get('sql')
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            return Response(rows)


class ComponentsByWarrantyViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk):
        # Add plain SQL in order to demonstrate this code for lab
        warranty = Warranty.objects.raw('''
                                    select * from data_center_warranty
                                        where id = %s;
                                        ''', [pk])
        warranty = warranty[0]
        trunks = Trunk.objects.raw('''
                                select * from data_center_trunk
                                    where warranty_id = %s
                                   ''', [warranty.pk])
        trunks = [*trunks]
        motherboards = MotherBoard.objects.raw('''
                                        select * from data_center_motherboard
                                            where warranty_id = %s
                                               ''', [warranty.pk])
        motherboards = [*motherboards]
        warranty = WarrantySerializer(warranty).data
        trunks = TrunkSerializer(trunks, many=True).data
        motherboards = MotherBoardSerializer(motherboards, many=True).data
        response = {
            'components': [*trunks, *motherboards],
            'warranty': warranty
        }
        return Response(response)
