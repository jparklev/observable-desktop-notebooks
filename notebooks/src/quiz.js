// Interactive multiple-choice quiz component for Observable Framework
// Usage:
//   display(Quiz({
//     question: "What is 2 + 2?",
//     options: ["3", "4", "5", "6"],
//     correctIndex: 1,
//     explanation: "2 + 2 equals 4."
//   }));

// FT Paper colors for parchment theme
const colors = {
  primary: "#0f5499",
  positive: "#2d724f",
  negative: "#b3312c",
  background: "#faf6f3",
  border: "#d4c8c0",
  text: "#4a413a"
};

export function Quiz({
  question,
  options,
  correctIndex,
  explanation
}) {
  // Input validation
  if (typeof question !== "string" || !question.trim()) {
    throw new Error("Quiz requires a non-empty question string");
  }
  if (!Array.isArray(options) || options.length < 2) {
    throw new Error("Quiz requires at least 2 options");
  }
  if (!Number.isInteger(correctIndex) || correctIndex < 0 || correctIndex >= options.length) {
    throw new Error(`correctIndex must be 0-${options.length - 1}, got ${correctIndex}`);
  }
  if (typeof explanation !== "string") {
    throw new Error("Quiz requires an explanation string");
  }

  // Create container
  const container = document.createElement("div");
  container.style.cssText = `
    border: 1px solid ${colors.border};
    border-radius: 8px;
    padding: 20px;
    margin: 24px 0;
    background: ${colors.background};
    font-family: system-ui, sans-serif;
    color: ${colors.text};
  `;

  // Question
  const questionEl = document.createElement("div");
  questionEl.style.cssText = `
    font-weight: 600;
    margin-bottom: 16px;
    font-size: 1.1em;
    line-height: 1.4;
  `;
  questionEl.textContent = question;
  container.appendChild(questionEl);

  // Options container
  const optionsContainer = document.createElement("div");
  optionsContainer.style.cssText = "display: flex; flex-direction: column; gap: 8px;";

  // Unique name for radio group
  const groupName = `quiz-${Math.random().toString(36).substr(2, 9)}`;

  // State
  let selectedIndex = null;
  let submitted = false;

  // Create option elements
  const optionElements = options.map((opt, i) => {
    const label = document.createElement("label");
    label.style.cssText = `
      display: flex;
      align-items: center;
      padding: 10px 12px;
      cursor: pointer;
      border-radius: 4px;
      border: 1px solid transparent;
      transition: all 0.15s;
    `;

    const radio = document.createElement("input");
    radio.type = "radio";
    radio.name = groupName;
    radio.value = i;
    radio.style.cssText = `margin-right: 12px; accent-color: ${colors.primary};`;

    const span = document.createElement("span");
    span.textContent = opt;

    const marker = document.createElement("span");
    marker.style.cssText = "margin-left: auto; font-weight: 600; display: none;";

    label.appendChild(radio);
    label.appendChild(span);
    label.appendChild(marker);

    // Hover effects
    label.addEventListener("mouseover", () => {
      if (!submitted) label.style.background = "#f0ebe7";
    });
    label.addEventListener("mouseout", () => {
      if (!submitted) label.style.background = "transparent";
    });

    // Selection
    radio.addEventListener("change", () => {
      if (!submitted) selectedIndex = i;
    });

    optionsContainer.appendChild(label);
    return { label, radio, marker };
  });

  container.appendChild(optionsContainer);

  // Button row
  const buttonRow = document.createElement("div");
  buttonRow.style.cssText = "margin-top: 20px; display: flex; align-items: center; gap: 12px;";

  const button = document.createElement("button");
  button.textContent = "Check Answer";
  button.style.cssText = `
    background: ${colors.primary};
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
    font-size: 0.95em;
    opacity: 0.5;
    transition: opacity 0.15s;
  `;
  button.disabled = true;

  const resultSpan = document.createElement("span");
  resultSpan.style.cssText = "font-weight: 600;";

  buttonRow.appendChild(button);
  buttonRow.appendChild(resultSpan);
  container.appendChild(buttonRow);

  // Explanation (hidden initially)
  const explanationEl = document.createElement("div");
  explanationEl.style.cssText = `
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid ${colors.border};
    line-height: 1.5;
    display: none;
  `;
  explanationEl.innerHTML = `<strong>Explanation:</strong> ${explanation}`;
  container.appendChild(explanationEl);

  // Enable button when option selected
  optionElements.forEach(({ radio }) => {
    radio.addEventListener("change", () => {
      if (!submitted) {
        button.disabled = false;
        button.style.opacity = "1";
      }
    });
  });

  // Submit handler
  button.addEventListener("click", () => {
    if (submitted || selectedIndex === null) return;
    submitted = true;

    // Disable all radios
    optionElements.forEach(({ radio }) => {
      radio.disabled = true;
    });

    // Disable button
    button.disabled = true;
    button.style.opacity = "0.5";

    // Show results
    const isCorrect = selectedIndex === correctIndex;
    resultSpan.textContent = isCorrect ? "Correct!" : "Not quite.";
    resultSpan.style.color = isCorrect ? colors.positive : colors.negative;

    // Highlight options
    optionElements.forEach(({ label, marker }, i) => {
      if (i === correctIndex) {
        label.style.background = `${colors.positive}15`;
        label.style.borderColor = colors.positive;
        marker.textContent = "✓";
        marker.style.color = colors.positive;
        marker.style.display = "inline";
      } else if (i === selectedIndex) {
        label.style.background = `${colors.negative}15`;
        label.style.borderColor = colors.negative;
        marker.textContent = "✗";
        marker.style.color = colors.negative;
        marker.style.display = "inline";
      }
    });

    // Show explanation
    explanationEl.style.display = "block";
  });

  return container;
}
