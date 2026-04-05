select
    customerid,

    tenure,
    monthlycharges,
    totalcharges,

    -- feature engineering
    case 
        when tenure < 12 then 'new'
        when tenure < 24 then 'mid'
        else 'long'
    end as tenure_group,

    churn

from {{ ref('stg_churn') }}