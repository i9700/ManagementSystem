from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        # 设置白名单
        print("request.path--->", request.path)
        if request.path in ["/login/", ]:
            return
        if not request.user.username:
            return redirect("/login/")
