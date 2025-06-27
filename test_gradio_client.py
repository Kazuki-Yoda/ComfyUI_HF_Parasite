import json

from gradio_client import Client

client = Client("black-forest-labs/FLUX.1-dev")
api = client.view_api(return_format="dict")
print(type(api))
print(json.dumps(api, indent=2))

# result = client.predict(
#     prompt="A beautiful girl with long hair and blue eyes",
#     seed=0,
#     randomize_seed=True,
#     width=1024,
#     height=1024,
#     guidance_scale=3.5,
#     num_inference_steps=28,
#     api_name="/infer"
# )
# print(result)
