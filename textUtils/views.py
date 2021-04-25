# this is created by me
from django.http import HttpResponse
from django.shortcuts import render



# index page
def index(request):
    return render(request, 'index.html')


# This is the function called when form is submitted
def analyze(request):

    # get the text
    text = request.POST.get('text', 'default');

    # get checkbox vales
    removepunc = request.POST.get('removepunc', 'default');
    capitalize = request.POST.get('capitalize', 'default');
    new_line_remover = request.POST.get('new_line_remover', 'default');
    extra_space_remover = request.POST.get('extra_space_remover', 'default');
    char_counter = request.POST.get('char_counter', 'default');

    # print text
    # print(text);
    # print(removepunc);
    # print(capitalize);

    # definations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''';
    analyzed = "";
    counter = 0;

    # used to remove punctuations
    if (removepunc == "on"):
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char;
        text = analyzed;

    # checked to capitalize text
    if (capitalize == "on"):
        analyzed="";
        for char in text:
            analyzed = analyzed + char.upper();
        text = analyzed;

    # to remove new line
    if (new_line_remover == "on"):
        analyzed="";
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char;
        text = analyzed;

    # to remove extra space
    if (extra_space_remover == "on"):
        analyzed="";
        for index, char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed = analyzed + char;
        text = analyzed;

    # to count the character only
    if (char_counter == "on"):
        analyzed="";
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char;
        for char in analyzed:
            if not (char == " " or char == "\n" or char == "\r"):
                counter = counter + 1;
        text = analyzed;

    # if No option is selcted
    if(removepunc != "on" and capitalize != "on" and new_line_remover != "on" and extra_space_remover != "on" and char_counter != "on"):
        return HttpResponse("<h2>Select atleast one option</h2> ");

    # parameter sent to analyze page to display output
    params = {'purpose': 'Remove punctuations', 'analyzed_text': text, 'counter': counter}
    return render(request, 'analyze.html', params)




#
# def cart(request):
#     return HttpResponse("this is cart"
#                         '<a href="/sign">click to sign</a>')
# def sign(request):
#     return HttpResponse("this is sign"
#                         '<a href="/account">click to account</a>')
# def account(request):
#     return HttpResponse("this is account"
#                         '<a href="/service">click to service</a>')
# def service(request):
#     return HttpResponse("this is service"
#                         '<a href="/">click to index</a>')
