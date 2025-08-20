DELETE f 
FROM indicator_to_mo_fact f
JOIN indicator_to_mo m ON f.indicator_to_mo_id = m.indicator_to_mo_id
JOIN indicator i ON m.indicator_id = i.indicator_id
WHERE i.indicator_id = 273 
  AND DATE(f.fact_time) = '2024-09-10';
