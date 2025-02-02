SELECT *
FROM {{ source('staging', 'telegram_messages') }}
WHERE message_date < now() - INTERVAL '365 days'