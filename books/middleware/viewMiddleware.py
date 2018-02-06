try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object
    class ViewMiddleware(MiddlewareMixin):
        process_req(self,request):
            request.dept = "OS"
            return None
