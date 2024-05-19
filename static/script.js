// Função para validar senha
function validarSenha() {
    var senha = document.getElementsByName("senha")[0].value;
    var confirmarSenha = document.getElementsByName("confirmar_senha")[0].value;
    var senhaValida = true;

    if (senha !== confirmarSenha) {
        alert("As senhas não correspondem.");
        senhaValida = false;
    }

    var pattern = /^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$/;
    if (!pattern.test(senha)) {
        alert("A senha deve conter pelo menos 8 caracteres, incluindo uma letra maiúscula, um caractere especial, e um número.");
        senhaValida = false;
    }

    return senhaValida;
}

// Adiciona um listener para o evento 'submit' do formulário
document.querySelector("form").addEventListener("submit", function(event) {
    if (!validarSenha()) {
        event.preventDefault();
    }
});
