function addCard() {
    var textInput = document.getElementById('textInput').value;
    var imageUrlInput = document.getElementById('imageUrlInput').value;

    var cardContainer = document.getElementById('card-container');
    var card = document.createElement('div');
    card.className = 'card';

    var image = document.createElement('img');
    image.src = imageUrlInput;
    card.appendChild(image);

    var text = document.createElement('p');
    text.textContent = textInput;
    card.appendChild(text);

    cardContainer.appendChild(card);
}
