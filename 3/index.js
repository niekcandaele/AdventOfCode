const input = require('./input');

let lines = input.split('\n');
lines = lines.slice(1, lines.length - 1);
console.log(lines);

const slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

function checkSlope(moveX, moveY) {
    // Start top left
    let pos = [0, 0];

    // Trees we ran into
    let trees = 0
    let empty = 0

    while (pos[1] < lines.length - 1) {
        pos[0] += moveX;
        pos[1] += moveY;
        const tile = getTile(pos[0], pos[1]);
        if (tile) {
            if (tile === '#') {
                trees++
            } else {
                empty++
            }
        }
    }

    function getTile(x, y) {
        const row = lines[y];
        return row[x % row.length];
    }

    console.log(`Found ${trees}/${empty} trees`);
    return trees;
}

let total = 1;
for (const slope of slopes) {
    console.log(slope);
    total = total * checkSlope(slope[0], slope[1])
}

console.log(`Answer: ${total}`);