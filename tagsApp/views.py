from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

import dateutil.parser
import json

from tagsApp.models import Tag, ReadTagsOrder


class TagsAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        
        return Response({"message": "Hello, world!"})

    def post(self, request):

        try:
            formatted_scan_time = dateutil.parser.parse(request.data['scan_time'])
            rto = ReadTagsOrder(scan_time=formatted_scan_time)
            rto.save()

            taglist = json.loads(request.data['tags'])

            Tag.objects.bulk_create([Tag(**{'strEPC' : t['strEPC'],
                                        'antenna' : t['antenna'],
                                        'strRSSI' : t['strRSSI'],
                                        'nReadCount' : t['nReadCount'],
                                        'readtagorder' : rto})
                            for t in taglist])

            return Response({"message": "Done!"})
        except Exception as e:
            return Response({"message": "Not Done!"})