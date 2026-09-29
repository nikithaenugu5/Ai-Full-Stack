#print the content line byline
# with open("ai_sample.txt", "r") as file:
#     text = file.readlines()

# for line in text:
#     print(line)

#chunk concept

#with open("ai_sample.txt", "r") as file:
    #text = file.read()

#print(text)
#print("No of character:", len(text))

#chunks = []
#chunk_size = 20
#for i in range(0, len(text), chunk_size):
 #   chunk = text[i:i+chunk_size]
  #  chunks.append(chunk)
#print("no of chunks:",len(chunks))
#for chunk in chunks:
 #   print(chunk) 


from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
with open("ai_sample.txt","r") as file:
    text = file.read()
print(text)
print("No.of characters:",len(text))
chunks = []
chunk_size = 25
chunk_overlap = 5
step = chunk_size - chunk_overlap
for i in range(0,len(text),chunk_size):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
# print("no.of chunks:",len(chunks))
# for i in range (len(chunks)):
#     print(f"chunk{i} -> {chunks[i]}")

#Embeddings
embeddings = model.encode(chunks)
print("Embeddings created successfully.")
