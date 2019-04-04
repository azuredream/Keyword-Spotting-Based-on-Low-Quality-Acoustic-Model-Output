# Keyword-Spotting-Based-on-Low-Quality-Acoustic-Model-Output
Chinese only. 
Do you want to implement a Chinese speech keyword spotting program like me, but only have a small number of Chinese open data sets which is not enough to generate a competitive end-to-end speech recognition/keyword spotting program (CER about 30%)? Try this tool!

The principle is to convert Chinese characters into Pinyin and match the target keywords.

Input: output sting of your recognition/spotting program.
Output: "keyword1;keyword1;keyword2;keyword4....."

I strongly recommend removing the language model of your speech recognition program so that the string can convey the row speech more faithfully. After all, if your acoustic model is only 70 percent accurate, Kenlm can't help you much more than distorting row pronunciation.
