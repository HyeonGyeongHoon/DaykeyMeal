# file name : index.py
# pwd : /project_name/app/main/index.py
 
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
import requests
import json
import datetime
# 추가할 모듈이 있다면 추가
 
main = Blueprint('main', __name__, url_prefix='/')
 
@main.route('/main', methods=['GET'])
def index():
      now=datetime.datetime.now()
      response = requests.get('https://schoolmenukr.ml/api/high/T100000132?year='+str(now.year)+'&month='+str(now.month)+'&date='+str(now.day)+'&allergy=hidden')
      #response = requests.get('https://schoolmenukr.ml/api/high/T100000132?year'+str(now.year)+'&month='+'6'+'&date='+'7'+'&allergy=hidden')
      school_menu = json.loads(response.text)
      menu = school_menu['menu'][0]
      lunch = menu['lunch']
      dinner = menu['dinner']
      # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
      return render_template('/main/index.html',lunchDataHtml=lunch,dinnerDataHtml=dinner)