tst = '{&quot;author&quot;:{&quot;user_id&quot;:400507232,&quot;user_name&quot;:&quot;pppphyhy&quot;,&quot;name_u&quot;:&quot;pppphyhy&amp;ie=utf-8&quot;,&quot;user_sex&quot;:1,&quot;portrait&quot;:&quot;60417070707068796879df17&quot;,&quot;is_like&quot;:0,&quot;level_id&quot;:1,&quot;level_name&quot;:&quot;\u5927\u4e00\u65b0\u751f&quot;,&quot;cur_score&quot;:0,&quot;bawu&quot;:0,&quot;props&quot;:null},&quot;content&quot;:{&quot;post_id&quot;:66074902477,&quot;is_anonym&quot;:false,&quot;open_id&quot;:&quot;tieba&quot;,&quot;open_type&quot;:&quot;&quot;,&quot;date&quot;:&quot;2015-03-25 13:56&quot;,&quot;vote_crypt&quot;:&quot;&quot;,&quot;post_no&quot;:43,&quot;type&quot;:&quot;0&quot;,&quot;comment_num&quot;:8,&quot;ptype&quot;:&quot;0&quot;,&quot;is_saveface&quot;:false,&quot;props&quot;:null,&quot;post_index&quot;:10,&quot;pb_tpoint&quot;:null}}'

if '&quot;' in tst:
    tst = tst.replace('&quot;', '"')
    import json
    tst1 = json.loads(tst)
    print(1)