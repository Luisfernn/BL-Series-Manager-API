// Obter BL pela URL
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

let messageTimeout = null;

document.addEventListener('DOMContentLoaded', async () => {
    requireAuth();
    await loadSeriesInfo();

    const form = document.getElementById('add_actor_form');
    if (form) {
        form.addEventListener('submit', handleSubmit);
    }
});

async function loadSeriesInfo() {
    try {
        const response = await fetch(`${API_BASE_URL}/series/${blId}`);
        if (response.ok) {
            const series = await response.json();
            document.getElementById('current_bl').textContent = series.title;
        }
    } catch (error) {
        console.error('Erro ao carregar serie:', error);
    }
}

function handleSubmit(event) {
    event.preventDefault();

    const actorNameInput = document.getElementById('actor_name');
    if (!actorNameInput) return;

    const actorName = actorNameInput.value.trim();

    if (!actorName) {
        showMessage('error', 'Por favor, digite o nome do ator.');
        return;
    }

    // NOTA: A API requer dados completos do ator (nickname, nationality, gender)
    // Este formulário apenas coleta o nome. Funcionalidade limitada.
    console.log('Dados coletados:', { blId, actorName });
    showMessage('error', 'API requer dados completos do ator. Formulario precisa ser expandido.');
}

function showMessage(type, text) {
    const successMessage = document.getElementById('success_message');
    const errorMessage = document.getElementById('error_message');

    if (!successMessage || !errorMessage) return;

    if (messageTimeout) {
        clearTimeout(messageTimeout);
        messageTimeout = null;
    }

    successMessage.style.display = 'none';
    errorMessage.style.display = 'none';

    if (type === 'success') {
        successMessage.querySelector('.message-text').textContent = text;
        successMessage.style.display = 'flex';

        messageTimeout = setTimeout(() => {
            successMessage.style.display = 'none';
        }, 5000);
    }

    if (type === 'error') {
        errorMessage.querySelector('.message-text').textContent = text;
        errorMessage.style.display = 'flex';

        messageTimeout = setTimeout(() => {
            errorMessage.style.display = 'none';
        }, 5000);
    }
}