from urlapp.models import short_url

def fetch_top_three():
    try:
        result = list(short_url.objects.values('websitename', 'urlcount').order_by('-urlcount')[:3])
        print(result,'oooooooooooooooooooooooooooooooo999999999999999999999999999')
        return result

    except Exception as e:
        print(f"Error connecting to SqLight server: {e}")
        return None

