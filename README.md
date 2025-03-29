# Recruitment Quiz Hackazone

## Overview
Recruitment Quiz Hackazone is a Django-based quiz application designed for recruitment purposes. It allows users to log in, answer quiz questions, track their scores, and view a leaderboard. The application ensures security by implementing JWT authentication and Google reCAPTCHA verification.

## Features
- **User Login**: Users can log in using their name, student number, and email (must be from @akgec.ac.in domain). JWT authentication is used.
- **Google reCAPTCHA Verification**: Ensures bot protection during login.
- **Question Management**: Admins can add quiz questions and correct answers.
- **Quiz Participation**: Users can submit their responses and receive scores based on their answers.
- **Scoring System**: +4 points for a correct answer, -1 for an incorrect answer.
- **Leaderboard**: Users can view rankings based on their scores.
- **Secure API Endpoints**: JWT-based authentication for secure access.

## Live Deployment
The project is deployed on Render and can be accessed at:  
🔗 **[Hackazone Quiz Platform](https://hackazone.onrender.com)**

## API Endpoints

### Authentication
- **Login**: `POST /login/`
  - Required fields: `name`, `student_number`, `email`, `g-recaptcha-response`
  - Returns: JWT `access_token` and `refresh_token`

### Questions
- **Add Questions**: `POST /questions/` (Admin only)
  - Required: `question`, `correct_answer`
- **View All Questions**: `GET /questionlist/`

### Quiz Submission
- **Submit Responses**: `POST /submit-responses/` (Authenticated users)
  - Required: List of `question_id` and `answer_text`
  - Response: Updated user score

### Score and Leaderboard
- **View User Score**: `GET /score/` (Authenticated users)
- **View Leaderboard**: `GET /leaderboard/`

## License
This project is licensed under the MIT License.

## Contributors
- Your Name (@yourgithub)

## Acknowledgements
Special thanks to AKGEC for the inspiration behind this project.

