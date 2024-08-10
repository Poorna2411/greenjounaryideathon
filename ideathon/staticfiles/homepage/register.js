// homepage/static/homepage/register.js

document.addEventListener("DOMContentLoaded", function() {
    const teamMembersInput = document.getElementById("team_members");
    const teamMembersContainer = document.getElementById("teamMembersContainer");
    const paymentButton = document.getElementById("paymentButton");
    const paymentDetails = document.getElementById("paymentDetails");
    const totalPayment = document.getElementById("totalPayment");

    teamMembersInput.addEventListener("input", updateTeamMembers);

    function updateTeamMembers() {
        teamMembersContainer.innerHTML = "";
        const numberOfMembers = parseInt(teamMembersInput.value) || 0;
        for (let i = 1; i <= numberOfMembers; i++) {
            const label = document.createElement("label");
            label.setAttribute("for", `team_member_${i}`);
            label.textContent = `Team Member ${i} Name`;
            const input = document.createElement("input");
            input.setAttribute("type", "text");
            input.setAttribute("id", `team_member_${i}`);
            input.setAttribute("name", `team_member_${i}`);
            input.required = true;
            teamMembersContainer.appendChild(label);
            teamMembersContainer.appendChild(input);
        }
        totalPayment.textContent = numberOfMembers * 20; // Assuming ₹100 per team member
    }

    paymentButton.addEventListener("click", function() {
        paymentDetails.style.display = "block";
    });
});
