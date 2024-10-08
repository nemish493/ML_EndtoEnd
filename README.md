# Crop Prediction Model Deployment

This project aims to learn about CI/CD pipelines and the deployment of a machine learning model for crop prediction using Docker.

## Project Overview

The crop prediction model predicts the type of crop based on various environmental factors such as:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH level
- Rainfall

## Technologies Used

- Python
- Flask
- scikit-learn
- Docker
- GitHub Actions (for CI/CD)

## Project Structure

```
.
├── app.py                  # Main application file
├── Dockerfile              # Dockerfile for containerizing the app
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates for the web app
├── model/                  # Folder containing the trained model
├── tests/                  # Unit tests for the application
└── .github/                # GitHub Actions workflows
    └── workflows/
        └── ci.yml          # CI/CD pipeline configuration
```

## How to Run the Application

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Build the Docker Image:**

   ```bash
   docker build -t crop-prediction-app .
   ```

3. **Run the Docker Container:**

   ```bash
   docker run -d -p 5000:5000 crop-prediction-app
   ```

4. **Access the Application:**

   Open your web browser and navigate to `http://localhost:5000`.

## CI/CD Pipeline

This project includes a CI/CD pipeline configured with GitHub Actions. It automatically runs tests and builds the Docker image on every push to the main branch. You can see the status of the workflow by navigating to the **Actions** tab in your GitHub repository.

## Unit Testing

Unit tests are included in the `tests/` directory to ensure the reliability and accuracy of the application.

## Contributing

Feel free to submit issues or pull requests for enhancements or fixes.

## License

This project is licensed under the MIT License.
