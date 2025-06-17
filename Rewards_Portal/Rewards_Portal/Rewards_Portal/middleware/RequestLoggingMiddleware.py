from home.models import RequestLogs

class RequestMiddlewareLogs:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        '''
        request_info = (request)
        RequestLogs.objects.create(
            request_info = str(vars(request_info)),
            request_type = request_info.method,
            request_method = request_info.path 
        )

        # Code to be executed for each request/response after
        # the view is called.
        print("response -->", request_info)
        return request_info
        '''
        response = self.get_response(request)

        # Use request object directly
        RequestLogs.objects.create(
            request_info = str(vars(request)),
            request_type = request.method,
            request_method = request.path
        )

        print("response -->", response)
        return response