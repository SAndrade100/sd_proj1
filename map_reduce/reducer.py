import redis_config
import json

def reducer(output_file="./data/exemplo.txt"):
    redis_client = redis_config.redis_client
    final_counts = {}
    
    while item := redis_client.lpop('reduce_queue'):
        data = json.loads(item.decode('utf-8'))
        final_counts[data['word']] = data['count']
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(f"{word}: {count}\n" for word, count in sorted(final_counts.items()))
    
    print(f"Etapa reducer concluída, veja {output_file}")

if __name__ == "__main__":
    reducer()