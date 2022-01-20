from common.const.KEY_NAME import KEY_NAME, OTHER_KEY_NAME

class ShareSearchInHeaderFormatter:

    @staticmethod
    def create_share_into_search_fmt(share_infos):
        try:
            result = []
            for share_info in share_infos:
                result.append({
                    OTHER_KEY_NAME['TYPE']: OTHER_KEY_NAME['SHARE'],
                    OTHER_KEY_NAME['TARGET']: f"{share_info[KEY_NAME['SHARE_CODE']]}:{share_info[KEY_NAME['SHARE_NAME']]}",
                    KEY_NAME['SHARE_CODE']: share_info[KEY_NAME['SHARE_CODE']],
                    KEY_NAME['SHARE_NAME']: share_info[KEY_NAME['SHARE_NAME']]
                })

            return result

        except Exception as e:
            raise e

    @staticmethod
    def create_market_into_search_fmt(market_infos):
        try:
            result = []
            for market_info in market_infos:
                result.append({
                    OTHER_KEY_NAME['TYPE']: OTHER_KEY_NAME['MARKET'],
                    OTHER_KEY_NAME['TARGET']: f"{market_info[KEY_NAME['MARKET_CODE']]}:{market_info[KEY_NAME['MARKET_NAME']]}",
                    KEY_NAME['MARKET_CODE']: market_info[KEY_NAME['MARKET_CODE']],
                    KEY_NAME['MARKET_NAME']: market_info[KEY_NAME['MARKET_NAME']]
                })

            return result

        except Exception as e:
            raise e
