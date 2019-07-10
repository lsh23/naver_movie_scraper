from naver_movie_scraper import scrap_comments


idx = 159000
pos_tag_count = 0
nag_tag_count = 0


len(scrap_list_of_dict)

for i in range(10):
    scrap_list_of_dict = scrap_comments(idx, limit=100)
    with open('./result/'+str(idx)+'_result.txt','w',encoding='utf-8') as f:
        for dict in scrap_list_of_dict:
            user_id = dict['user']
            score = int(dict['score'])
            text = dict['text']
            if score > 8:
                pos_or_nag_tag = "1"
                pos_tag_count = pos_tag_count + 1
                f.write('\\t'.join([user_id,text,pos_or_nag_tag])+'\n')
            elif score < 5:
                pos_or_nag_tag = "0"
                nag_tag_count = nag_tag_count + 1
                f.write('\\t'.join([user_id,text,pos_or_nag_tag])+'\n')
            else:
                continue
    idx = idx + 1


print(pos_tag_count)
print(nag_tag_count)
