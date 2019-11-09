from django.shortcuts import render
from django.views import View
from .reader import Reader

import json
class TilesView(View):
    root_sheet_name = "Main"
    def display(self, request, sheet_name):
        reader = Reader(sheet_name)
        tiles_data = reader.get_tiles_data()
        return render(request, "index.html", {"tiles": tiles_data, "js_data": json.dumps(tiles_data),"can_go_back":sheet_name != self.root_sheet_name, "back_sheet_name": reader.get_parent()})

    def get(self, request, *args, **kwargs):
        return self.display(request, self.root_sheet_name)
    
    def post(self, request, *args, **kwargs):
        print(request.POST["name"])
        return self.display(request, request.POST["name"])
    
    