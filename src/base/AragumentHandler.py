from flask import Flask, request, jsonify

def Arg_Handler(func) :
    def wrapper(*args, **kwargs):
        print('pre')

        headers = request.headers
    
        print( headers.values())
        print( headers.values)

        kwarg =  __getParam__()

        res = func(*args , kwarg)
               
        print('after')

        return res
    return wrapper

def __getParam__() :
    print ( request.method )
    
    if request.method == 'GET' :
        # print(request.query_string)
        # print(request.get_json)
        # print(request.args)
        # print(request.args.to_dict)
        # print(request.args.to_dict(flat=False))

        # return request.args.to_dict
        return request.args.to_dict(flat=False)
    else :
        return request.get_json()