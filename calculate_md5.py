import hashlib
#文件位置中的路径，用双反斜杠
file = 'fastspeech2_vctk_ckpt_1.2.0.zip'
md5file=open(file,'rb')
md5=hashlib.md5(md5file.read()).hexdigest()
md5file.close()
print(md5)
