import gradio as gr
import pandas as pd
import joblib

# Load model and data
model = joblib.load("gradient_boosting_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

def predict_rent(Location, Area, BHK, Bathrooms, Furnishing):
    try:
        # Create a single row dataframe with input values
        input_df = pd.DataFrame([[Location, Area, BHK, Bathrooms, Furnishing]], columns=feature_columns)
        prediction = model.predict(input_df)[0]
        return f"Estimated Monthly Rent: ₹{int(prediction):,}"
    except Exception as e:
        return f"Error: {e}"

# Example inputs (based on your dataset)
example_inputs = [
    ["Whitefield", 1200, 2, 2, "Semi-Furnished"],
    ["Indiranagar", 850, 1, 1, "Fully-Furnished"],
    ["HSR Layout", 1500, 3, 2, "Unfurnished"]
]

# UI Layout
with gr.Blocks() as demo:
    gr.Markdown("# 🏡 Bangalore Rental Price Predictor")
    gr.Markdown("Enter details about a rental property in Bangalore to estimate its monthly rent.")

    with gr.Row():
        Location = gr.Textbox(label="Location")
        Area = gr.Number(label="Area (in sq. ft.)")
    
    with gr.Row():
        BHK = gr.Number(label="BHK")
        Bathrooms = gr.Number(label="Bathrooms")
        Furnishing = gr.Radio(["Fully-Furnished", "Semi-Furnished", "Unfurnished"], label="Furnishing Status")
    
    predict_button = gr.Button("Predict Rent")
    result = gr.Textbox(label="Prediction", interactive=False)

    predict_button.click(fn=predict_rent, inputs=[Location, Area, BHK, Bathrooms, Furnishing], outputs=result)

    gr.Examples(
        examples=example_inputs,
        inputs=[Location, Area, BHK, Bathrooms, Furnishing]
    )

demo.launch()
