# 进度提示
import math

def rep_progress(current_progress, max_progress, *other_info,**display_control):
    MAX_LEN_REF = 30 #进度条在屏幕上的最大长度
    TIME_SPLIT = math.ceil(max_progress/MAX_LEN_REF) #单位长度对应的数值
    max_len=int(max_progress/TIME_SPLIT) #真实的最大长度（取整之后）
    progress_per=current_progress/max_progress
    progress_i=int(round(current_progress/TIME_SPLIT*2,0)) #当前长度取整
    i,is_odd=divmod(progress_i,2)

    if i>=max_len: #舍入错误，补丁
        i=max_len
        is_odd=0

    display='█'*(i)+'▌'*is_odd+'..'*(max_len-i-is_odd)

    info_join='' #处理*other_info的内容
    if len(other_info) !=0:
        for info_index in range(len(other_info)):
            info_join=info_join+' '+str(other_info[info_index])

    if ('head' in display_control.keys()): #处理**display_control的内容
        head=display_control['head']
    else:
        head='已完成'

    display_dict={'head':head,'per':progress_per,'other_info':info_join,'display':display}
    print('\r{head} {per:7.2%}: |{display}| {other_info}'.format(**display_dict), end="")
    #print(max_len,i,is_odd,max_len-i-is_odd)

if __name__ == '__main__':
	import random,time
	for i in range(1001):
	    time.sleep(0.0001)
	    rep_progress(i,1000,round(random.uniform(0,i),2))
	print('')
	for i in range(1001):
	    time.sleep(0.009)
	    rep_progress(i,1000,round(random.uniform(0,i),2),head='正在完成')
	print('')
	for i in range(2001):
	    time.sleep(0.001)
	    rep_progress(i,2000,round(random.uniform(0,i),2),'无数据',i*i,head='')
	print('')
	for i in range(21):
	    time.sleep(0.01)
	    rep_progress(i,20,round(random.uniform(0,i),2),'test')
	print('')
	#▌▇█▌