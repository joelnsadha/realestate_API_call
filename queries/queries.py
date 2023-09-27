
staging_table = """
    CREATE TABLE t_stg_realestate (
        id BIGINT PRIMARY KEY NOT NULL,
        user_id BIGINT,
        user_phone TEXT,
        title TEXT,
        region TEXT,
        location TEXT,
        price BIGINT,
        bedroom BIGINT,
        bathroom BIGINT
    )
"""

price_conversion_func = """
    CREATE OR REPLACE FUNCTION stg_jiji.price_in_millions(old_price INT)
        RETURNS NUMERIC
        LANGUAGE PLPGSQL
    AS
    $$
    DECLARE 
        new_price NUMERIC;
    BEGIN
        SELECT(old_price/1000000)::NUMERIC(19,2) INTO new_price;
        RETURN new_price;
    END;
    $$
"""

view_avg_beds_baths_price_by_location = """
    -- AVERAGE BEDROOMS BATHROOMS AND PRICE BY LOCATION
    
    CREATE VIEW public.v_avg_price_by_location
    SELECT
            ss.location,
            ROUND(AVG(ss.bedroom),0) AS avg_bedrooms,
            ROUND(AVG(ss.bathroom),0) AS avg_bathrooms,
            ROUND((ss.price/1000000)::NUMERIC(19,2),0) AS avg_price_millions
        FROM public.t_stg_realestate ss
        GROUP BY ss.location, ROUND((ss.price/1000000)::NUMERIC(19,2),0)
        ORDER BY ROUND((ss.price/1000000)::NUMERIC(19,2),0) DESC;
"""

view_avg_price_by_location = """
    --AVERAGE PRICE BY LOCATION
    
    CREATE OR REPLACE VIEW avg_price_by_location AS 
    SELECT
        location,
        ROUND(AVG(stg_re.price_in_millions(ss.price)),0) AS avg_price_millions
    FROM public.t_stg_realestate ss
    GROUP BY location
    ORDER BY avg_price_millions DESC;
"""

view_total_lsitings_by_location = """
    -- TOTAL LISTINGS BY LOCATION
    
    CREATE VIEW v_total_listings_by_location AS 
    SELECT
        location,
        COUNT(id) AS total_listings
    FROM public.t_stg_realestate ss
    GROUP BY location
    ORDER BY total_listings DESC;
"""

view_total_listings_by_user = """
    -- TOTAL LISTINGS BY USER
    
    CREATE VIEW v_total_listings_by_user AS 
    SELECT
        user_id,
        COUNT(id) AS total_listings
    FROM public.t_stg_realestate ss
    GROUP BY user_id
    ORDER BY total_listings DESC
"""
