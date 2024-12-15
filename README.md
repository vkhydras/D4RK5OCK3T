# D4RK5OCK3T

<img src="./D4RK5OCK3T.png" alt="D4RK5OCK3T Logo" width="200"/>

A secure and anonymous terminal-based chat application that allows users to create and join private chat groups. This is an open source project that welcomes community contributions.

## Features

- Create and host private chat servers
- Create secure chat groups with unique IDs and join keys
- Join existing chat groups using group credentials
- Colorized usernames for better chat visibility
- Encrypted connection IDs for secure server access
- Message history for each group
- Cross-platform support (Windows, Linux, MacOS)

## Getting Started

### Fork and Clone

1. Fork this repository by clicking the 'Fork' button at the top right of this page
2. Clone your forked repository:

```bash
git clone https://github.com/YOUR_USERNAME/D4RK5OCK3T.git
cd D4RK5OCK3T
```

### Installation

1. Create a virtual environment (recommended):

```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Starting the Application

1. Activate the virtual environment (if not already activated):

```bash
# On Windows
.\venv\Scripts\activate

# On Linux/MacOS
source venv/bin/activate
```

2. Run the application:

```bash
python main.py
```

### Creating a Chat Group

1. First, start a server:

   - Select option `1` from the main menu
   - The server will start automatically and display a Connection ID
   - Save this Connection ID as it will be needed for others to join

2. Create a new group:
   - Select option `2` from the main menu
   - Enter a group name when prompted
   - Enter your username when prompted
   - The application will display:
     - Group ID
     - Join Key
     - Connection ID
   - Save these credentials to share with other users

### Joining an Existing Group

1. Select option `3` from the main menu
2. Enter the following credentials when prompted:
   - Group ID
   - Join Key
   - Your username
   - Connection ID

### Chat Commands

- Type your message and press Enter to send
- Type `exit` or `quit` to leave the chat
- Press `Ctrl+C` to force exit

## Security Features

- Unique group IDs and join keys for each chat group
- Encrypted connection IDs
- Local database for storing group information
- Colorized usernames for easy identification
- System notifications for user joins and leaves

## Contributing

We welcome contributions from the community! Here's how you can contribute:

1. Fork the Repository

   - Click the 'Fork' button at the top of this page

2. Clone your fork

   ```bash
   git clone https://github.com/YOUR_USERNAME/D4RK5OCK3T.git
   ```

3. Create a branch for your feature

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. Make your changes

   - Write clean, documented code
   - Follow the existing code style
   - Add comments where necessary

5. Commit your changes

   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

6. Push to your fork

   ```bash
   git push origin feature/YourFeatureName
   ```

7. Create a Pull Request
   - Go to the original repository
   - Click 'New Pull Request'
   - Select your fork and branch
   - Describe your changes in detail

### Contribution Guidelines

- Follow Python PEP 8 style guide
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting
- One feature/bug fix per pull request

### Development Setup

1. Set up development environment:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

## Troubleshooting

1. If you can't connect to a server:

   - Ensure the server is running
   - Verify the Connection ID is correct
   - Check your network connection
   - Ensure no firewall is blocking the connection

2. If you can't join a group:
   - Verify the Group ID and Join Key are correct
   - Ensure the server is running
   - Check that you're using the correct Connection ID

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 D4RK5OCK3T

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## Support

- Open an issue for bug reports
- Start a discussion for feature requests
- Check existing issues and discussions before creating new ones
