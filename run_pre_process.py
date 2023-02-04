from pre_process.create_summary_data_wrapper import create_summary_data_wrapper
from pre_process.create_market_summary_data_wrapper import create_market_summary_data_wrapper
from pre_process.create_gdp_data import create_gdp_data

def run_pre_process():
    create_gdp_data()
    create_market_summary_data_wrapper()
    create_summary_data_wrapper()