async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch('/upload/', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('summary').innerText = result.summary;
}
