import redis_config
import json

def shuffle():
    redis_client = redis_config.redis_client
    word_counts = {}
    
    while item := redis_client.lpop('shuffle_queue'):
        data = json.loads(item.decode('utf-8'))
        word_counts[data['word']] = word_counts.get(data['word'], 0) + data['count']
    
    for word, count in word_counts.items():
        redis_client.rpush('reduce_queue', json.dumps({'word': word, 'count': count}))
    
    print('Processo de shuffle concluido')

if __name__ == '__main__':
    shuffle()