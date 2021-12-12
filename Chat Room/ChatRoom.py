def chat_room(word):
    assert len(word) > 1 or len(word) < 100
    hello = "hello"
    i = 0
    for l in word:
        if l == hello[i]:
            i += 1
            if i == len(hello):
                break
    
    if i ==  len(hello):
        return 'YES'
    else:
        return 'NO'