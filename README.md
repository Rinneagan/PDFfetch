# PDFetch

A modern, secure Python desktop application for searching, previewing, and downloading PDF files with a clean graphical user interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## Features

### Core Functionality
- **PDF Search**: Search for PDFs using Google Search API via SerpApi
- **PDF Preview**: Preview the first page of PDFs before downloading
- **Download Management**: Download PDFs with real-time progress tracking
- **Cancelable Downloads**: Stop downloads at any time with a single click

### User Interface
- **Dark/Light Themes**: Switch between dark and light visual themes
- **Search History**: Maintain search history between sessions
- **Download History**: Track all downloaded files
- **Status Bar**: Real-time operation feedback and status updates
- **Progress Tracking**: Visual progress bar for download operations

### Security & Validation
- **URL Validation**: Validates URLs before downloading (HTTP/HTTPS only)
- **File Size Limits**: Prevents downloading files larger than 100MB
- **PDF Validation**: Verifies downloaded files are valid PDFs
- **Concurrent Download Limits**: Maximum 3 simultaneous downloads
- **Secure API Key Management**: Environment variable-based configuration

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Internet connection
- SerpApi API key ([Get one here](https://serpapi.com/))

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/PDFfetch.git
   cd PDFfetch
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**
   
   Create a `.env` file in the root directory:
   ```bash
   SERPAPI_KEY=your_actual_api_key_here
   ```
   
   **Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

4. **Install pdf2image (for PDF preview)**
   
   **Windows:**
   ```bash
   pip install pdf2image
   ```
   Also install [poppler](https://github.com/oschwartz10612/poppler-windows) and add it to your PATH.

   **Linux:**
   ```bash
   sudo apt-get install poppler-utils
   pip install pdf2image
   ```

   **macOS:**
   ```bash
   brew install poppler
   pip install pdf2image
   ```

## Usage

### Running the Application

```bash
python crawler.py
```

### Basic Workflow

1. **Launch the application** - The GUI will open with the dark theme by default
2. **Enter search term** - Type your PDF search query in the search box
3. **Search** - Click "Search PDFs" to find matching PDFs
4. **Preview** - Select a PDF from results and click "Preview PDF" to view the first page
5. **Download** - Click "Download PDF" to save the selected PDF
6. **Choose location** - Use "Select Folder" to change download directory (default: Downloads)
7. **Cancel** - Click "Cancel Download" to stop an active download
8. **Switch theme** - Use "Switch Theme" to toggle between dark and light modes

### Advanced Features

- **Search History**: Access previous searches via the dropdown
- **Download History**: View all downloaded files in the history list
- **Progress Tracking**: Monitor download progress in real-time
- **Error Handling**: Automatic validation and error reporting

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SERPAPI_KEY` | Your SerpApi API key | Yes |

### Application Settings (config.py)

| Setting | Default | Description |
|---------|---------|-------------|
| `DEFAULT_DOWNLOAD_DIR` | `~/Downloads` | Default download directory |
| `MAX_RETRIES` | `3` | Maximum retry attempts for failed requests |
| `TIMEOUT` | `30` | Request timeout in seconds |
| `MAX_FILE_SIZE` | `100 MB` | Maximum allowed file size for downloads |
| `MAX_CONCURRENT_DOWNLOADS` | `3` | Maximum simultaneous downloads |

## Security Considerations

- **API Key Protection**: API keys are loaded from environment variables only
- **URL Validation**: Only HTTP/HTTPS URLs are allowed
- **File Validation**: Downloaded files are verified as valid PDFs
- **Size Limits**: Prevents downloading excessively large files
- **No Hardcoded Secrets**: All sensitive data is externalized

## Troubleshooting

### Common Issues

**"SERPAPI_KEY environment variable is not set"**
- Ensure your `.env` file exists in the project root
- Verify the format: `SERPAPI_KEY=your_key` (no spaces around `=`)
- Restart the application after creating the `.env` file

**"pdf2image module not installed"**
- Install pdf2image: `pip install pdf2image`
- Install poppler for your operating system (see Installation section)
- Verify poppler is in your system PATH

**"File too large" error**
- The file exceeds the 100MB limit
- Adjust `MAX_FILE_SIZE` in `config.py` if needed

**"Downloaded file is not a valid PDF"**
- The URL may not point to a valid PDF
- The file may be corrupted
- Try a different source

**Preview not working**
- Ensure pdf2image and poppler are properly installed
- Check the application logs in `app.log` for detailed errors

### Logging

Application logs are saved to `app.log` in the project directory. Check this file for detailed error information.

## Project Structure

```
PDFfetch/
├── .env                 # API key configuration (not in git)
├── .gitignore          # Git ignore rules
├── config.py           # Application configuration
├── crawler.py          # Main application and GUI
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── app.log            # Application logs
└── *.pdf              # Downloaded PDF files
```

## Dependencies

- `requests>=2.31.0` - HTTP library for API requests
- `PyPDF2>=3.0.0` - PDF file manipulation
- `python-dotenv>=1.0.0` - Environment variable management
- `Pillow>=10.0.0` - Image processing
- `pdf2image>=1.16.3` - PDF to image conversion
- `serpapi>=0.1.0` - Google Search API client

## Development

### Code Quality

- Follows PEP 8 style guidelines
- Type hints for better code clarity
- Comprehensive error handling
- Modular architecture with separation of concerns

### Testing

Run the application with different scenarios:
- Various search terms
- Different file sizes
- Network interruptions
- Invalid URLs
- Missing dependencies

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python crawler.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [SerpApi](https://serpapi.com/) for providing the Google Search API
- [PyPDF2](https://github.com/py-pdf/PyPDF2) for PDF processing
- [pdf2image](https://github.com/Belval/pdf2image) for PDF to image conversion
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section above

## Changelog

### Version 1.0.0 (Current)
- Initial release
- PDF search and download functionality
- GUI with dark/light themes
- Search and download history
- Security improvements (URL validation, file validation, size limits)
- Concurrent download management
- Comprehensive error handling 
