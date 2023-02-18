import datetime

from common.util.config_get import get_config
from common.AppBase import AppBase
from common.lib.ma.data_access.system.AccessService import AccessService
from common.type.Errors import AuthenticationException
from common.const.API_PATH import *
from .type.Res_type import ResType

# import boto3
import csv
import json
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
api_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
sys.path.append(api_root)

# import module
import requests
import pydash as _

# Create instance
config = get_config()
now = datetime.datetime.now()
# s3 = boto3.client(
#     's3',
#     aws_access_key_id=config['S3']['aws_access_key_id'],
#     aws_secret_access_key=config['S3']['aws_secret_access_key'],
# )

# get config data
s3_bucket_name = config['S3']['s3_bucket_name']


@AppBase
def lambda_handler(event, context=None) -> ResType:

    """
    lambda_handler : This functions will be implemented in lambda
    : param event: (dict)
    : param context: (dict)
    : serviceKey: (string) 공공데이터포털에서 받은 인증키
    : numOfRows: (integer) 한 페이지 결과 수
    : pageNo: (integer) 페이지 번호
    : resultType: (string) 구분(xml, json) Default: xml
    : basDt: (string) 검색값과 기준일자가 일치하는 데이터를 검색
    : beginBasDt: (string) 기준일자가 검색값보다 크거나 같은 데이터를 검색
    : endBasDt: (string) 기준일자가 검색값보다 작은 데이터를 검색
    : likeBasDt: (string) 기준일자값이 검색값을 포함하는 데이터를 검색
    : likeSrtnCd: (string) 단축코드가 검색값을 포함하는 데이터를 검색
    : isinCd: (string) 검색값과 ISIN코드이 일치하는 데이터를 검색
    : likeIsinCd: (string) ISIN코드가 검색값을 포함하는 데이터를 검색
    : itmsNm: (string) 검색값과 종목명이 일치하는 데이터를 검색
    : likeItmsNm: (string) 종목명이 검색값을 포함하는 데이터를 검색
    : mrktCls: (string) 검색값과 시장구분이 일치하는 데이터를 검색
    : beginVs: (string) 대비가 검색값보다 크거나 같은 데이터를 검색
    : endVs: (string) 대비가 검색값보다 작은 데이터를 검색
    : beginFltRt: (string) 등락률이 검색값보다 크거나 같은 데이터를 검색
    : endFltRt: (string) 등락률이 검색값보다 작은 데이터를 검색
    : beginTrqu: (string) 거래량이 검색값보다 크거나 같은 데이터를 검색
    : endTrqu: (string) 거래량이 검색값보다 작은 데이터를 검색
    : beginTrPrc: (string) 거래대금이 검색값보다 크거나 같은 데이터를 검색
    : endTrPrc: (string) 거래대금이 검색값보다 작은 데이터를 검색
    : beginLstgStCnt: (string) 상장주식수가 검색값보다 크거나 같은 데이터를 검색
    : endLstgStCnt: (string) 상장주식수가 검색값보다 작은 데이터를 검색
    : beginMrktTotAmt: (string) 시가총액이 검색값보다 크거나 같은 데이터를 검색
    : return: (dict)
    """

    # Get data from API Gateway
    header = event.get('header')
    auth_id = header.get('authId')
    service_key = (config.get('AUTH')).get('FSC_OPEN_API')
    num_of_rows = (event.get('params')).get('numOfRows')
    page_no = (event.get('params')).get('pageNo')
    result_type = (event.get('params')).get('resultType') or "json"
    bas_dt = (event.get('params')).get('basDt')
    begin_bas_dt = (event.get('params')).get('beginBasDt')
    end_bas_dt = (event.get('params')).get('endBasDt')
    like_bas_dt = (event.get('params')).get('likeBasDt')
    like_srtn_cd = (event.get('params')).get('shareCode')
    is_in_cd = (event.get('params')).get('isinCd')
    like_is_in_cd = (event.get('params')).get('likeIsinCd')
    itms_nm = (event.get('params')).get('itmsNm')
    like_itms_nm = (event.get('params')).get('likeItmsNm')
    mrkt_cls = (event.get('params')).get('mrktCls')
    begin_vs = (event.get('params')).get('beginVs')
    end_vs = (event.get('params')).get('endVs')
    begin_flt_rt = (event.get('params')).get('beginFltRt')
    end_flt_rt = (event.get('params')).get('endFltRt')
    begin_trqu = (event.get('params')).get('beginTrqu')
    end_trqu = (event.get('params')).get('endTrqu')
    begin_tr_prc = (event.get('params')).get('beginTrPrc')
    end_tr_prc = (event.get('params')).get('endTrPrc')
    begin_lstg_st_cnt = (event.get('params')).get('beginLstgStCnt')
    end_lstg_st_cnt = (event.get('params')).get('endLstgStCnt')
    begin_mrkt_tot_amt = (event.get('params')).get('beginMrktTotAmt')
    end_mrkt_tot_amt = (event.get('params')).get('endMrktTotAmt')


    res = requests.get(FSC_OPEN_API_GET_STOCK_PRICE_INFO_URL, params={
        "serviceKey": service_key,
        "numOfRows": num_of_rows,
        "pageNo": page_no,
        "resultType": result_type,
        "basDt": bas_dt,
        "beginBasDt": begin_bas_dt,
        "endBasDt": end_bas_dt,
        "likeBasDt": like_bas_dt,
        "likeSrtnCd": like_srtn_cd,
        "isinCd": is_in_cd,
        "likeIsinCd": like_is_in_cd,
        "itmsNm": itms_nm,
        "likeItmsNm": like_itms_nm,
        "mrktCls": mrkt_cls,
        "beginVs": begin_vs,
        "endVs": end_vs,
        "beginFltRt": begin_flt_rt,
        "endFltRt": end_flt_rt,
        "beginTrqu": begin_trqu,
        "endTrqu": end_trqu,
        "beginTrPrc": begin_tr_prc,
        "endTrPrc": end_tr_prc,
        "beginLstgStCnt": begin_lstg_st_cnt,
        "endLstgStCnt": end_lstg_st_cnt,
        "beginMrktTotAmt": begin_mrkt_tot_amt,
        "endMrktTotAmt": end_mrkt_tot_amt,
    })

    json_res = res.json()
    result = (((json_res.get('response')).get('body')).get('items')).get('item')

    return ResType(value=result).get_response()

