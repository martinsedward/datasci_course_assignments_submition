/* frequency(docid, term, count) */
-- select count(*) from frequency where docid = "10398_txt_earn"
-- select count(term) from frequency where docid = "10398_txt_earn" and count = 1;
-- select count(*)
-- from(
--   select term
--   from frequency 
--   where docid = "10398_txt_earn" and count = 1
--   union
--   select term
--   from frequency 
--  where docid = "925_txt_trade" and count = 1
-- ) x
-- ;
-- select count(*) from frequency where term = "parliament";
-- select count(*) from (
-- select sum(count) as count_term  from frequency group by docid having count_term > 300);
-- select count(*) from frequency where term = "transactions" and docid in(
-- select distinct(docid) from frequency where term = "world");
/* A(row_num, col_num, value), B(row_num, col_num, value) */

SELECT A1.row_num, A2.col_num
  FROM A AS A1, A AS A2
  WHERE A1.col_num = A2.row_num
  GROUP BY A1.row_num, A2.col_num;




