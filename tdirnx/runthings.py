#%%
from crib import app
# #%%
# from downloader import download
# from compmap import compmap
# import os
# #%%
# def gettopics():
#     topic = os.environ['topic']
#     topics = [u for u in topic.split('/') if u != '']
#     #print(topics)
#     return topics

# def getsometopics(topics):
#     #count=0
#     curres = []
#     #stopiter = 1
#     #lt = len(topics)
#     a = 5
#     # try:
#     for x in topics:
#             #print(f"i:{i}")
#         curres.append(x)
#         #else:
#             #   raise StopIteration
#         #if i % a==0 and i != 0:
#     return curres
#     #             curres.clear()
            
            

#     # except StopIteration:
#     #     print('stopiteration1')

        
# #%%       
    
# def getld(topics):
    
#     c = compmap(mktransfunc,topics)
#     c.start_threads()
#     cres = c.get_results()
#     print(cres)
#     #x = download(topic, 
#      #            output_dir="./Downloads/lt", limit=25, timeout=1)
#     return cres

# def mktransfunc(topic):
#     #print('making func')
#     def transfunc():
#         #data = getld(topic)
#         data = download(topic, output_dir="./Downloads/", limit=45, timeout=1)
#         res = topic
#         return res
#     return transfunc

# cresa = None
# topics = list(gettopics())
# #topics = list(gettopics())
# print(topics)
# cresa = getld(topics)

#%%

app.env="development"
app.run(debug=True,host='0.0.0.0')

# %%
