import transformers
import torch

model_id = "meta-llama/Llama-3.2-3B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {
        "role": "system", 
        "content": "Fala como se fosse um mano de osasco"
    },
    {
        "role": "user", 
        "content": "cinco curiosidades sobre o osasco"
    },
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])
