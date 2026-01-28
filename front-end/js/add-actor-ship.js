// ====== BL vindo pela URL ======
const urlParams = new URLSearchParams(window.location.search);
const blId = urlParams.get('blId');

// Função para voltar para bl-details (navegação explícita)
function goBackToDetails() {
    if (blId) {
        window.location.href = 'bl-details.html?blId=' + blId;
    } else {
        window.location.href = 'bl-list.html';
    }
}

if (!blId) {
    alert('BL não informado');
    window.location.href = 'bl-list.html';
}

let shipCount = 1;

document.addEventListener('DOMContentLoaded', async function () {
    requireAuth();
    await loadSeriesInfo();

    const form = document.getElementById('add-ship-form');
    form.addEventListener('submit', handleSubmit);
});

async function loadSeriesInfo() {
    try {
        const response = await fetch(`${API_BASE_URL}/series/${blId}`);
        if (response.ok) {
            const series = await response.json();
            document.getElementById('current-bl').textContent = series.title;
        }
    } catch (error) {
        console.error('Erro ao carregar serie:', error);
    }
}

function addShipSection() {
    shipCount++;
    const shipsContainer = document.getElementById('ships-container');

    const shipSection = document.createElement('div');
    shipSection.className = 'ship-section';
    shipSection.id = `ship-section-${shipCount}`;

    shipSection.innerHTML = `
        <div class="ship-header">
            <h3 class="ship-title">Ship ${shipCount}</h3>
            <button type="button" class="remove-ship-button" onclick="removeShipSection(${shipCount})">
                × Remover
            </button>
        </div>

        <div class="form-group">
            <label for="ship-name-${shipCount}">Nome do Ship</label>
            <input 
                type="text" 
                id="ship-name-${shipCount}" 
                class="form-input"
                placeholder="Ex: BrightWin"
                required
            >
        </div>

        <div class="form-group">
            <label for="actor-1-${shipCount}">Ator 1</label>
            <input 
                type="text" 
                id="actor-1-${shipCount}" 
                class="form-input"
                placeholder="Nome do primeiro ator"
                required
            >
        </div>

        <div class="form-group">
            <label for="actor-2-${shipCount}">Ator 2</label>
            <input 
                type="text" 
                id="actor-2-${shipCount}" 
                class="form-input"
                placeholder="Nome do segundo ator"
                required
            >
        </div>
    `;

    shipsContainer.appendChild(shipSection);
}

function removeShipSection(shipNumber) {
    const shipSection = document.getElementById(`ship-section-${shipNumber}`);
    if (shipSection) {
        shipSection.remove();
    }
}

async function handleSubmit(e) {
    e.preventDefault();

    const ships = [];

    for (let i = 1; i <= shipCount; i++) {
        const section = document.getElementById(`ship-section-${i}`);
        if (!section) continue;

        const shipName = document.getElementById(`ship-name-${i}`);

        if (shipName?.value.trim()) {
            ships.push({ name: shipName.value.trim() });
        }
    }

    if (ships.length === 0) {
        showMessage('error', 'Preencha pelo menos um ship.');
        return;
    }

    try {
        let successCount = 0;

        for (const ship of ships) {
            // 1. Criar o ship
            const createResponse = await fetch(`${API_BASE_URL}/ship-actors`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name: ship.name })
            });

            if (!createResponse.ok) {
                const error = await createResponse.json();
                throw new Error(error.detail || 'Erro ao criar ship');
            }

            const createdShip = await createResponse.json();

            // 2. Associar o ship à série
            const linkResponse = await fetch(`${API_BASE_URL}/series/${blId}/ship-actors`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ ship_id: createdShip.id })
            });

            if (linkResponse.ok) {
                successCount++;
            }
        }

        showMessage('success', `${successCount} ship(s) criado(s) e vinculado(s) com sucesso!`);
        setTimeout(() => goBackToDetails(), 2000);
    } catch (error) {
        showMessage('error', error.message);
    }
}

function showMessage(type, text) {
    const success = document.getElementById('success-message');
    const error = document.getElementById('error-message');

    success.style.display = 'none';
    error.style.display = 'none';

    if (type === 'success') {
        success.querySelector('.message-text').textContent = text;
        success.style.display = 'flex';
        setTimeout(() => success.style.display = 'none', 5000);
    }

    if (type === 'error') {
        error.querySelector('.message-text').textContent = text;
        error.style.display = 'flex';
        setTimeout(() => error.style.display = 'none', 5000);
    }
}