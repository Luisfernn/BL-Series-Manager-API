/**
 * login.js
 * Login real integrado com backend
 */

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('login-form');
    form.addEventListener('submit', handleLogin);
});

/**
 * Envio do formulário de login
 */
async function handleLogin(event) {
    event.preventDefault();

    const loginInput = document.getElementById('login');
    const passwordInput = document.getElementById('password');

    const login = loginInput.value.trim();
    const password = passwordInput.value.trim();

    if (!login || !password) {
        showMessage('error', 'Preencha login e senha.');
        return;
    }

    setLoading(true);

    try {
        const response = await fetch('http://localhost:8000/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ login, password })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Login inválido');
        }

        const data = await response.json();

        // Salva token usando auth.js
        saveToken(data.access_token);

        showMessage('success', 'Login realizado com sucesso!');

        setTimeout(() => {
            window.location.href = 'index.html';
        }, 1000);

    } catch (err) {
        showMessage('error', err.message);
    } finally {
        setLoading(false);
    }
}

/**
 * Feedback visual
 */
function showMessage(type, text) {
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');

    successMessage.style.display = 'none';
    errorMessage.style.display = 'none';

    if (type === 'success') {
        successMessage.querySelector('.message-text').textContent = text;
        successMessage.style.display = 'flex';
    } else {
        errorMessage.querySelector('.message-text').textContent = text;
        errorMessage.style.display = 'flex';
    }
}

/**
 * Estado de loading no botão
 */
function setLoading(isLoading) {
    const button = document.querySelector('.submit-button');

    if (isLoading) {
        button.disabled = true;
        button.innerText = 'Entrando...';
    } else {
        button.disabled = false;
        button.innerText = 'Entrar';
    }
}