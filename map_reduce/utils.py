import os 

def split_file(file_path, num_chunks=10):
    file_size = os.path.getsize(file_path)
    chunk_size = file_size // num_chunks

    with open(file_path, 'r', encoding='utf-8') as f:
        for i in range(num_chunks):
            output_path = f"{file_path}.part{i+1}"
            with open(output_path, 'w', encoding='utf-8') as outfile:
                chars_read = 0
                while chars_read < chunk_size:
                    line = f.readline()
                    if not line:
                        break
                    outfile.write(line)
                    chars_read += len(line.encode('utf-8'))
            yield output_path