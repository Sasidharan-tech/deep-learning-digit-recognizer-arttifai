🧠 Handwritten Digit Recognizer using Deep Learning

This project is a digit recognition system built using Convolutional Neural Networks (CNNs) trained on the MNIST dataset. It features a GUI built with Tkinter that allows users to draw digits and receive real-time predictions. The model is implemented using TensorFlow and achieves high accuracy in recognizing handwritten digits from 0 to 9.

🔧 Features

 🧠 CNN model trained on MNIST dataset
 🖼️ GUI for drawing digits (Tkinter-based)
 ⚡ Real-time digit prediction
 💾 Model saved as `model.h5`

🚀 Technologies Used

 Python
 TensorFlow / Keras
 Tkinter
 NumPy
 Pillow

📦 Installation
1. Clone the repository:

      git clone https://github.com/yourusername/digit-recognizer.git
      cd digit-recognizer


2. Install dependencies:

pip install tensorflow numpy opencv-python pillow matplotlib

3. Train the model:

python model_train.py

This will generate a file named `model.h5` containing the trained CNN.

4. Run the GUI app:

python gui_app.py

Use your mouse to draw a digit, then click "Predict" to see the result.


📁 Project Structure


digit-recognizer/
├── model_train.py       # Trains and saves the CNN model
├── gui_app.py           # GUI for digit drawing and prediction
├── model.h5             # Saved trained model
├── README.md            # Project description and instructions




📷 Screenshots (Optional)

![Screenshot (10)](https://github.com/user-attachments/assets/dcb750ee-c3a7-4cbb-87f6-d6475fd269ba)

![Screenshot (11)](https://github.com/user-attachments/assets/e67dbb94-f36d-4dc2-a57f-7448f7aeaf39)




Made with ❤️ using Deep Learning.
