from flask_restful import Resource
from flask import Flask, request, jsonify
import json
from src.base.AragumentHandler import Arg_Handler
from src.base import DBTemplate

# from flask import request 파라미터 받기 .. GET : request.args.get('juso', "서울시") , request.form.get('email') POST : from flask import Flask, request, jsonify

class User(Resource):
    # def __init__():

    def get(self):
        return {'a':'1'}

# Interceptor 라고 하긴 좀 귀찮네 ..파이썬 데코레이터(Decorator) 
class RegistUser(Resource):
    @Arg_Handler
    def get(self , param:dict):
        print ('param' , param)
        # return {'result': 'ok'}

        # {'NOW': '2021-04-05'}
        selectRow = DBTemplate.Database().executeOne(" select DATE_FORMAT(now() , '%%Y-%%m-%%d') AS NOW " , {}) 

        result = {}
        result['selectRow'] = selectRow 
        result['param'] = param
        
        return result

    @Arg_Handler
    def post(self , param:json):
        # 애초에 dict 이네 ;;;;
        # param = request.get_json()

        print('param:' , param)

        # return {'mehtod': 'ok'}
        return param