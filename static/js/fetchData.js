async function getData() {
  let response = await fetch('/fetch-dns');
  let dns_data = await response.json();
  return dns_data;
}

function showData(data) {
  data.forEach(dns => {
    const dnsContainer = document.getElementById('dns-container');
    const dnsRow = document.createElement('div');
    dnsRow.setAttribute('class', 'row d-flex');
    dnsRow.innerHTML = `<div id="dns-text">
        ${dns[0]['Name']}
      </div>
      <div class="action-button">
        <button id="block-dns" class="btn-danger">Block</button>
      </div>`;
    dnsContainer.appendChild(dnsRow);
  });
}

async function renderData() {
  const dns_data = await getData();
  if (dns_data['dns_data']) {
    showData(dns_data['dns_data']);
  }
}

window.onload = function() {
  renderData();
  setInterval(function() {
    renderData();
  }, 3000);
}