from urllib.parse import urlparse

def extract_website_name(url):
    parsed_url = urlparse(url)
    website_name_parts = parsed_url.netloc.split('.')
    if len(website_name_parts) >= 2:
        return website_name_parts[-2]
    else:
        return website_name_parts[0]