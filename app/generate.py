from aitextgen import aitextgen


class Generate:

    def __init__(self):
        self.ft = aitextgen(model_folder="model/model/FairyTales_Model")
        self.bs = aitextgen(model_folder="model/model/BedTimeStories_Model")
        self.hr = aitextgen(model_folder="model/model/Horror_Model")
        self.sf = aitextgen(model_folder="model/model/SciFi_Model")
        self.rs = aitextgen(model_folder="model/model/Russian_Stories")

    def generate(self, genre, prompt):
        if genre == "horror":
            return self.hr.generate_one(prompt=prompt, max_length=250, temperature = 1.0, batch_size=5)
        elif genre == "fairy-tale":
            return self.ft.generate_one(prompt=prompt, max_length=250, temperature = 1.0, batch_size=5)
        elif genre == "sci-fi":
            return self.sf.generate_one(prompt=prompt, max_length=250, temperature = 1.0, batch_size=5)
        elif genre == "bedtime":
            return self.bs.generate_one(prompt=prompt, max_length=250, temperature = 1.0, batch_size=5)
        elif genre == "russian":
            return self.rs.generate_one(prompt=prompt, max_length=250, temperature = 1.0, batch_size=5)
        else:
            return "Error"
