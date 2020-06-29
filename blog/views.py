from django.shortcuts import render

from notion.client import NotionClient
from .utils.renderer import HTMLRenderer
import os


def get_blog(url=''):
    client = NotionClient(token_v2=os.getenv('NOTION_TOKEN'))
    entry_url = 'https://www.notion.so/Blog-93ca297bbe9d45e68eee6e2cc8b2deae'
    page = client.get_block(entry_url)
    return page, client
# Create your views here.


def index(request):
    page, client = get_blog()

    renderer = HTMLRenderer(client)
    if len(HTMLRenderer.output) > 0:
            renderer.cleanup()
    rendered_result = renderer.render_page(page)
    output = HTMLRenderer.output
    print(len(output))
    title = page.title
    context = {
        'page': page,
        'title': title,
        'rendered': rendered_result,
        'output': output,
    }
    return render(request, 'blog/index.html', context)
