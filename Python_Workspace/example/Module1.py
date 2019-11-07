#import time
#def lots_for_time(max):
#    t1=time.time()
#    for x in range(0,max):
#        print(x)
#        time.sleep(1)
#    t2=time.time()
#    print("it took %s" % (t2-t1))
#lots_for_time(100)

import pickle
game_data = {'player_position': 'N43 E23',
             'pockets': ['apple','knife','keys'],
             'backpack': ['rope','stone'],
             'money': 185}
save_file = open("C:\\Users\\b\\Desktop\\新建文本文档.txt",'wb')
pickle.dump(game_data,save_file)
save_file.close()
load_file = open("C:\\Users\\b\\Desktop\\新建文本文档.txt",'rb')
data = pickle.load(load_file)
print(data)
load_file.close()
