import os
import pandas as pd
import jieba
from snownlp import SnowNLP
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

def load_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        comments = file.readlines()
    return comments

def preprocess_comments(comments):
    preprocessed_comments = []
    for comment in comments:
        comment = comment.strip()
        if comment:
            preprocessed_comments.append(comment)
    return preprocessed_comments

def extract_feminism_sentences(comments):
    feminism_keywords = ['女性', '女权', '女强人', '性别', '平等', '独立', '女', '女性主义']
    relevant_sentences = []
    for comment in comments:
        for sentence in SnowNLP(comment).sentences:
            if any(keyword in sentence for keyword in feminism_keywords):
                relevant_sentences.append(sentence)
    return relevant_sentences

def generate_wordcloud(text, filename_prefix=''):
    wordcloud = WordCloud(
        width=1600,  # 增加图像宽度
        height=800,  # 增加图像高度
        background_color='white',
        font_path='/Library/Fonts/Arial Unicode.ttf',
        max_font_size=150  # 增加最大字体大小
    ).generate(" ".join(text))
    plt.figure(figsize=(20, 10))  # 调整图像大小
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(f"{filename_prefix}_wordcloud.png", dpi=300)  # 增加图像分辨率
    plt.close()

def summarize_comments(comments):
    nlp = SnowNLP(" ".join(comments))
    summary = nlp.summary(5)
    return summary

# 加载评论数据
huanlesong_comments = load_comments('/Users/zhangmengxin/Desktop/vscode/欢乐颂5comments.txt')
jintian_comments = load_comments('/Users/zhangmengxin/Desktop/vscode/今天的她们comments.txt')
yanhuo_comments = load_comments('/Users/zhangmengxin/Desktop/vscode/烟火人家comments.txt')

# 预处理评论数据
huanlesong_comments = preprocess_comments(huanlesong_comments)
jintian_comments = preprocess_comments(jintian_comments)
yanhuo_comments = preprocess_comments(yanhuo_comments)

# 提取与女性主义相关的句子
huanlesong_sentences = extract_feminism_sentences(huanlesong_comments)
jintian_sentences = extract_feminism_sentences(jintian_comments)
yanhuo_sentences = extract_feminism_sentences(yanhuo_comments)

# 生成词云
generate_wordcloud(huanlesong_sentences, filename_prefix='huanlesong')
generate_wordcloud(jintian_sentences, filename_prefix='jintian')
generate_wordcloud(yanhuo_sentences, filename_prefix='yanhuo')

# 总结评论内容
huanlesong_summary = summarize_comments(huanlesong_comments)
jintian_summary = summarize_comments(jintian_comments)
yanhuo_summary = summarize_comments(yanhuo_comments)

print("欢乐颂5评论总结：")
print("\n".join(huanlesong_summary))

print("\n今天的她们评论总结：")
print("\n".join(jintian_summary))

print("\n烟火人家评论总结：")
print("\n".join(yanhuo_summary))
