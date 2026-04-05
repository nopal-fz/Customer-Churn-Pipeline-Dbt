select
    customerid,
    gender,
    contract

from {{ ref('stg_churn') }}