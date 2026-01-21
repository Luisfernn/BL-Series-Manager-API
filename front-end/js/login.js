/**
 * Sistema de Login - BL Archive
 * Simulação de autenticação (frontend apenas)
 */

// Aguardar o carregamento completo do DOM
document.addEventListener('DOMContentLoaded', function() {
    initializeLoginForm();
});

/**
 * Inicializa o formulário de login
 */
function initializeLoginForm() {
    const form = document.getElementById('login-form');
    
    // Adicionar listener ao formulário
    form.addEventListener('submit', handleLoginSubmit);
    
    // Adicionar listeners aos inputs para limpar mensagens
    const inputs = form.querySelectorAll('.form-input');
    inputs.forEach(input => {
        input.addEventListener('focus', clearMessages);
    });
}

/**
 * Processa o envio do formulário
 * @param {Event} event - Evento de submit
 */
function handleLoginSubmit(event) {
    event.preventDefault();
    
    // Obter valores dos campos
    const loginValue = document.getElementById('login').value.trim();
    const passwordValue = document.getElementById('password').value.trim();
    
    // Validação básica (apenas visual)
    if (!loginValue || !passwordValue) {
        showMessage('error', 'Por favor, preencha todos os campos.');
        return;
    }
    
    // Validação de comprimento mínimo (apenas visual)
    if (loginValue.length < 3) {
        showMessage('error', 'Login deve ter pelo menos 3 caracteres.');
        return;
    }
    
    if (passwordValue.length < 4) {
        showMessage('error', 'Senha deve ter pelo menos 4 caracteres.');
        return;
    }
    
    // Simular loading
    simulateLogin(loginValue, passwordValue);
}

/**
 * Simula o processo de login
 * @param {string} login - Login do usuário
 * @param {string} password - Senha do usuário
 */
function simulateLogin(login, password) {
    const submitButton = document.querySelector('.submit-button');
    const originalText = submitButton.innerHTML;
    
    // Desabilitar botão e mostrar loading
    submitButton.disabled = true;
    submitButton.innerHTML = '<span class="button-text">Entrando...</span>';
    
    // Log dos dados (apenas para demonstração)
    console.log('=== Tentativa de Login ===');
    console.log('Login:', login);
    console.log('Senha:', password);
    console.log('Timestamp:', new Date().toISOString());
    console.log('========================');
    
    // Simular delay de requisição (1.5 segundos)
    setTimeout(() => {
        // Restaurar botão
        submitButton.disabled = false;
        submitButton.innerHTML = originalText;
        
        // Mostrar mensagem de sucesso
        showMessage('success', 'Login realizado com sucesso! Redirecionando...');
        
        // Simular redirecionamento após 2 segundos
        setTimeout(() => {
            console.log('Redirecionando para index.html...');
            // window.location.href = 'index.html';
        }, 2000);
    }, 1500);
}

/**
 * Exibe mensagem de feedback
 * @param {string} type - Tipo da mensagem ('success' ou 'error')
 * @param {string} text - Texto da mensagem
 */
function showMessage(type, text) {
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');
    
    // Esconder todas as mensagens primeiro
    successMessage.style.display = 'none';
    errorMessage.style.display = 'none';
    
    // Mostrar mensagem apropriada
    if (type === 'success') {
        successMessage.querySelector('.message-text').textContent = text;
        successMessage.style.display = 'flex';
        
        // Auto-esconder após 5 segundos
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 5000);
    } else if (type === 'error') {
        errorMessage.querySelector('.message-text').textContent = text;
        errorMessage.style.display = 'flex';
        
        // Auto-esconder após 5 segundos
        setTimeout(() => {
            errorMessage.style.display = 'none';
        }, 5000);
    }
}

/**
 * Limpa todas as mensagens de feedback
 */
function clearMessages() {
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');
    
    successMessage.style.display = 'none';
    errorMessage.style.display = 'none';
}