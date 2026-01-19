// Dados de exemplo do BL
const blData = {
    id: 1,
    name: "Love in the Moonlight"
};

let characterCount = 1; // Começamos com 1 personagem

document.addEventListener('DOMContentLoaded', function() {
    // Carregar nome do BL
    document.getElementById('current-bl').textContent = blData.name;
    
    // Configurar formulário
    const form = document.getElementById('add-character-form');
    form.addEventListener('submit', handleSubmit);
});

function addCharacterSection() {
    characterCount++;
    const charactersContainer = document.getElementById('characters-container');
    
    const characterSection = document.createElement('div');
    characterSection.className = 'character-section';
    characterSection.id = `character-section-${characterCount}`;
    
    characterSection.innerHTML = `
        <div class="character-header">
            <h3 class="character-title">Personagem ${characterCount}</h3>
            <button type="button" class="remove-character-button" onclick="removeCharacterSection(${characterCount})">
                × Remover
            </button>
        </div>
        
        <div class="form-group">
            <label for="character-name-${characterCount}">Nome do Personagem</label>
            <input 
                type="text" 
                id="character-name-${characterCount}" 
                name="character-name-${characterCount}" 
                class="form-input"
                placeholder="Ex: Phaya"
                required
            >
        </div>

        <div class="form-group">
            <label for="actor-name-${characterCount}">Ator/Atriz</label>
            <input 
                type="text" 
                id="actor-name-${characterCount}" 
                name="actor-name-${characterCount}" 
                class="form-input"
                placeholder="Nome do ator ou atriz"
                required
            >
        </div>

        <div class="form-group">
            <label for="role-type-${characterCount}">Tipo de Papel</label>
            <select 
                id="role-type-${characterCount}" 
                name="role-type-${characterCount}" 
                class="form-select"
                required
            >
                <option value="">Selecione...</option>
                <option value="main">Main Role</option>
                <option value="support">Support Role</option>
            </select>
        </div>
    `;
    
    charactersContainer.appendChild(characterSection);
}

function removeCharacterSection(characterNumber) {
    const characterSection = document.getElementById(`character-section-${characterNumber}`);
    if (characterSection) {
        characterSection.remove();
    }
}

function handleSubmit(e) {
    e.preventDefault();
    
    const characters = [];
    
    for (let i = 1; i <= characterCount; i++) {
        const characterSection = document.getElementById(`character-section-${i}`);
        if (!characterSection) continue;
        
        const characterName = document.getElementById(`character-name-${i}`);
        const actorName = document.getElementById(`actor-name-${i}`);
        const roleType = document.getElementById(`role-type-${i}`);
        
        if (characterName && actorName && roleType) {
            const characterData = {
                characterName: characterName.value.trim(),
                actorName: actorName.value.trim(),
                roleType: roleType.value
            };
            
            if (characterData.characterName && characterData.actorName && characterData.roleType) {
                characters.push(characterData);
            }
        }
    }
    
    if (characters.length === 0) {
        showMessage('error', 'Por favor, preencha pelo menos um personagem completo.');
        return;
    }
    
    const requestData = {
        blId: blData.id,
        characters: characters
    };
    
    // Simulação de sucesso
    console.log('Dados dos personagens:', requestData);
    const charactersText =
        characters.length === 1
            ? '1 personagem foi adicionado'
            : `${characters.length} personagens foram adicionados`;
            
    showMessage('success', `✓ ${charactersText} com sucesso!`);
    
    // Limpar formulário
    document.getElementById('characters-container').innerHTML = '';
    characterCount = 0;
    addCharacterSection();
}

function showMessage(type, text) {
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');
    
    successMessage.style.display = 'none';
    errorMessage.style.display = 'none';
    
    if (type === 'success') {
        successMessage.querySelector('.message-text').textContent = text;
        successMessage.style.display = 'flex';
        
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 5000);
    } else if (type === 'error') {
        errorMessage.querySelector('.message-text').textContent = text;
        errorMessage.style.display = 'flex';
        
        setTimeout(() => {
            errorMessage.style.display = 'none';
        }, 5000);
    }
}