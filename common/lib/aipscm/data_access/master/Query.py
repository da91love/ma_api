class Query():
    sql_select_item = """

        WITH m_item_comment AS (
                 select item_key,
                        comment
                 from core_engine_test.item_comment
                 where (item_key, created_at) in (
                     select item_key, max(created_at)
                     from core_engine_test.item_comment
                     group by item_key
                 )
            ) ,
			/* maker_category用のI18nテーブル*/
			maker_category_i18n_translator As (
				select mst.item_group_cd, COALESCE(tgt.name, mst.name) as maker_category_i18n
				from (select * from core_engine_test.m_item_group_i18n where language_cd = 'en') as mst
				left join
					 (select * from core_engine_test.m_item_group_i18n where language_cd = '{lang}') as tgt
				on mst.item_group_cd = tgt.item_group_cd
			) ,
            maker AS (
                SELECT type1.item_group_cd, type2.item_group_cd AS maker_cd
				FROM (SELECT item_group_cd,item_group_type , parent_group_cd FROM core_engine_test.m_item_group WHERE item_group_type = '1') AS type1
					LEFT OUTER JOIN (SELECT item_group_cd,item_group_type , parent_group_cd FROM core_engine_test.m_item_group WHERE item_group_type = '2') AS type2
						ON type1.parent_group_cd = type2.item_group_cd
                where type2.item_group_type = '2'
            ) ,
			/* 国際化されたMakerテーブル*/
			maker_i18n AS (
				SELECT maker.*, maker_category_i18n_translator.maker_category_i18n as maker_cd_i18n
				FROM maker
				JOIN maker_category_i18n_translator
					on maker.maker_cd = maker_category_i18n_translator.item_group_cd
			) ,
            category AS (
                SELECT type1.item_group_cd, type3.item_group_cd AS category_cd
				FROM (SELECT item_group_cd,item_group_type , parent_group_cd FROM core_engine_test.m_item_group WHERE item_group_type = '1') AS type1
					LEFT OUTER JOIN (SELECT item_group_cd,item_group_type , parent_group_cd FROM core_engine_test.m_item_group WHERE item_group_type = '3') AS type3
					ON type1.parent_group_cd = type3.item_group_cd
                where type3.item_group_type = '3'
            ) ,
			/* 国際化されたCategoryテーブル*/
			category_i18n AS (
				SELECT category.*, maker_category_i18n_translator.maker_category_i18n as category_cd_i18n
				FROM category
				JOIN maker_category_i18n_translator
					on category.category_cd = maker_category_i18n_translator.item_group_cd
			)


        SELECT m_item.item_key,
               m_item.closing_day,
               m_item.image_url,
               m_item.stockout_flag,
               m_item.item_group_cd,
               m_item_comment.comment,
               maker_i18n.maker_cd,
			   maker_i18n.maker_cd_i18n,
               category_i18n.category_cd,
			   category_i18n.category_cd_i18n
        FROM core_engine_test.m_item AS m_item
        LEFT OUTER JOIN m_item_comment
        ON m_item_comment.item_key = m_item.item_key
        LEFT OUTER JOIN maker_i18n
        ON m_item.item_group_cd = maker_i18n.item_group_cd
        LEFT OUTER JOIN category_i18n
        ON m_item.item_group_cd = category_i18n.item_group_cd

    """
