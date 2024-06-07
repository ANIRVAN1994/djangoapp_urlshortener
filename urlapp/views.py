from django.shortcuts import render
import json, hashlib, os
from django.http import JsonResponse
from django.shortcuts import render
import json, time, datetime, shutil, os
from django.shortcuts import render, redirect
from django.http import HttpResponse, response, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from django.contrib.sessions.models import Session
from . import validationcheck, extractwebsite, dbuploader, dbfetcher
from urlshortproject.settings import BASE_DIR
# Create your views here.

@api_view(['GET'])
def homepage(request):
    request.session.flush()
    return render(request, 'home.html')

@api_view(['GET','POST'])
def post_url(request):
    if request.method == 'POST':
        json_data = request.data
        url_string = json_data['postedurl']
        request.session['original_url'] = url_string
        hash_code = hashlib.sha256(url_string.encode()).hexdigest()[:8]
        short_url = "http://short.url/" + hash_code

        #checking the url is present in db or not to calculate the count of url shortened
        time.sleep(1)
        existing_count = validationcheck.check_existing_url(url_string)
        if existing_count:
            newcount = existing_count + 1
            print(newcount)
        else:
            newcount = 1

        time.sleep(1)
        #parsing the website name from the parsar function
        website_name = extractwebsite.extract_website_name(url_string)
        print('The extracted Website Name is  :',website_name)  # Output: javatpoint

        # making a whole context 
        context = {'originalurl':url_string,'shorturl':short_url,'websitename':website_name, 'urlcount':newcount}

        time.sleep(1)
        # saving all the data in database
        dbuploader.upload_details_to_database(context)

        Fruit_Json = json.dumps(context)
        request.session['context'] = Fruit_Json

        # Though we are saving the context in the session variable, somwtime we are getting no saved data - which never be the case
        # so we are saving the context temporarily in a json file

        jsonfile_path = os.path.join(BASE_DIR,'tempfile.json')
        with open(jsonfile_path, 'w') as f:
            json.dump(context, f)

        return JsonResponse("ok",safe=False)

    if request.method == 'GET':
        # Reading the JSON file
        jsonfile_path = os.path.join(BASE_DIR, 'tempfile.json')
        with open(jsonfile_path, 'r') as f:
            saved_json_data = f.read()

        if saved_json_data:
            # Parse the JSON string into a dictionary
            saved_data_dict = json.loads(saved_json_data)
            print(saved_data_dict, '999999999999999999999999999')
        else:
            print('No saved data found in session')
            saved_data_dict = {}

        context = {'data': saved_data_dict}
        print(context)  # Check the context before passing to the template
        return render(request, 'returnedpage.html', context)


@api_view(['GET','POST'])
def get_top_three_domain_names(request):
    if request.method == 'POST':
        time.sleep(1)
        # fetch top 3 domain names from the db
        top_domain_names = dbfetcher.fetch_top_three()
        print(top_domain_names)

        jsonfile_path = os.path.join(BASE_DIR, 'topdomain.json')
        with open(jsonfile_path, 'w') as f:
            json.dump(top_domain_names, f)
        return JsonResponse("ok",safe=False)

    if request.method == 'GET':
        time.sleep(1)
        jsonfile_path = os.path.join(BASE_DIR, 'topdomain.json')
        with open(jsonfile_path, 'r') as f:
            saved_json_data = f.read()

        if saved_json_data:
            # Parse the JSON string into a dictionary
            saved_data_dict = json.loads(saved_json_data)
            print(saved_data_dict, '999999999999999999999999999')
        else:
            print('No saved data found in session')
            saved_data_dict = {}

        context = {'data': saved_data_dict}
        print(context)  # Check the context before passing to the template
        return render(request, 'returnedpage.html', context)

