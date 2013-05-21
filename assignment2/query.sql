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
-- select sum(Count_term) from (select count(term) AS 'Count_term' from frequency group by docid having count(term) > 300) as a;
-- You've probably got the group by and the filter correct, but remember that you need to add up the term frequencies rather than just count the terms.


select count(docid) from (
select docid, sum(term) AS sum_term  from frequency group by docid having sum_term >= 300);

