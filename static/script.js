// script.js
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generateBtn').addEventListener('click', function() {
        // 서버에 새로운 URL 생성을 요청합니다.
        fetch('/generate', { method: 'GET' })
            .then(response => response.json())
            .then(data => {
                // 응답에서 받은 URL을 input 필드에 표시합니다.
                document.getElementById('urlField').value = data.url;
            })
            .catch(error => console.error('Error:', error));
    });
});
