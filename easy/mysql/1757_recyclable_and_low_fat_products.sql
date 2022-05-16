# Write your MySQL query statement below
select
  p.product_id
from
  Products p
where
  low_fats = 'Y'
  and recyclable = 'Y'