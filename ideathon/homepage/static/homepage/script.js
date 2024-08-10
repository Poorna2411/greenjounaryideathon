document.addEventListener('DOMContentLoaded', function () {
    // Log to ensure the script is running
    console.log("DOM fully loaded and parsed");

    // Get the notice list element
    const noticeList = document.getElementById('notice-list');

    // Check if notice list element is found
    if (!noticeList) {
        console.error("Notice list element not found");
        return;
    }

    // Notices for the notice board
    const notices = [
        {
            text: 'Registration closes on July 31st!',
            link: '#registration'
        },
        {
            text: 'Keynote speaker announced: Dr. John Doe!',
            link: '#keynote'
        },
        {
            text: 'New workshops added to the schedule!',
            link: '#workshops'
        },
        {
            text: 'Early bird tickets available now!',
            link: '#earlybird'
        },
        {
            text: 'Event venue changed to Grand Hall!',
            link: '#venue'
        },
        {
            text: 'Join our pre-event networking session!',
            link: '#networking'
        }
    ];

    // Function to populate notice board with notices
    function populateNoticeBoard() {
        console.log("Populating notice board");
        
        // Clear any existing notices
        noticeList.innerHTML = '';

        // Add notices to the notice board
        notices.forEach(notice => {
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.href = notice.link;
            link.textContent = notice.text;
            listItem.appendChild(link);
            noticeList.appendChild(listItem);
        });

        console.log("Notice board updated with notices:", notices);
    }

    // Call the function to populate the notice board
    populateNoticeBoard();
});
