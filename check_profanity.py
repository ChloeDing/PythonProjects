import urllib

def read_text():
    file = open(".../movie_quotes.txt")
    content_of_file = file.read()
    print(content_of_file)
    file.close()
    return content_of_file




def get_length(s):
    print("the length of the provided string " + s + " is: " + str(len(s)))


#get_length("hello")


def check_profanity(content_of_file):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + content_of_file)
    response = connection.read()
    print(response)
    connection.close()
    return response

def check():
    content_of_file = read_text()
    response = check_profanity(content_of_file)
##    if(response == "true"):
##        print("dirty")
##    else:
##        print("clean")

    if "true" in response:
        print("Profanity Alert!!")
    elif "false" in response:
        print("This document has no curse word")
    else:
        print("Could not scan the document properly")


check()
