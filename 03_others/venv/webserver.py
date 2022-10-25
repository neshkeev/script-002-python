from aiohttp import web


async def user_handle(request):
    # http://127.0.0.1:8080/Username
    name = request.match_info.get('name', 'Anonymous')
    text = f'Hello, {name}'
    return web.Response(text=text, content_type='text/html')


app = web.Application()
app.add_routes([
    web.get('/user/', user_handle),
    web.get('/user/{name}', user_handle),
])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
