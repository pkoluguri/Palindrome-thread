import io
import concurrent.futures
import time

parsed_list = []
source_list = []

def process(source_list):
    for word in  source_list:
        reveresed_word = word[::-1]
        if reveresed_word == word:
            parsed_list.append(word)
    print(parsed_list)

if __name__ == "__main__":
    try:
     with io.open("words.txt",encoding="utf-8") as file:
        for word in file:
             word = word.replace("\n","").replace('"',"").replace(",","").replace("(","").replace(")","").replace(".","")
             if word != " " and word != "" and len(word) != 1:
              source_list.append(word)
    except FileNotFoundError:
        print("please run the writer.py file first")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(process,source_list)