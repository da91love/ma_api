from enum import Enum


class EntitySum(Enum):
    TOTAL_SALES_PLAN: str = 'TOTAL_SALES_PLAN'
    TOTAL_SITE_SALES: str = 'TOTAL_SITE_SALES'
    TOTAL_ORDER: str = 'TOTAL_ORDER'
    TOTAL_ARRIVAL_PLAN: str = 'TOTAL_ARRIVAL_PLAN'
    WAREHOUSE_DELIVERY: str = 'WAREHOUSE_DELIVERY'
    TOTAL_ARRIVAL_PLAN_FIXED: str = 'TOTAL_ARRIVAL_PLAN_FIXED'
