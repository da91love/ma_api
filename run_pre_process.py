from pre_process.create_summary_data_wrapper import create_summary_data_wrapper
from pre_process.create_market_summary_data_wrapper import create_market_summary_data_wrapper
from pre_process.create_gdp_data import create_gdp_data
from pre_process.create_mrkcap_data_wrapper import create_mrkcap_data_wrapper

# API에서 매회 연산하기에는 리소스가 아깝고, 한번 계산해 놓으면 쭉 사용할 수 있는 데이터 가공
def run_pre_process():
    create_mrkcap_data_wrapper()
    create_gdp_data()
    create_market_summary_data_wrapper()
    create_summary_data_wrapper()