function copyToClipboard(target_element) {
    // Seleciona o elemento com o texto que você deseja copiar
    var textToCopy = document.getElementById(target_element);

    // Cria um elemento de área de transferência
    var clipboard = navigator.clipboard;

    // Copia o texto para a área de transferência
    clipboard.writeText(textToCopy.textContent.trim())
        .then(function() {
            // Exibe a mensagem temporária
            var copyMessage = document.getElementById('message_api');
            copyMessage.style.display = 'block';
            copyMessage.style.opacity = 1;

            // Oculta a mensagem após alguns segundos (tempo ajustável)
            setTimeout(function () {
                copyMessage.style.opacity = 0;
                setTimeout(function () {
                    copyMessage.style.display = 'none';
                }, 500); // Tempo de transição definido no estilo
            }, 2000); // 2000 milissegundos = 2 segundos
        })
        .catch(function(err) {
            console.error('Erro ao copiar para a área de transferência:', err);
        });
}
