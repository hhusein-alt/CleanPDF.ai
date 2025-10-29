document.addEventListener('DOMContentLoaded', function() {
    const uploadZone = document.getElementById('uploadZone');
    const pdfFile = document.getElementById('pdfFile');
    const uploadForm = document.getElementById('uploadForm');
    const modeButtons = document.querySelectorAll('.mode-btn');
    const modeInput = document.getElementById('modeInput');

    uploadZone.addEventListener('click', function() {
        pdfFile.click();
    });

    uploadZone.addEventListener('dragover', function(e) {
        e.preventDefault();
        uploadZone.classList.add('dragover');
    });

    uploadZone.addEventListener('dragleave', function(e) {
        e.preventDefault();
        uploadZone.classList.remove('dragover');
    });

    uploadZone.addEventListener('drop', function(e) {
        e.preventDefault();
        uploadZone.classList.remove('dragover');

        const files = e.dataTransfer.files;
        if (files.length > 0 && files[0].type === 'application/pdf') {
            pdfFile.files = files;
            uploadForm.submit();
        } else {
            alert('Please upload a valid PDF file');
        }
    });

    pdfFile.addEventListener('change', function() {
        if (pdfFile.files.length > 0) {
            uploadForm.submit();
        }
    });

    modeButtons.forEach(button => {
        button.addEventListener('click', function() {
            modeButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            const mode = this.getAttribute('data-mode');
            modeInput.value = mode;
        });
    });
});
