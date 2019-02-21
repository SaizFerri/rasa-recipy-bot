function createPersonMessage(msg) {
  return `<li class="chat__list--item chat__list--item-person">${msg}</li>`
}

function createBotMessage(msg) {
  return `<li class="chat__list--item chat__list--item-bot">${msg}</li>`
}

async function sendMessage(msg) {
  const apiCall = await fetch('http://localhost:5005/webhooks/rest/webhook', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({message: msg})
  });
  return await apiCall.json();
}

$('.js-action').click(async (e) => {
  e.preventDefault();
  
  let text = $('.js-chat-input').val();

  $('.js-chat-list').append(createPersonMessage(text));
  $('.js-chat-input').val('');

  if (text !== '') {
    const response = await sendMessage(text);
    let responseText = response[0]['text'];

    $('.js-chat-list').append(createBotMessage(responseText));
    $('.js-chat-list').scrollTop($('.js-chat-list').prop('scrollHeight'));
  }
});