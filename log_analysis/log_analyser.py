with open('log.txt', 'r', encoding='utf-8') as f:
    # a = f.read()
    # print(a)
    count_level = {'INFO':0, 'ERROR':0, 'WARNING':0}
    error_messages = []
    for line in f:
        parts = line.split()
        level = parts[2]
        message = ' '.join(parts[3:])
        if level == 'INFO':
            count_level['INFO'] += 1
        elif level == 'ERROR':
            error_messages.append(message)
            count_level['ERROR'] += 1
        elif level == 'WARNING':
            count_level['WARNING'] += 1
        
    print(f"""
            Log Summary
            {count_level}

            """)        
    # print(count_level,'\n', error_messages)
    # print(max(count_level, key=count_level.get))




