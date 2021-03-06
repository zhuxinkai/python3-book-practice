# Prints a sentence in a centered "box" of correct width

# 从这里可以学习到相应的变量的命名方式。 例如： screen_width  , text_windth , box_width这样的
# 下滑线命名方式非常有助于提高代码的可读性。
# 可以做为输出的一个模块。

sentence = input("Sentence: ")

screen_width = 80
text_width   = len(sentence)
box_width    = text_width + 6
left_margin  = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+')
print(' ' * left_margin + '|  ' + ' ' * text_width     + '  |')
print(' ' * left_margin + '|  ' +       sentence       + '  |')
print(' ' * left_margin + '|  ' + ' ' * text_width     + '  |')
print(' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+')
print()