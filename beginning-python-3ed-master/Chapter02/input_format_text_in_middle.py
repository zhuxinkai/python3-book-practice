# Prints a sentence in a centered "box" of correct width

# 从这里可以学习到相应的变量的命名方式。 例如： screen_width  , text_windth , box_width这样的
# 下滑线命名方式非常有助于提高代码的可读性。
# 可以做为输出的一个模块。(发现这个方法在输出中文的时候会异常）

sentence = input("Sentence: ")

screen_width = 80
text_width   = len(sentence)
box_width    = text_width*2
left_margin  = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+')
print(' ' * left_margin + '|  ' + ' ' * (box_width-4)  + '|')
print(' ' * left_margin + '|  ' +       sentence      + '       |')
print(' ' * left_margin + '|  ' + ' ' * (box_width-4)     + '|')
print(' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+')
print()


'''

采用中文字符的空格填充 chr(12288)

tp = '{0:^10}\t{1:{3}^10}\t{2:^10}'
print(tp.format('名次'，'学校名称'，'总分',chr(12288)))

'''

