from django.shortcuts import render

def home(request):
    return render(request, '1.html')

def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)
    dict_word = {}

    for word in user_text:
        if word not in dict_word:
            dict_word[word] = 1
        else:
            dict_word[word] += 1

    return render(request,'count.html',{'count':total_count,'text':user_text,
                                        'dicword':dict_word})

def about(request):
    return render(request, 'about.html')
