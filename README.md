# Student Progress Calculator

## Overview
The Student Progress Calculator application helps students and staff track academic progress based on credit inputs. It offers both manual and automatic input methods for convenience and displays progress outcomes using histograms.

## Features
- Input validation for credits
- Progress status calculation
- Horizontal and vertical histograms
- Manual and automatic input methods

## Installation
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/yourusername/student-progress-calculator.git
   cd student-progress-calculator
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Usage
### Running the Application
Navigate to the \`src\` directory and run the \`main.py\` file:
\`\`\`bash
python src/main.py
\`\`\`

### Manual Input
- Follow the prompts to enter credit values.
- View progress outcomes and histograms.

### Automatic Input
- Ensure \`dataset.txt\` is present in the \`data\` directory.
- The application reads the file and generates histograms based on its contents.

## File Structure
- \`src/\`: Contains all the source code.
  - \`CharInput.py\`: Handles character input validation.
  - \`Histograms.py\`: Generates and displays histograms.
  - \`ForStaff.py\`: Contains methods for staff operations (manual and automatic).
  - \`main.py\`: Main entry point of the application.
- \`data/\`: Contains the dataset for automatic input.
  - \`dataset.txt\`: Sample dataset for automatic input.
- \`README.md\`: This file.
- \`CONTRIBUTING.md\`: Guidelines for contributing to the project.
- \`LICENSE.md\`: License information.
- \`requirements.txt\`: List of dependencies.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
EOL
