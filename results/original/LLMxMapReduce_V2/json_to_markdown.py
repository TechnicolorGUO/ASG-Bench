import json
import os

input_file = "E:/1101_Automatic_Survey_Generation/Results/LLMxMapReduce_V2/Biology/bio_results.json"
output_dir = "E:/1101_Automatic_Survey_Generation/Results/LLMxMapReduce_V2/Biology"

with open(input_file, "r") as f:
    for line in f:
        data = json.loads(line)
        content = data["content"]
        content += "\n\n" + data["ref_str"]
        with open(os.path.join(output_dir, data["title"] + ".md") , "w") as out:
            out.write(content)