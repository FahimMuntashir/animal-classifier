document.addEventListener('DOMContentLoaded', function() {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const imagePreview = document.getElementById('image-preview');
    const previewContainer = document.getElementById('preview-container');
    const resultContainer = document.getElementById('result-container');
    const errorContainer = document.getElementById('error-container');
    const classifyBtn = document.getElementById('classify-btn');
    const predictionSpan = document.getElementById('prediction');
    const confidenceSpan = document.getElementById('confidence');
    const errorMessage = document.getElementById('error-message');

    let selectedFile = null;

    // Handle drag and drop events
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });

    // Handle click to upload
    dropZone.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });

    // Handle file selection
    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            showError('Please select an image file.');
            return;
        }

        selectedFile = file;
        const reader = new FileReader();

        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            previewContainer.classList.remove('d-none');
            resultContainer.classList.add('d-none');
            errorContainer.classList.add('d-none');
            classifyBtn.disabled = false;
        };

        reader.readAsDataURL(file);
    }

    // Handle classification
    classifyBtn.addEventListener('click', async () => {
        if (!selectedFile) return;

        classifyBtn.disabled = true;
        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.error) {
                showError(data.error);
                return;
            }

            showResult(data);
        } catch (error) {
            showError('An error occurred while processing your request.');
        } finally {
            classifyBtn.disabled = false;
        }
    });

    // Show result
    function showResult(data) {
        predictionSpan.textContent = data.prediction;
        confidenceSpan.textContent = data.confidence;
        resultContainer.classList.remove('d-none');
        errorContainer.classList.add('d-none');
    }

    // Show error
    function showError(message) {
        errorMessage.textContent = message;
        errorContainer.classList.remove('d-none');
        resultContainer.classList.add('d-none');
    }
}); 