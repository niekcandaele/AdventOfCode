const input = require('./input');


console.log('PART ONE');

for (let i = 0; i < input.length; i++) {
    const e1 = input[i];
    for (let j = 0; j < input.length; j++) {
        const e2 = input[j];

        if (e1 + e2 === 2020) {
            console.log(`The answer is ${e1 * e2}`);
        }
    }
}

console.log('PART TWO');

for (let i = 0; i < input.length; i++) {
    const e1 = input[i];
    for (let j = 0; j < input.length; j++) {
        const e2 = input[j];
        for (let k = 0; k < input.length; k++) {
            const e3 = input[k];

            if (e1 + e2 + e3 === 2020) {
                console.log(`The answer is ${e1 * e2 * e3}`);
            }
        }
    }
}