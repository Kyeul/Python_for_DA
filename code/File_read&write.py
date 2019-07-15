# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:48:56 2019

@author: gyul6
"""

#f = open('file_name', 'W')  #file_name이라는 파일을 연다. 모드는 wt다.
#f.write(str)
#f.close()
#f = open('C:\myPyCode\myFile.txt', 'w')     #1) 'myFile.txt' 파일 쓰기 모드로 열기
#f.write('This is my first file.')   #2) 연 파일에 문자열 쓰기
#f.close()

f = open('myFile.txt', 'r') # f = open('file_name) 도 가능. r은 모드의 디폴트
data = f.read()
f.close()

print(data)