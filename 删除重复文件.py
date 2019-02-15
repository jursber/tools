import os,sys
import hashlib
import pandas as pd

#计算md5值
def get_md5(filename):   
    with open(filename,'rb') as f:
    	hash=hashlib.md5(f.read()).hexdigest()
    return hash

#获取文件夹内的全部文件信息
def get_file_info(path=None):      
	if path==None:
		path=sys.path[0]
	dir=os.walk(path)
	file_info_array=[]  #[[文件名，md5，文件路径],……]
	for folder in dir :
		for sub_folder in folder[2]:
			file_name=sub_folder
			file_path=os.path.join(folder[0],sub_folder)
			#print(sub_folder)
			file_md5=get_md5(file_path)

			file_info_array.append([file_name,file_md5,file_path])
	#print(file_info_array)
	print('\n=========================\n')
	return file_info_array

#查找重复文件
def redundant_files(paths):
	paths=pd.DataFrame(paths)
	paths.columns=['name','md5','path']
	paths['len']=paths['name'].apply(len)
	paths=paths.sort_values('len',ascending=True) #文件名比较长的排后头，优先删除
	redundant_judge=paths.duplicated(subset='md5')
	#print(redundant_judge)
	#print(paths)
	del_path_array=paths[redundant_judge] #[[文件名，md5，文件路径,文件名长度],……]
	#print(del_path_array)
	return del_path_array

#删除重复文件
def del_files(paths):
	total_size=0
	if paths.shape[0]==0:
		print('未发现重复文件！')
	else:
		for index,row in paths.iterrows():
			print(row['name'])
			total_size+=os.path.getsize(row['path'])
		confirm=input('\n以上文件将被删除，共计{}Mb，确认请输入\'yes\': '.format(round(total_size/1024/1024,2)))
		if confirm=='yes':
				for index,row in paths.iterrows():
					os.remove(row['path'])
					print('正在删除：',row['name'])
				print('\n=====================================\n重复文件已被删除\n=====================================\n')
		else:
			print('没有删除任何文件，程序退出')


def main():
	try:
		path=sys.argv[1]
	except:
		path=None
	file_info=get_file_info(path)
	del_files_path=redundant_files(file_info)
	del_files(del_files_path)


if __name__ == '__main__':
	main()