# Plain Label App

This is a simple Flask app that generates 4x6 PDF shipping labels with a fixed return address (Mecha Games) and a user-supplied destination address.

## Setup

1. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    python app.py
    ```

4. Open your browser to `http://127.0.0.1:5000`

## Usage

Enter the customer name and shipping address, click "Print Plain Label", and a printable PDF will open in a new tab.
