import yaml

#打开yaml文件,验证类型和
# desired_caps = yaml.load(open("E:/VScode_word/yaml/GalaxyS8.yaml"))
# print(type(desired_caps))
# print(desired_caps)
desired_caps = yaml.load(open("E:/VScode_word/yaml/GalaxyS8.yaml"))
element = yaml.load(open('E:/VScode_word/yaml/element.yaml','r', encoding='UTF-8'))
# eth = yaml.load(open('E:/VScode_word/yaml/ETH_Private Key.yaml','r', encoding='UTF-8'))


# print(a.readlines())
# print(element)

for i,j in range(10):
    i = i+i
    j = j+1
    
    print(str("eth")+str(j))
    print(i)
# yaml 字典中的索引方法
# print(element['ivTabManage'])
# ivTabManage = "com.machain.mybitt:id/ivTabManage"
# print(ivTabManage)

# print(type(eth))
# print(eth)