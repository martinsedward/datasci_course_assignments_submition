/* frequency(docid, term, count) */
-- select count(*) from frequency where docid = "10398_txt_earn"
-- select count(term) from frequency where docid = "10398_txt_earn" and count = 1;

select count(term) from frequency where docid = "10398_txt_earn" and count = 1
UNION
select count(term) from frequency where docid = "925_txt_trade" and count = 1;