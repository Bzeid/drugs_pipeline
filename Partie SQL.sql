Partie SQL:
Requête question 1:

select date, SUM(prod_price*prod_qty) as 'ventes'
from transactions 
WHERE date BETWEEN DATE('2019-01-01') AND DATE('2019-12-31')
group by date
ORDER BY date



Requête question 2:

SELECT t1.client_id, t1.ventes_deco, t2.ventes_meubles
FROM 
(select client_id, SUM(prod_price*prod_qty) as 'ventes_deco'
from transactions JOIN
     product_nomenclature 
     ON transactions.prop_id = product_nomenclature.product_id 
WHERE (date BETWEEN DATE('2019-01-01') AND DATE('2019-12-31')) AND product_type = 'DECO'
group by client_id) t1
LEFT JOIN
(select client_id, SUM(prod_price*prod_qty) as 'ventes_meubles'
from transactions JOIN
     product_nomenclature 
     ON transactions.prop_id = product_nomenclature.product_id 
WHERE (date BETWEEN DATE('2019-01-01') AND DATE('2019-12-31')) AND product_type = 'MEUBLE'
group by client_id) t2
ON (t1.client_id = t2.client_id)
ORDER BY t1.client_id DESC
