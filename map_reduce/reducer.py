import redis_config
import json

def reducer(output_file="./data/exemplo.txt"):
    redis_client = redis_config.redis_client

    final_counts = {}
    while redis_client.llen('reduce_queue') > 0:
        item = redis_client.lpop('reduce_queue')
        if item:
            data = json.loads(item.decode('utf-8'))
            word = data['word']
            count = data['count']
            final_counts[word] = count

    with open(output_file, 'w', encoding='utf-8') as f:
        for word, count in sorted(final_counts.items()):
            f.write(f"{word}: {count}\n")

    print(f"Etapa reducer concluída, veja {output_file}")

if __name__ == "__main__":
    reducer()