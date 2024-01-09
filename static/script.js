// script.js
document.addEventListener('DOMContentLoaded', function() {
    var currentEndpoint = null;
    document.getElementById('generateBtn').addEventListener('click', function() {
        // 서버에 새로운 URL 생성을 요청합니다.
        fetch('/generate', { method: 'GET' })
            .then(response => response.json())
            .then(data => {
                history.pushState( {page: 1}, data.url, data.url)  // url만 변경해준다.
                var urlField = document.getElementById("urlField")      // input value 변경
                urlField.value = data.url
                currentEndpoint = data.url + '/loglist'
                console.log(currentEndpoint)
            })
            .catch(error => console.error('Error:', error));
    });
    // 5초마다 fetchEndpointData 함수를 실행
    setInterval(function() {
        if (currentEndpoint) {
            fetchEndpointData(currentEndpoint);
        }
    }, 5000);
});

function fetchEndpointData(endpoint) {
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            const requestInfoDiv = document.getElementById('request-details');
            requestInfoDiv.innerHTML = `
                <h2>Details</h2>
                <p>Method: ${data.method}</p>
                <p>URL: ${data.url}</p>
                <p>Base URL: ${data.base_url}</p>
                <p>Query Params: ${JSON.stringify(data.query_params)}</p>
                <p>Headers: ${JSON.stringify(data.headers)}</p>
                <p>Data: ${data.data}</p>
                <p>Text Data: ${data.text_data}</p>
            `;
            const requestsummaryDiv = document.getElementById('request-list');
            requestsummaryDiv.innerHTML = `
                <h2>Requests</h2>
                <p>Method: ${data.method}</p>
                <p>Host: ${JSON.stringify(data.headers['Host'])}</p>
                <p>Time: ${data.time}</p>
            `
        })
        .catch(error => console.error('Error fetching endpoint data:', error));
}