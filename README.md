
## Handwritten Digit Recognizer using Deep Learning
This project is a digit recognition system built using Convolutional Neural Networks (CNNs) trained on the MNIST dataset. It features a GUI built with Tkinter that allows users to draw digits and receive real-time predictions. The model is implemented using TensorFlow and achieves high accuracy in recognizing handwritten digits from 0 to 9.


## Features

- CNN model trained on MNIST dataset
- GUI for drawing digits (Tkinter-based)
- Real-time digit prediction
- Model saved as model.h5


## Tech Stack

- Python TensorFlow / Keras
- Tkinter 
- NumPy 
- Pillow


## Installation

Clone the repository:

```bash
  git clone https://github.com/Sasidharan-tech/deep-learning-digit-recognizer-arttifai.git
  cd digit-recognizer
```
install dependencies:

```bash
pip install tensorflow numpy opencv-python pillow matplotlib
```
Train the model:
```bash
python model_train.py
```
This will generate a file named model.h5 containing the trained CNN.

Run the GUI app:
```bash
python gui_app.py
```
## Deployment

To deploy this project run

```bash
  python gui_app.py
```


## 📁 Project Structure

```
digit-recognizer/
├── model_train.py   # Trains and saves the CNN model
├── gui_app.py       # GUI for digit drawing and prediction
├── model.h5         # Saved trained model
├── README.md        # Project description and instructions
```

## Screenshots

![Screenshot (10)](https://github.com/user-attachments/assets/dcb750ee-c3a7-4cbb-87f6-d6475fd269ba)

![Screenshot (11)](https://github.com/user-attachments/assets/e67dbb94-f36d-4dc2-a57f-7448f7aeaf39)


## License

This project is for educational purposes.






## Support

For support, email sasidharan.m2004@gmail.com or join our Slack channel.

