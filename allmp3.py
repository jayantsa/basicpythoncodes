import os
def find_all(folder):
  os.chdir(folder)
  list=os.listdir()
  for item in list:
    print(item)
    if(os.path.isdir(folder+"/"+item)):
      find_all(folder+"/"+item)
      continue;
    name_split=item.split('.')
    if(len(name_split)>1 and name_split[-1]=='mp3'):
      file=open('/home/jayant/mysongs','w')
      file.write(item)
      file.close()
  os.chdir('..')

find_all('/media/jayant/OS/jayant/songs')
