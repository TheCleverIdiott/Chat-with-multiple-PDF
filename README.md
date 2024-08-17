# Chat with Multiple PDF Files

This is a Streamlit web application that allows users to upload multiple PDF files and ask questions based on the content of those files. The application uses OpenAI's language model to process and answer the questions.

## Features

- **Upload PDFs**: Upload one or more PDF files to the application.
- **Ask Questions**: Input a question related to the content of the uploaded PDFs.
- **Get Answers**: The application processes the PDFs and provides answers to the questions using OpenAI's GPT-based model.

## Installation

### Prerequisites

- Python 3.7 or higher
- OpenAI API key

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/YourRepository.git
   cd YourRepository
   ```

2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file in the root directory and add your OpenAI API key:**
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Interact with the application:**

   - Enter your OpenAI API key in the sidebar.
   - Upload one or more PDF files.
   - Ask a question related to the content of the PDFs.
   - Click the "Process" button to generate an answer.

3. **View the results**: The answer to your question will be displayed on the main page.

## File Structure

```
|-- app.py            # Main Streamlit application
|-- backend.py        # Backend processing logic
|-- requirements.txt  # Python package dependencies
|-- README.md         # This README file
```

## Requirements

All required packages are listed in the `requirements.txt` file. Install them using the following command:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://www.streamlit.io/)
- [OpenAI](https://www.openai.com/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [LangChain](https://langchain.com/)

## Contact

If you have any questions or feedback, feel free to reach out!