async function getData() {
  let response = await fetch('/fetch-dns');
  let dns_data = await response.json();
  return dns_data;
}

function getHtmlTemplate(name, count) {
  return `<div class="d-flex data-container">
      <div id="dns-text">
        ${name}
      </div>
      <div class="chip">
        <div class="chip-label">${count}</div>
      </div>
    </div>
    <div class="action-buttons d-flex">
      <button id="block-dns" class="btn-default">Ignore</button>
      <button id="block-dns" class="btn-danger">Block</button>
    </div>`;
}

function removeDuplicateDns(row) {
  row.parentNode.removeChild(row);
}

function showData(data) {
  data.forEach(dns => {
    const dnsContainer = document.getElementById('dns-container');
    const dnsRow = document.createElement('div');
    dnsRow.setAttribute('class', 'row');
    dnsRow.setAttribute('data-host', dns['qlist'][0]);
    const duplicateDns = document.querySelector(
      '.row[data-host="' + dns['qlist'][0] + '"]'
    );
    let dnsCount = "1";
    if (duplicateDns) {
      removeDuplicateDns(duplicateDns);
      dnsCount = Number(duplicateDns.getAttribute('data-count')) + 1;
    }
    dnsRow.setAttribute('data-count', dnsCount);
    dnsRow.innerHTML = getHtmlTemplate(dns['qlist'][0],  dnsCount);
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