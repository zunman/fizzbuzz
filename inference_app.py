from fastapi import FastAPI
from transformers import pipeline
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline


# Create a FastAPI app
app = FastAPI()

# Load a pre-trained model from the Hugging Face Model Hub
model_path = "martin-ha/toxic-comment-model"

@app.post("/predict")
async def predict(input_data: dict):

	tokenizer = AutoTokenizer.from_pretrained(model_path)
	model = AutoModelForSequenceClassification.from_pretrained(model_path)
	

    
    	# Perform inference
 
    	#result = question_answerer(question=question, context=context)
	pipeline =  TextClassificationPipeline(model=model, tokenizer=tokenizer)
	print(input_data["text"])
	result = pipeline(input_data["text"])
	
	return result

# Define a root endpoint for health checks
@app.get("/")
async def read_root():
    	return {"status": "running"}

