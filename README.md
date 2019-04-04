# Keyword-Spotting-Based-on-Low-Quality-Acoustic-Model-Output
Chinese only. 
Do you want to implement a Chinese speech keyword spotting program like me, but only have a small number of Chinese open data sets which is not enough to generate a competitive end-to-end speech recognition/keyword spotting program (CER about 30%)? Try this tool!

The principle is to convert Chinese characters into Pinyin and match the target keywords.

Input: output sting of your recognition/spotting program.
Output: "keyword1;keyword1;keyword2;keyword4....."

I strongly recommend removing the language model of your speech recognition program so that the string can convey the row speech more faithfully. After all, if your acoustic model is only 70 percent accurate, Kenlm can't help you much more than distorting row pronunciation.

## Using
demo keyword: 您好请稍等；再见；请交费；


import spotting

result = getWord(input)

##parameters
simithreshold: 78 default. If the Similarity of Pinyin string of the input and keyword is greater than simithreshold, the word will be corrected to the target word and added to output.
