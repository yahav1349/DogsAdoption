# DogsAdoption
## Overview
Our website dedicated to helping you find the perfect dog companion.
Our platform is designed to guide you through a comprehensive survey, enabling us to match you with the most suitable dog breeds based on your preferences.
Additionally, we extend our services by incorporating advanced algorithms, including both matching and natural language processing (NLP), leveraging an extensive dog breed dataset.

## Process:
1.Users are prompted to complete a detailed survey on the website, outlining their preferences and ideal dog characteristics.
2.Responses are transformed into tensors, and our sophisticated matching algorithm, coupled with NLP capabilities, is applied to compare user preferences with the available dog breeds in our dataset.
3.Utilizing web scraping techniques, a similar process is undertaken with dogs available for adoption on various adoption sites.
4.Users receive personalized recommendations, encompassing the most suitable dog breeds, as well as information on dogs available for adoption that align with their preferences.

### Our goal is to make the adoption process seamless and ensure that each user finds their ideal canine companion.

# How to start the project:
## instrucrtions:
### Download all filles as they are in the git

To execute the main program, you have two options available. Firstly, you can utilize the usual_main.py script,
 which should be executed once you have initialized the model and acquired the necessary .pkl files. 
Alternatively, there's the first_main.py script, which you need to execute initially to generate the .pkl files. 
This ensures that the model won't encounter extended runtime periods.

The initial execution and creation of the .pkl files typically require approximately 20 minutes, 
while subsequent runs using the pre-loaded model usually complete within a maximum of 20 seconds

### The two running options: 
1. Initialize in case you don't have the .pkl files:
	At first:
	To utilize the part-of-speech tagging model so the preproccessing won't fail, it's only necessary if you're running the model from scratch without pre-existing .pkl files.
	In the pos_model.py script, within the _init_ method, you'll need to insert your Gemini API key into the genai.configure() function. 
	Specifically, it should be entered as follows: genai.configure([Your API Key])
	After you set every thing you may continue.	

	Enter anaconda powershell prompt

Write:

    1. conda env create -n backEnd -f backEndFinal.yml
    2. conda activate backEnd
	3. cd algorithm
	4. python first_main.py

2. Run the backend in case you already have the .pkl files:

	Enter anaconda powershell prompt

Write:

	1. conda env create -n backEnd -f backEndFinal.yml
	2. conda activate backEnd
	3. cd algorithm
	4. python usual_main.py

When you see: 

INFO:     Application startup complete.

### Go to next step:
#### make sure you have node js on your comp, if not, install it.

Open another (different) anaconda powershell prompt

Write:

    1. conda env create -n react -f react.yml
    2. conda activate react
    3. npm install
    4. npm start

Now you are able to use the site freely and get the model's findings based on your input.
