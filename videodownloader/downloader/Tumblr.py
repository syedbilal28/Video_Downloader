import argparse
import json
import os
import requests


def get_photo_urls(blog_name, pages):
    for page in range(pages):
        api_url = (
                'http://{}.tumblr.com/api/read/json?start={}&num=50'.format(
                blog_name, page
                ))
        r = requests.get(api_url)
        if r.status_code == 404:
            print('Error: Does not able to retreive data')
            return
        html_src = r.text
        html_src = html_src.replace('var tumblr_api_read = ', '')
        html_src = html_src.replace(';', '')
        json_data = json.loads(html_src)

        for d in json_data['posts']:
            try:
                yield d['photo-url-1280']
            except:
                pass


def download_posts(url, blog_name):
    # Make filename
    url_chars = url.split('/')[-1]
    file_name = "{name}_{chars}".format(name=blog_name, chars=url_chars)

    # Start downloading
    if os.path.exists(file_name):
        pass
    else:
        r = requests.get(url, stream=True)
        print("Downloading {}".format(file_name))
        with open(file_name, 'wb') as outfile:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    outfile.write(chunk)
                else:
                    return
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tumblr download script')
    parser.add_argument(
            'blog_name',
            help='Name of the blog, eg. quotes'
            )
    parser.add_argument(
            '-n', '-num',
            dest='pages',
            metavar='N',
            action='store',
            type=int,
            default=1,
            help='Number of pages',
            )
    args = parser.parse_args()

    try:
        for url in get_photo_urls(args.blog_name, args.pages):
            download_posts(url, args.blog_name)
    except (KeyboardInterrupt, RuntimeError):
        import sys
        sys.exit()

