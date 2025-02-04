WITH raw_data AS (
    SELECT 
        message_id,
        channel_title,
        channel_username,
        message,
        message_date::timestamp AS message_date,  -- Cast message_date to timestamp
        CASE
            WHEN media_path = 'no media' THEN NULL  -- Convert 'no media' to NULL
            ELSE media_path
        END AS media_path,
        CASE 
            WHEN emoji_used = 'no emoji' THEN NULL  -- Convert 'no emoji' to NULL
            ELSE emoji_used
        END AS emoji_used,
        CASE 
            WHEN youtube_links = 'no link' THEN NULL  -- Convert 'no link' to NULL
            ELSE youtube_links
        END AS youtube_links
    FROM {{ source('staging', 'telegram_messages') }}  -- Reference the source data directly
)
SELECT 
    message_id,
    channel_title,
    channel_username,
    message,
    message_date,
    media_path,
    emoji_used,
    youtube_links
FROM raw_data
WHERE message_date > now() - INTERVAL '450 days'
