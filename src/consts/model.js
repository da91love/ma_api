import {KEY_NAME, OTHER_KEY_NAME} from './keyName';

export const MODELS = {
    VALUE: 'value',
    TURNAROUND: 'turnaround',
    CPGROWTH: 'cpgrowth',
    MRKGROWTH: 'mrkgrowth',
    COLLAPSE: 'collapse',
    BLUECHIP: 'bluechip'
}

export const MODEL_NAME = {
    VALUE: 'Value Stock Model',
    TURNAROUND: 'Turnaround Stock Model',
    CPGROWTH: 'CpGrowth Stock Model',
    MRKGROWTH: 'MrkGrowth Stock Model',
    COLLAPSE: 'Collapse Stock Model',
    BLUECHIP: 'Bluechip Stock Model'
}

export const MODEL_TABLE_COL = {
    VALUE: [KEY_NAME.PERIOD, KEY_NAME.SHARE_NAME, KEY_NAME.MARKET_NAME, KEY_NAME.MV, KEY_NAME.SALES, KEY_NAME.OP, KEY_NAME.NP_CTRL, KEY_NAME.PER, KEY_NAME.ROE, OTHER_KEY_NAME.GRAPH],
    TURNAROUND: [KEY_NAME.PERIOD, KEY_NAME.SHARE_NAME, KEY_NAME.MARKET_NAME, KEY_NAME.MV, KEY_NAME.SALES, KEY_NAME.OP, KEY_NAME.NP_CTRL, OTHER_KEY_NAME.GRAPH],
    CPGROWTH: [KEY_NAME.PERIOD, KEY_NAME.SHARE_NAME, KEY_NAME.MARKET_NAME, KEY_NAME.MV, KEY_NAME.SALES, KEY_NAME.OP, KEY_NAME.NP_CTRL, OTHER_KEY_NAME.GRAPH],
    MRKGROWTH: [KEY_NAME.PERIOD, KEY_NAME.SHARE_NAME, KEY_NAME.MARKET_NAME, KEY_NAME.MV, KEY_NAME.SALES, KEY_NAME.OP, KEY_NAME.NP_CTRL, OTHER_KEY_NAME.GRAPH],
    COLLAPSE: [KEY_NAME.PERIOD, KEY_NAME.SHARE_NAME, KEY_NAME.MARKET_NAME, KEY_NAME.MV, KEY_NAME.SALES, KEY_NAME.OP, KEY_NAME.NP_CTRL, OTHER_KEY_NAME.GRAPH],
    BLUECHIP: [KEY_NAME.PERIOD, KEY_NAME.SHARE_NAME, KEY_NAME.MARKET_NAME, KEY_NAME.MV, KEY_NAME.SALES, KEY_NAME.OP, KEY_NAME.NP_CTRL, KEY_NAME.PER, KEY_NAME.ROE, OTHER_KEY_NAME.GRAPH],
}

export const MODEL_HIT_TABLE_COL = [KEY_NAME.PERIOD, KEY_NAME.SHARE_NAME, OTHER_KEY_NAME.SCORE, KEY_NAME.MV, KEY_NAME.SALES, MODELS.VALUE, MODELS.TURNAROUND, MODELS.CPGROWTH, MODELS.COLLAPSE, MODELS.BLUECHIP, OTHER_KEY_NAME.GRAPH]

export const GRAPH_ANALYSIS_COL = [
    "시가총액",
    "매출액",
    "영업이익",
    "당기순이익(지배)",
    "PSR(배)",
    "POR(배)",
    "PER(배)",
    "PCR(배)",
    "PBR(배)",
]
