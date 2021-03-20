import {KEY_NAME, OTHER_KEY_NAME} from './keyName';

export const MODELS = {
    VALUE: 'value',
    TURNAROUND: 'turnaround',
    CPGROWTH: 'cpgrowth',
    MRKGROWTH: 'mrkgrowth',
    COLLAPSE: 'collapse',
    BLUECHIP: 'bluechip',
    INVGROWTH: 'invgrowth'
}

export const MODEL_NAME = {
    VALUE: 'Value Stock Model',
    TURNAROUND: 'Turnaround Stock Model',
    CPGROWTH: 'CpGrowth Stock Model',
    MRKGROWTH: 'MrkGrowth Stock Model',
    COLLAPSE: 'Collapse Stock Model',
    BLUECHIP: 'Bluechip Stock Model',
    INVGROWTH: 'Investment Growth Stock Model',
}

/**
 * MARKET데이터는 rawData에서 따로 가공해야 하기 때문에, 키명을 rawData대로 하지 않고 따로 정의함
 * MRKGROWTH모델의 MODEL_TABLE_COL과 GRAPH_ANALYSIS_COL의 keyname은 아래의 keyname에 포함되어야함
 */
export const MKRGROWTH_MODEL_RAWDATA_KEYNAME = [
    KEY_NAME.PERIOD, 
    KEY_NAME.MARKET_NAME,
    KEY_NAME.MARKET_CODE,
    OTHER_KEY_NAME.NUM_OF_CP,
    KEY_NAME.MV, 
    KEY_NAME.SALES, 
    KEY_NAME.OP, 
    KEY_NAME.NP_CTRL,
    KEY_NAME.PSR,
    KEY_NAME.POR,
    KEY_NAME.PER,
    KEY_NAME.PCR,
    KEY_NAME.PBR,
]

export const BY_SHARE_DEFAULT_GRAPH_TYPE = [
    KEY_NAME.MV,
    KEY_NAME.SALES,
    KEY_NAME.OP,
    KEY_NAME.NP_CTRL,
    KEY_NAME.PSR,
    KEY_NAME.POR,
    KEY_NAME.PER,
    KEY_NAME.PCR,
    KEY_NAME.PBR,
    KEY_NAME.IA_CF,
]

export const BY_MRK_DEFAULT_GRAPH_TYPE = [
    OTHER_KEY_NAME.NUM_OF_CP,
    KEY_NAME.MV,
    KEY_NAME.SALES,
    KEY_NAME.OP,
    KEY_NAME.NP_CTRL,
    KEY_NAME.PSR,
    KEY_NAME.POR,
    KEY_NAME.PER,
    KEY_NAME.PCR,
    KEY_NAME.PBR,
]

export const FILTER_TYPE = {
    PERIOD: "periodFilter",
    TERM: "termFilter",
    PER_MIN: "perMinFilter",
    PER_MAX: "perMaxFilter",
    SALES_MIN: "salesMinFilter",
    ROE_MIN: "roeMinFilter",
    OP_TIMES: "opTimesFilter",
    IA_CF_TIMES: "iaCfTimesFilter",
    MV_TIMES: "mvTimesFilter"
}

export const BY_SHARE_ALL_GRAPH_TYPE = [
    KEY_NAME.MV,
    KEY_NAME.SALES,
    KEY_NAME.SALES_VAR,
    KEY_NAME.OP,
    KEY_NAME.OP_VAR,
    KEY_NAME.OP_PUB,
    KEY_NAME.OP_CNTN,
    KEY_NAME.NP,
    KEY_NAME.NP_CTRL,
    KEY_NAME.NP_VAR,
    KEY_NAME.NP_NCTRL,
    KEY_NAME.ASST,
    KEY_NAME.DBT,
    KEY_NAME.CPTL,
    KEY_NAME.ASST_CTRL,
    KEY_NAME.ASST_NCTRL,
    KEY_NAME.CPTL,
    KEY_NAME.OA_CF,
    KEY_NAME.IA_CF,
    KEY_NAME.FA_CF,
    KEY_NAME.CAPEX,
    KEY_NAME.FCF,
    KEY_NAME.DBT_I,
    KEY_NAME.OPM,
    KEY_NAME.NPM,
    KEY_NAME.ROE,
    KEY_NAME.ROA,
    KEY_NAME.DBT_RATIO,
    KEY_NAME.CPTL_RATIO,
    KEY_NAME.PCR,
    KEY_NAME.PSR,
    KEY_NAME.POR,
    KEY_NAME.EPS,
    KEY_NAME.PER,
    KEY_NAME.BPS,
    KEY_NAME.PBR,
    KEY_NAME.CASH_DPS,
    KEY_NAME.DVD_YIELD,
    KEY_NAME.DVD_RATIO,
    KEY_NAME.SHARE_NUM
]

export const BY_MRK_ALL_GRAPH_TYPE = [
    OTHER_KEY_NAME.NUM_OF_CP,
    KEY_NAME.MV, 
    KEY_NAME.SALES, 
    KEY_NAME.OP, 
    KEY_NAME.NP_CTRL,
    KEY_NAME.PSR,
    KEY_NAME.POR,
    KEY_NAME.PER,
    KEY_NAME.PCR,
    KEY_NAME.PBR,
]