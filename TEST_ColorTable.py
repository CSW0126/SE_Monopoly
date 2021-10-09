def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

    #test    
    print('\x1b[6;30;47m' + 'Success!' + '\x1b[0m')
print_format_table()

# 30-37 text color
#   black: 30
#   red: 31
#   green: 32
#   yellow: 33
#   blue: 34
#   magenta: 35
#   cyan: 36
#   white: 37

# 40–47 background color
#   39 重置文本顏色
#   49 重置背景顏色
#   1  加粗文本/ 高亮
#   22 重置加粗/ 高亮
#   0  重置所有文本屬性（顏色，背景，亮度等）為默認值