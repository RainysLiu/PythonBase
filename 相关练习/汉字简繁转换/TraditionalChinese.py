from langconv import *

def Simplifiedto_to_Traditional(sentence):
    '''
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    '''
    sentence = Converter('zh-hant').convert(sentence)
    return sentence
def Traditional_to_Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

if __name__=="__main__":
    while True:
        simplified_sentence = input('请输入简体汉字：')
        traditional_sentence = Simplifiedto_to_Traditional(simplified_sentence)
        print('對應的繁體漢字：'+traditional_sentence)
        c=input('继续转换请按1 结束程序请按任意...\n')
        if c==1:
            pass
        else:
            break
