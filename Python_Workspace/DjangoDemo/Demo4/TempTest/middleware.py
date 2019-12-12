from django.http import HttpResponse
class BlockIpMiddleware():
    """中间件类"""
    exclude_ip = ['10.21.21.115']
    def process_view(self, request, view_func, *args, **kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockIpMiddleware.exclude_ip:
            return HttpResponse('<h1>Forbidden</h1>')

class TestMiddleware():
    def __init__(self):
        '''服务器处理第一个请求时调用'''
        print('---init---')
    
    def process_request(self, request):
        '''request对象产生之后，在url匹配之前调用'''
        print('---process_request---')
    
    def process_view(self, request, view_func, *args, **kwargs):
        '''url匹配完成后，在视图函数调用之前调用'''
        print('---process_view---')
    
    def process_response(self, request, response):
        '''在视图函数完成之后，内容返回给浏览器之前调用'''
        # response表示视图函数的返回值(既要返回给页面的内容)
        print('---process_response---')
        return response