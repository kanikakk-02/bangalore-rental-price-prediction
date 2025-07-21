## Bangalore Rental Price Prediction

This project predicts monthly rental prices in Bangalore using machine learning. It includes end-to-end development: from **web scraping over 3,500 listings** to **data preprocessing**, **model comparison**, and a **Gradio web app** using the best-performing model.

---

## Overview

-  **Problem Statement:** Predict the rent of residential properties in Bangalore based on features like area, location, furnishing type, and more.
-  **Data Source:** Custom web scraping from [MagicBricks.com](https://www.magicbricks.com/) — over 3,500 listings scraped.
- ⚙ **Tech Stack:** Python, Pandas, Scikit-learn, Gradio, BeautifulSoup, Streamlit (initially).
-  **ML Models Tried:**
  - Linear Regression
  - Support Vector Regression (SVR)
  - Random Forest Regressor
  - Gradient Boosting Regressor ✅ *(Best Performing)*

---

## Project Flow

```mermaid
graph TD
    A[Web Scraping from MagicBricks] --> B[Data Cleaning & Exploration]
    B --> C[Feature Engineering & Outlier Removal]
    C --> D[Multiple ML Models Trained]
    D --> E{Best Model?}
    E -- GBR --> F[Final Model Selected: Gradient Boosting]
    F --> G[Gradio Web App Development]
    G --> H[App Deployment Ready]
