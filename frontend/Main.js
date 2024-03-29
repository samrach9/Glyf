// JavaScript code to populate story cards
document.addEventListener('DOMContentLoaded', function () {
    // Sample data (you can replace this with your actual data)
    const stories = [
        {
            title: 'Story 1',
            time: '5:30 pm P.S.T., Saturday, 2/17/24',
            uploadedBy: 'user123'
        },
        {
            title: 'Story 2',
            time: '6:00 pm P.S.T., Sunday, 2/18/24',
            uploadedBy: 'user456'
        },
        // Add more stories as needed
    ];

    // Function to create a story card HTML element
    function createStoryCard(story) {
        const storyCard = document.createElement('div');
        storyCard.classList.add('storyCard');

        storyCard.innerHTML = `
            <div class="storyImage"></div>
            <p class="storyCardFont">${story.title}</p>
            <p class="storyCardDetails">${story.time}</p>
            <p class="storyCardDetails">Uploaded by: ${story.uploadedBy}</p>
        `;

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
