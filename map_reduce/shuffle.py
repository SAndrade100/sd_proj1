import redis_config
import json

def shuffle():
    redis_client = redis_config.redis_client

    word_counts = {}
    while redis_client.llen('shuffle_queue') > 0:
        item = redis_client.lpop('shuffle_queue')
        if item:
            data = json.loads(item.decode('utf-8'))
            word = data['word']
            count = data['count']
            word_counts[word] = word_counts.get(word, 0) + count

    for word, total_count in word_counts.items():
        redis_client.rpush('reduce_queue', json.dumps({'word': word, 'count': total_count}))

    print('Processo de shuffle concluido')

if __name__ == '__main__':
    shuffle()