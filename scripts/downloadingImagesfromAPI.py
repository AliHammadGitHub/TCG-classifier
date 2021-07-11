import json
import requests

# downloading images from poki api.
i = 1
for j in range(1,17):
    print("start parsing 1st page")
    response = requests.get(f"https://api.pokemontcg.io/v2/cards?page={j}")
    json_data = json.loads(response.text)
    # print(json_data)

    print("Print each key-value pair from JSON response")
    for key, value in json_data.items():
        if type(value) is not int:
            for card in value:
                for att, attValue in card.items():
                    if(att == "images"):
                        for keyIma, image in attValue.items():
                            file = open(f"sample_image{i}.png", "wb")
                            if(keyIma == "small"):
                                ima = requests.get(image)
                                file.write(ima.content)
                                file.close()
                                i += 1
    print("finshed 1st page")
    j+=1