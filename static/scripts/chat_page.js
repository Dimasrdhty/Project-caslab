document.addEventListener('DOMContentLoaded', () => {

  document.querySelector('#show-sidebar_button').onclick = () => {
    document.querySelector('#sidebar').classList.toggle('view-sidebar');
  };

  let msg = document.querySelector('#user_message');
  msg.addEventListener('keyup', function(event) => {
    event.preventDefault();
    if (event.keyCode === 13) {
      document.querySelector('#send_message').click();
    }
  });
});
