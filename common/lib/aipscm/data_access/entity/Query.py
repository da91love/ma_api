class Query():
    sql_insert_entity = """
    insert into core_engine_test.entity (
        item_key,
        location_key,
        period_key,
        entity_cd,
        candidate_cd,
        stage_cd,
        adjustment_cd,
        value,
        value_type,
        created_by
        )
    values (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        )
    """