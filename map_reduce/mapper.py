import redis_config
import json
import re

def mapper(input_file):
    redis_client = redis_config.redis_client
    word_counts = {}
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            for word in re.findall(r'\b[a-zA-Z]+\b', line.lower()):
                word_counts[word] = word_counts.get(word, 0) + 1
    
    for word, count in word_counts.items():
        redis_client.rpush('shuffle_queue', json.dumps({'word': word, 'count': count}))
        
    print(f"Mapper: processando {input_file}")

if __name__ == '__main__':
    mapper("data/exemplo.txt")