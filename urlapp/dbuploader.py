from urlapp.models import short_url
from django.http import JsonResponse

def upload_details_to_database(data_to_insert):
    try:
        if data_to_insert['urlcount'] > 1:
            original_url = data_to_insert['originalurl']
            url_count = data_to_insert['urlcount'] 
            short_url.objects.filter(originalurl=original_url).update(urlcount=url_count)
        else:
            original_url = data_to_insert['originalurl']
            shortened_url = data_to_insert['shorturl']
            website_name = data_to_insert['websitename']
            url_count = data_to_insert['urlcount']
            new_short_url = short_url.objects.create(originalurl=original_url,
                                                    shorturl=shortened_url,
                                                    websitename=website_name,
                                                    urlcount=url_count)
            new_short_url.save()

        return JsonResponse("successful",safe=False)

    except Exception as e:
        print(f"Error connecting to SQLITE server: {e}")



