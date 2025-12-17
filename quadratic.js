function isNotNumber(a, b, c) {
  if (isNaN(a) || isNaN(b) || isNaN(c)) {
    console.log("Խնդրում ենք մուտքագրել միայն թվեր");
    return true;
  }
  return false;
}

function solveEquation(a, b, c) {
  if (a === 0) {
    if (b === 0) {
      if (c === 0) {
        console.log("Անսահման բազմակի լուծում՝ x ∈ (-∞, +∞)");
      } else {
        console.log("Լուծում չկա");
      }
    } else {
      const x = -c / b;
      console.log(`Միակ լուծումը՝ x = ${x}`);
    }
  } else {
    const D = b ** 2 - 4 * a * c;
    handleDiscriminant(a, b, c, D);
  }
}

function handleDiscriminant(a, b, c, D) {
  if (D === 0) {
    const x = -b / (2 * a);
    console.log(`Կրկնվող լուծում՝ x = ${x}`);
  } else if (D > 0) {
    const x1 = (-b + Math.sqrt(D)) / (2 * a);
    const x2 = (-b - Math.sqrt(D)) / (2 * a);
    console.log(`Երկու տարբեր լուծում՝ x₁ = ${x1}, x₂ = ${x2}`);
  } else {
    console.log("Թվային լուծում չի կարող լինել (հիմնականում անհնար)");
  }
}

const testCases = [
  [1, 4, 2],
  [1, 4, 4],
  [3, 1, 4],
  [2, 4, 0],
  [4, 0, 4],
  [0, 4, 1],
  [0, 0, 0],
  [0, 0, 5],
];

for (const [a, b, c] of testCases) {
  console.log(`\nՓորձում ենք լուծել՝ ${a}x² + ${b}x + ${c} = 0`);
  if (!isNotNumber(a, b, c)) {
    solveEquation(a, b, c);
  }
}

