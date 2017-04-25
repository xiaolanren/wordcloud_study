#!/usr/bin/evn python
#coding:utf-8
#version:1.0.0

import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import sys

def usage():
  print "Create_ciyun.py src.txt fenci.txt picture.jpg beijin.jpg msyh.ttf"
def fenci(src,fenci_txt):
  text = ''
  with open(src) as data:
    for line in data.readlines():
      line = line.strip('\n')
      text += ' '.join(jieba.cut(line))
      text += ' '
  fc = open(fenci_txt,'wb')
  pickle.dump(text,fc)
  fc.close()

def ciyun(fenci,image_src,font,image_dst):
  fc = open(fenci,'rb')
  text = pickle.load(fc)
  background = plt.imread(image_src)
  
  cy = WordCloud( background_color = 'white',
                  mask = backgroud,
                  max_words = 200,
                  stopwords = STOPWORDS,
                  font_path = font,
                  max_font_size = 50,
                  random_state = 30,
                ).generate(text)
  
  image_colors = ImageColorGenerator(background)
  wc.recolor(color_func = image_colors)
  plt.imshow(wc)
  plt.axis('off')
  plt.savefig(image_dst)
  plt.show()
  
  
if __name__ == '__main__':
  src = sys.argv[1]
  fenci_txt = sys.argv[2]
  image_dst = sys.argv[3]
  image_src = sys.argv[4]
  font = sys.argv[5]

  if len(sys.argv) < 6:
    usage()
  else:
    fenci(src,fenci_txt)
    ciyun(fenci_txt,image_src,font,image_dst)
