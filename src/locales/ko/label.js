import { KEY_NAME, OTHER_KEY_NAME } from '../../consts/keyName';

export const KO_JSON = {
  "shareSearch": {
    "label": {
      "modelHitSummary": "모델매칭",
      "financialSummary": "회계요약",
      "valuation": "벨류에이션",
      "idcTrendLine": "주요지표추세선"
    },
  },
  "marketSearch": {},
  "target": {
    "addModel": "모델추가",
    "chooseModel": "모델을 선택해주세요",
    "noneSelectedModel": "모델이 선택되지 않았습니다",
  },
  "modelHit": {},
  "allShares": {},
  "compare": {
    "compareTgSave": "비교종목저장",
    "compareTgApply": "저장된 비교 그룹 적용",
    "insertCompareTgGroup": "저장할 비교 그룹명을 입력하세요"
  },
  "common": {
    "compare": {
      "compareTgShares": "compare target shares",
      "compareTgList": "선택된 비교 대상 종목",
      "noneSelectedCompareTg": "어떠한 비교대상 종목도 선택되지 않았습니다",
    },
    "navigator": {
      "bookmark": "bookmark",
      "bookmarkList": "저장된 북마크 리스트",
      "noneSelectedBookmark": "어떠한 북마크도 저장되지 않았습니다",
    },
    "header": {
      "shareSearch": "종목검색",
      "marketSearch": "마켓검색",
      "target": "모델 타게팅",
      "modelHit": "종목별 모델매칭",
      "allShares": "모든 종목 검색",
      "compare": "종목별 비교",
      "login": "로그인",
      "logout": "로그아웃",
    },
    "button": {
      "save": "저장",
      "remove": "삭제",
      "close": "닫기",
      "cancelAll": "모두취소",
      "selectIdc": "지표선택",
      "apply": "적용",
    },
    "tab": {
      "yearly": "년도별",
      "quarterly": "분기별",
    },
    "mainTitle": "Market Analysis",
    "rawData": {
      [KEY_NAME.PERIOD]: "기간",
      [KEY_NAME.SHARE_NAME]: "종목명",
      [KEY_NAME.SHARE_CODE]: "종목코드",
      [KEY_NAME.MARKET_NAME]: "마켓명",
      [KEY_NAME.MARKET_CODE]: "마켓코드",
      [KEY_NAME.EV]: "총기업가치",
      [KEY_NAME.MV]: "시가총액",
      [KEY_NAME.SALES]: "매출액",
      [KEY_NAME.SALES_VAR]: "매출변동(%)",
      [KEY_NAME.OP]: "영업이익",
      [KEY_NAME.OP_VAR]: "영익변동(%)",
      [KEY_NAME.OP_PUB]: "영업이익(발표기준)",
      [KEY_NAME.OP_CNTN]: "세전계속사업이익",
      [KEY_NAME.DA]: "감가상각비",
      [KEY_NAME.EBITDA]: "EBITDA",
      [KEY_NAME.NOPLAT]: "NOPLAT",
      [KEY_NAME.NP]: "당기순이익",
      [KEY_NAME.NP_CTRL]: "당기순이익(지배)",
      [KEY_NAME.NP_VAR]: "순이익변동(%)",
      [KEY_NAME.NP_NCTRL]: "당기순이익(비지배)",
      [KEY_NAME.ASST]: "자산총계",
      [KEY_NAME.LBLT]: "부채총계",
      [KEY_NAME.EQT]: "자본총계",
      [KEY_NAME.EQT_CTRL]: "자본총계(지배)",
      [KEY_NAME.EQT_NCTRL]: "자본총계(비지배)",
      [KEY_NAME.CMM_STC]: "자본금",
      [KEY_NAME.CFO]: "영업활동현금흐름",
      [KEY_NAME.CFI]: "투자활동현금흐름",
      [KEY_NAME.CFF]: "재무활동현금흐름",
      [KEY_NAME.CAPEX]: "CAPEX",
      [KEY_NAME.IC]: "IC",
      [KEY_NAME.FCF]: "FCF",
      [KEY_NAME.DBT_I]: "이자발생부채",
      [KEY_NAME.OPM]: "영업이익률(%)",
      [KEY_NAME.NPM]: "순이익률(%)",
      [KEY_NAME.EPM]: "EBITDA률(%)",
      [KEY_NAME.ROE]: "ROE(%)",
      [KEY_NAME.ROA]: "ROA(%)",
      [KEY_NAME.ROIC]: "ROIC(%)",
      [KEY_NAME.LBLT_RATIO]: "부채비율(%)",
      [KEY_NAME.EQT_RATIO]: "자본유보율(%)",
      [KEY_NAME.PCR]: "PCR(배)",
      [KEY_NAME.PSR]: "PSR(배)",
      [KEY_NAME.POR]: "POR(배)",
      [KEY_NAME.EPS]: "EPS(원)",
      [KEY_NAME.PER]: "PER(배)",
      [KEY_NAME.BPS]: "BPS(원)",
      [KEY_NAME.PBR]: "PBR(배)",
      [KEY_NAME['EV/EBITDA']]: "EV/EBITDA",
      [KEY_NAME.CASH_DPS]: "현금DPS(원)",
      [KEY_NAME.DVD_YIELD]: "현금배당수익률(%)",
      [KEY_NAME.DVD_RATIO]: "현금배당성향(%)",
      [KEY_NAME.SHARE_NUM]: "발행주식수(보통주)",
      [OTHER_KEY_NAME.GRAPH]: "그래프",
      [OTHER_KEY_NAME.SPS]: "SPS(원)",
      [OTHER_KEY_NAME.OPS]: "OPS(원)",
      [OTHER_KEY_NAME.PRICE]: "주가",
    }
  }
}