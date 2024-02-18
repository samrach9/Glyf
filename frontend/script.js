// JavaScript code to populate story cards
document.addEventListener('DOMContentLoaded', function () {
    const stories = [
        {
            title: 'Story 1',
            time: '5:30 pm P.S.T., Saturday, 2/17/24',
            uploadedBy: 'user123',
            summary: 'Today I went to the store and I bought some salmon and broccoli to make for dinner for the next week.'
        },
        {
            title: 'Story 2',
            time: '6:00 pm P.S.T., Sunday, 2/18/24',
            uploadedBy: 'user456',
            summary: 'Today I went to the store and I bought some salmon and broccoli to make for dinner for the next week.'
        },
        {
            title: 'Story 3',
            time: '6:00 pm P.S.T., Sunday, 2/18/24',
            uploadedBy: 'user456',
            summary: 'Today I went to the store and I bought some salmon and broccoli to make for dinner for the next week.'
        },
        // Add more stories as needed
    ];

    // Function to create a story card HTML element
    function createStoryCard(story) {
        const storyCard = document.createElement('div');
        storyCard.classList.add('storyCard');

        storyCard.innerHTML = `
            <div class="cardDisplay storyCard" onclick="expandCard(this)">
                <div class="storyImage"></div>
                <p class="storyCardFont">${story.title}</p>
                <p class="storyCardDetails">${story.time}</p>
                <p class="storyCardDetails">Uploaded by: ${story.uploadedBy}</p>
                <p class="storyCardDetails hiddenText">${story.summary}</p>
            </div>
        `;

        storyCard.querySelector('.cardDisplay').addEventListener("click", function() {
            var hiddenText = this.querySelector('.hiddenText');
            if (hiddenText.style.display === "none" || hiddenText.style.display === "") {
                hiddenText.style.display = "block";
            } else {
                hiddenText.style.display = "none";
            }
        });

        return storyCard;
    }

    // Function to populate story cards
    function populateStoryCards() {
        const storyContainer = document.querySelector('.storyContainer .row');

        stories.forEach(story => {
            const storyCard = createStoryCard(story);
            storyContainer.appendChild(storyCard);
        });
    }

    // Call the function to populate story cards when the DOM content is loaded
    populateStoryCards();
});
