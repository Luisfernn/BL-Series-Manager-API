// Dados de exemplo do BL
const blData = {
    id: 1,
    name: "Love in the Moonlight"
};

let messageTimeout = null;

document.addEventListener('DOMContentLoaded', () => {
    const blNameEl = document.getElementById('current-bl');
    const form = document.getElementById('add-actor-form');

    if (blNameEl) {
        blNameEl.textContent = blData.name;
    }

    if (form) {
        form.addEventListener('submit', handleSubmit);
    }
});

function handleSubmit(event) {
    event.preventDefault();

    const actorNameInput = document.getElementById('actor-name');
    if (!actorNameInput) return;

    const actorName = actorNameInput.value.trim();

    if (!actorName) {
        showMessage('error', 'Por favor, digite o nome do ator.');
        return;
    }

    // Simulação de sucesso (remover quando implementar o backend real)
    showMessage(
        'success',
        `Ator "${actorName}" foi vinculado com sucesso ao BL.`
    );

    actorNameInput.value = '';
}

function showMessage(type, text) {
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');

    if (!successMessage || !errorMessage) return;

    // Limpar timeout anterior
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