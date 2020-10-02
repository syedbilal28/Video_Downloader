from instalooter.looters import PostLooter
def application(url,path):
    looter = PostLooter(url)
    var=looter.download(f"media/{path}")
    return var 
