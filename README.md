# HuggingChat Client Documentation

## Introduction

The HuggingChat client is a graphical user interface (GUI) for interacting with the HuggingChat, an open-source large language model developed by Hugging Face, an artificial intelligence company founded in 2016. This client provides a user-friendly interface to communicate with the chatbot using text input. This client uses the Unofficial HuggingChat Python API, you can find it [here.](https://github.com/Soulter/hugging-chat-api)

## Prerequisites

Before running this HuggingChat client, ensure you have the following:

- Python installed on your system (version 3.6 or higher).
- The required libraries installed. You can install them using the following command:

```bash
pip install tkinter ttkthemes hugchat
```

## Getting Started

To use the HuggingChat client, follow these steps:

1. **Clone the Repository**: Download or clone the repository containing the client code.

2. **Configure Credentials**:
   - Create a file named `credentials` and add your login information in the following format:
     ```
     your_email@example.com
     your_password
     ```

   **Note**: If you don't have a huggingchat account, you'll need to create one [on huggingchat.]https://huggingface.co/chat/)

3. **Set Up the Prompt**:
   - Create a file named `prompt` and write the initial user message you want to start the conversation with.

4. **Run the Client**:
   - Execute the client code using Python.

```bash
python client.py
```
or
```bash
python3 client.py
```

## Interaction

1. **User Input**:
   - Type your messages in the input field and press `Enter` or click the "Send" button to send them to the chatbot.

2. **Exiting the Client**:
   - Type "exit" in the input field and press `Enter` or use the "Close" button to close the client.

## GUI Interface

- The GUI window contains a conversation display area, an input field, and "Send" and "Close" buttons.

- The input field allows you to type messages to interact with the chatbot.

- The "Send" button sends the typed message to the chatbot.

- The "Close" button disconnects from the chatbot and closes the client.

## Important Notes

- Make sure to keep the `credentials` and `prompt` files in the same directory as the client code.

- The `credentials` file should contain your HuggingChat login information (email and password).

- The `prompt` file should contain the initial message you want to send to the chatbot.

- Ensure that you have an active internet connection to use the HuggingChat client.

## Conclusion

You are now ready to use the HuggingChat client. Enjoy interacting with the chatbot using this interface! If you encounter any issues or have further questions, don't hesitate to ask.
