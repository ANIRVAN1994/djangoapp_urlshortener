from .models import short_url

def check_existing_url(url_string):

    try:
        url_count = list(short_url.objects.filter(originalurl=url_string).values_list('urlcount', flat=True))
        if url_count:
            print(url_count[0],'0000000000000000000000000')
            return url_count[0]
        else:
            return 0
    except Exception as e:
        print(f"Error connecting to Sqlite server: {e}")