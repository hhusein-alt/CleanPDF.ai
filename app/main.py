import os
import tempfile
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from werkzeug.utils import secure_filename
from watermark_detector import WatermarkDetector
from watermark_remover import WatermarkRemover

# Create necessary directories
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'pdf'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = FastAPI(title="Gamma AI Watermark Remover API", version="2.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize detector and remover
detector = WatermarkDetector()
remover = WatermarkRemover()

def allowed_file(filename: str) -> bool:
    """Check if file type is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.post("/remove_watermark")
async def remove_watermark(pdf_file: UploadFile = File(...)):
    """Remove Gamma.app watermarks from a PDF file"""

    # Validate file
    if not pdf_file.filename:
        return JSONResponse({"error": "No file selected. Please choose a PDF file."}, status_code=400)

    if not allowed_file(pdf_file.filename):
        return JSONResponse({"error": "Invalid file type. Please upload a PDF file."}, status_code=400)

    # Secure filename
    filename = secure_filename(pdf_file.filename)

    # Create temporary input file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_input:
        upload_path = temp_input.name
        try:
            # Save uploaded PDF
            content = await pdf_file.read()
            temp_input.write(content)
            temp_input.flush()

            print(f"Analyzing file: {filename}")
            elements_to_remove, error = detector.identify_watermarks(upload_path)

            if error:
                raise Exception(error)

            if elements_to_remove:
                # Prepare output file
                output_filename = f'processed_{filename}'
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)

                print("Removing watermarks...")
                images_removed, links_removed = remover.clean_pdf_from_target_domain(upload_path, output_path)

                total_removed = images_removed + links_removed
                print(f"Watermarks removed: {total_removed}")

                return FileResponse(
                    output_path,
                    media_type='application/pdf',
                    filename=output_filename,
                    headers={"Content-Disposition": f"attachment; filename={output_filename}"}
                )
            else:
                return JSONResponse(
                    {"message": "No Gamma.app watermarks found in PDF."},
                    status_code=200
                )

        except Exception as e:
            error_message = f"Error processing file: {str(e)}"
            print(error_message)
            return JSONResponse({"error": error_message}, status_code=500)
        finally:
            try:
                os.unlink(upload_path)
            except:
                pass


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc: StarletteHTTPException):
    """HTTP error handler"""
    return JSONResponse({"error": f"{exc.detail}"}, status_code=exc.status_code)


@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    """General error handler"""
    return JSONResponse({"error": f"Internal server error: {str(exc)}"}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

