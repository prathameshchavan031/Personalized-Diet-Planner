# Personalized Diet Planner 🥗

A smart web-based application that provides personalized diet recommendations based on individual characteristics and preferences. Using machine learning, it analyzes various factors to suggest the most suitable diet plan for each user.

## 📱 Application Interface

Here's how our application looks in action:

![Diet Planner Interface](docs/images/Screenshot%202025-11-06%20131252.png)

### Key Interface Features:
1. **Clean, User-friendly Design**: Simple form layout with clear input fields
2. **Input Fields**:
   - Age (numeric input)
   - Gender (dropdown selection)
   - BMI (Body Mass Index)
   - Health Condition (None/Diabetes/BP)
   - Allergy (None/Milk/Nuts)
   - Food Preference (Veg/Non-Veg)
3. **Instant Results**: Get personalized diet recommendations with one click
4. **Responsive Layout**: Works well on both desktop and mobile devices

## 🌟 Features

- User-friendly web interface
- Personalized diet recommendations based on:
  - Age
  - Gender
  - BMI (Body Mass Index)
  - Health conditions (None/Diabetes/BP)
  - Food allergies (None/Milk/Nuts)
  - Food preferences (Vegetarian/Non-Vegetarian)
- Machine Learning powered recommendations using Decision Tree Classifier
- Responsive design with clean UI

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy

## Project Structure

```
personalized_diet_planner/
├── app.py              # Main Flask application
├── train_model.py      # ML model training script
├── requirements.txt    # Project dependencies
├── dataset/           # Directory containing training data
├── model/            # Directory containing trained model
├── static/           # Static files (CSS)
└── template/         # HTML templates
    └── index.html
```

## 🚀 Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/prathameshchavan031/Personalized-Diet-Planner.git
   cd Personalized-Diet-Planner
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Train the model (if not already trained):
   ```bash
   python train_model.py
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your web browser and navigate to `http://localhost:5000`

## How to Use

1. Fill in your personal details in the form:
   - Enter your age
   - Select your gender
   - Enter your BMI
   - Select any health conditions
   - Select any food allergies
   - Choose your food preference
2. Click on "Get Diet Plan"
3. View your personalized diet recommendation

## Model Information

The application uses a Decision Tree Classifier with the following characteristics:
- Maximum depth: 5
- Random state: 42
- Features: Age, Gender, BMI, Health Condition, Allergies, Food Preference

## 🛠️ Requirements

- Python 3.6+
- Flask (Web Framework)
- pandas (Data Processing)
- numpy (Numerical Operations)
- scikit-learn (Machine Learning)

## 📝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

- **Prathamesh Chavan**
  - GitHub: [@prathameshchavan031](https://github.com/prathameshchavan031)

## 🙏 Acknowledgments

- Thanks to all contributors and users of this project
- Special thanks to the Flask and scikit-learn communities

## 📊 Future Improvements

- Add more diet categories and recommendations
- Implement user authentication and profile management
- Add detailed nutritional information for each diet plan
- Integrate with food tracking APIs
- Add mobile-responsive design improvements
=======
# Personalized-Diet-Planner
Personalized Diet Planner
>>>>>>> 91342580468a87906872952c04bfbe359bef86ea
