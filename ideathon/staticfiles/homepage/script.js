// homepage/static/homepage/script.js

document.addEventListener('DOMContentLoaded', function() {
    const marquee = document.querySelector('.marquee');

    // Simulate fetching updates from a server or an API
    const updates = [
        'Update: Registration closes on July 31st!',
        'Update: Keynote speaker announced: Dr. John Doe!',
        'Update: New workshops added to the schedule!'
    ];

    // Function to populate marquee with updates
    function populateMarquee() {
        const content = updates.join(' <span class="separator">|</span> ');
        const duplicatedContent = content + ' <span class="separator">|</span> ' + content; // Duplicate content for seamless scroll

        marquee.innerHTML = `<p>${duplicatedContent}</p>`; // Wrap in <p> for inline display
    }

    // Function to set the scrolling speed
    function setScrollSpeed(speed) {
        document.documentElement.style.setProperty('--scroll-speed', speed + 's');
    }

    // Example of setting the scroll speed (change the value to adjust speed)
    setScrollSpeed(15); // Scroll speed in seconds

    // Populate the marquee with updates and start animation
    populateMarquee();

    // Scroll-triggered animations for sections
    const sections = document.querySelectorAll('section');
    
    function checkVisibility() {
        const triggerBottom = window.innerHeight / 5 * 4;
        sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            if (sectionTop < triggerBottom) {
                section.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', checkVisibility);
    checkVisibility();

    // Smooth scroll for navigation links and buttons
    document.querySelectorAll('nav ul li a, .btn').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
