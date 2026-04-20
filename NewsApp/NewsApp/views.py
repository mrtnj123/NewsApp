
from django.shortcuts import render,redirect
import requests as rq


def home(request):
	return render(request, 'index.html')


def gen(request):
	x = request.GET.get('v')
	key = 'b5e4a37c249d4bb6bdc37005b167bf0f'

	if x:
		url = 'https://newsapi.org/v2/top-headlines?country=us&category='+x+'&apiKey='+key
		d = rq.get(url).json()
		d1 = d["articles"]

		# for i in d1:
		# 	print(i["title"]+"\n")


	context = {'title' : x, 'data' : d1}
	return render(request, 'newslist.html', context)


def news(request):
	pos= int(request.GET.get('x')) -1
	cat =  request.GET.get('y')

	context = {}
	key = 'b5e4a37c249d4bb6bdc37005b167bf0f'

	if  cat:
		url = 'https://newsapi.org/v2/top-headlines?country=us&category='+cat+'&apiKey='+key
		d = rq.get(url).json()
		d1 = d["articles"]
		d2 = d1[pos]

		print('data: ',d2['title'])
		context['data'] = d2
	

	return render(request, 'news.html',context)

