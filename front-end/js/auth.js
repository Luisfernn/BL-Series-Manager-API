/**
 * auth.js
 * Utilitário central de autenticação do front-end
 * Responsável por gerenciar token e acesso às páginas
 */

const TOKEN_KEY = 'bl_auth_token';

/**
 * Salva o token no navegador
 * @param {string} token
 */
function saveToken(token) {
    if (!token) return;
    localStorage.setItem(TOKEN_KEY, token);
}

/**
 * Retorna o token salvo
 * @returns {string|null}
 */
function getToken() {
    return localStorage.getItem(TOKEN_KEY);
}

/**
 * Remove o token (logout)
 */
function removeToken() {
    localStorage.removeItem(TOKEN_KEY);
}

/**
 * Verifica se o usuário está autenticado
 * @returns {boolean}
 */
function isAuthenticated() {
    return !!getToken();
}

/**
 * Protege páginas privadas
 * Se não estiver autenticado, redireciona para login
 */
function requireAuth() {
    if (!isAuthenticated()) {
        window.location.href = 'login.html';
    }
}