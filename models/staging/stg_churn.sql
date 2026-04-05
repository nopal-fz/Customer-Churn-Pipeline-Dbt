with source as (

    select * 
    from {{ source('churn_source', 'raw_churn') }}

),

cleaned as (

    select
        customerid,

        lower(gender) as gender,

        tenure,
        monthlycharges,

        nullif(trim(totalcharges), '')::float as totalcharges,

        lower(contract) as contract,

        case 
            when churn = 'Yes' then 1
            else 0
        end as churn

    from source

)

select * from cleaned