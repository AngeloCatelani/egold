/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    people.sort((a, b) => a - b); // Sort people by weight
    let i = 0;
    let j = people.length - 1;
    let boats = 0;

    while (i <= j) {
        if (people[i] + people[j] <= limit) {
            i++; // lightest person boards with heaviest
        }
        j--; // heaviest person always boards
        boats++; // we used a boat
    }

    return boats;
};