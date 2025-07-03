from flask import Flask, render_template, request
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

try:
    with open('df_percent.pkl', 'rb') as f:
        df_percent = pickle.load(f)
    with open('cosine_similarities.pkl', 'rb') as f:
        cosine_similarities = pickle.load(f)
    with open('indices.pkl', 'rb') as f:
        indices = pickle.load(f)
    print("Model components loaded successfully!")
except FileNotFoundError:
    print("Error: Model component files not found. Make sure 'df_percent.pkl', 'cosine_similarities.pkl', and 'indices.pkl' are in the same directory as app.py")
    exit()

def recommend(name, cosine_similarities=cosine_similarities, df=df_percent, indices=indices):

    if name not in df.index:
        return pd.DataFrame(), f"Restaurant '{name}' not found. Please check the spelling or try another restaurant."


    idx = indices[indices == name].index[0]

    score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending=False)


    top_indexes = list(score_series.iloc[1:31].index)

    recommended_df = df.iloc[top_indexes]

    recommended_df = recommended_df.drop_duplicates(subset=['cuisines', 'Mean Rating', 'cost'], keep='first')

    recommended_df = recommended_df.sort_values(by='Mean Rating', ascending=False).head(10)

    return recommended_df[['cuisines', 'Mean Rating', 'cost']], "Recommendations found!"


# --- Flask Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations_html = None
    error_message = None

    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name'].strip().title()

        if restaurant_name not in df_percent.index:
            error_message = f"Restaurant '{restaurant_name}' not found in our database. Please check the spelling or try another restaurant."
        else:
            reco_df, message = recommend(restaurant_name)
            if not reco_df.empty:
                recommendations_html = reco_df.to_html(classes='table table-striped', index=False)
            else:
                error_message = message

    return render_template('index.html', recommendations=recommendations_html, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)