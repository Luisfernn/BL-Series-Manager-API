// Dados de exemplo
const blData = {
    id: 1,
    name: "Love in the Moonlight"
};

// Tags existentes no banco (exemplo)
const existingTags = [
    { id: 1, name: "Romance" },
    { id: 2, name: "Drama" },
    { id: 3, name: "Fantasia" },
    { id: 4, name: "Sobrenatural" },
    { id: 5, name: "Ação" },
    { id: 6, name: "Comédia" },
    { id: 7, name: "Mistério" }
];

let newTagFieldCount = 1;

document.addEventListener('DOMContentLoaded', function() {
    // Carregar nome do BL
    document.getElementById('current-bl').textContent = blData.name;
    
    // Renderizar tags existentes
    renderExistingTags();
    
    // Configurar formulário
    const form = document.getElementById('add-tags-form');
    form.addEventListener('submit', handleSubmit);
});

function renderExistingTags() {
    const tagsList = document.getElementById('existing-tags-list');
    
    existingTags.forEach(tag => {
        const tagItem = document.createElement('div');
        tagItem.className = 'tag-checkbox-item';
        
        tagItem.innerHTML = `
            <input 
                type="checkbox" 
                id="tag-${tag.id}" 
                value="${tag.id}"
            >
            <label for="tag-${tag.id}">${tag.name}</label>
        `;
        
        tagsList.appendChild(tagItem);
    });
}

function addNewTagField() {
    newTagFieldCount++;
    const container = document.getElementById('new-tags-container');
    
    const fieldDiv = document.createElement('div');
    fieldDiv.className = 'new-tag-field';
    fieldDiv.id = `new-tag-field-${newTagFieldCount}`;
    
    fieldDiv.innerHTML = `
        <input 
            type="text" 
            id="new-tag-${newTagFieldCount}" 
            class="form-input"
            placeholder="Nome da nova tag"
        >
        <button type="button" class="remove-tag-button" onclick="removeNewTagField(${newTagFieldCount})">
            ×
        </button>
    `;
    
    container.appendChild(fieldDiv);
}

function removeNewTagField(fieldNumber) {
    const field = document.getElementById(`new-tag-field-${fieldNumber}`);
    if (field) {
        field.remove();
    }
}

function handleSubmit(e) {
    e.preventDefault();
    
    // Coletar tags selecionadas
    const selectedTags = [];
    const checkboxes = document.querySelectorAll('#existing-tags-list input[type="checkbox"]:checked');
    checkboxes.forEach(checkbox => {
        selectedTags.push(parseInt(checkbox.value));
    });
    
    // Coletar novas tags
    const newTags = [];
    for (let i = 1; i <= newTagFieldCount; i++) {
        const input = document.getElementById(`new-tag-${i}`);
        if (input && input.value.trim()) {
            newTags.push(input.value.trim());
        }
    }
    
    // Validar se pelo menos uma tag foi selecionada/criada
    if (selectedTags.length === 0 && newTags.length === 0) {
        showMessage('error', 'Por favor, selecione ou crie pelo menos uma tag.');
        return;
    }
    
    const requestData = {
        blId: blData.id,
        selectedTags: selectedTags,
        newTags: newTags
    };
    
    // Aqui você faria a chamada ao backend
    // fetch('/api/bls/' + blData.id + '/tags', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify(requestData)
    // })
    // .then(response => response.json())
    // .then(data => {
    //     showMessage('success', data.message || 'Tags vinculadas com sucesso!');
    //     // Opcional: voltar para a tela de detalhes
    //     // setTimeout(() => window.location.href = 'bl-details.html?id=' + blData.id, 2000);
    // })
    // .catch(error => {
    //     showMessage('error', 'Erro ao vincular tags. Tente novamente.');
    // });
    
    // Simulação de sucesso (remover quando implementar o backend real)
    console.log('Dados enviados:', requestData);
    const totalTags = selectedTags.length + newTags.length;
    const tagsText = totalTags === 1 ? '1 tag foi vinculada' : `${totalTags} tags foram vinculadas`;
    showMessage('success', `✓ ${tagsText} com sucesso!`);
}

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