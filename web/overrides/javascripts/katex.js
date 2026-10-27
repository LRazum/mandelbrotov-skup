// Prikaz formula pomoću KaTeX-a nakon svakog učitavanja stranice.
// Proširenje arithmatex omata formule u \( … \) i \[ … \].
document$.subscribe(({ body }) => {
  renderMathInElement(body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false },
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true },
    ],
  });
});
