import sys
import os
import re
import requests as r
import wget

filedir =  "C:/Users/bilal/pictures"


def application(url,path):
    filedir =  f"media/{path}"
    ERASE_LINE = '\x1b[2K'

    try:
        LINK = input("Enter a Facebook Video Post URL: ")
        html = r.get(LINK)
        hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
    except r.ConnectionError as e:
        print("OOPS!! Connection Error.")
    except r.Timeout as e:
        print("OOPS!! Timeout Error")
    except r.RequestException as e:
        print("OOPS!! General Error or Invalid URL")
    except (KeyboardInterrupt, SystemExit):
        print("Ok ok, quitting")
        sys.exit(1)
    except TypeError:
        print("Video May Private or Hd version not avilable")
    else:
        hd_url = hdvideo_url.replace('hd_src:"', '')
        print("\n")
        print("High Quality: " + hd_url)
        print("[+] Video Started Downloading")
        wget.download(hd_url, filedir)
        sys.stdout.write(ERASE_LINE)
        print("\n")
        print("Video downloaded")

