class Query():
    sql_translate = """
        select mst.{key_name}, COALESCE(tgt.name, mst.name) as {key_name}_i18n
        from (select * from core_engine_test.{table_name} where language_cd = 'en') as mst
        left join
             (select * from core_engine_test.{table_name} where language_cd = '{lang}') as tgt
        on mst.{key_name} = tgt.{key_name}
    """