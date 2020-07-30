<script>
  import rough from "roughjs/bundled/rough.cjs.js";
  import { onMount } from "svelte";

  export let questionUrl;
  export let title;

  let promiseQuestion;
  let guess;
  let questionObject;
  let inputRef;
  let draw;
  let rc;
  let dimW = 250;
  let dimH = 75;

  onMount(() => {
    draw = document.getElementById("draw");
    rc = rough.canvas(draw);
  });

  $: {
    // runs when title changes
    console.log("Loading:", title);
    clickQuestion();
  }

  function choice(list) {
    const n = list.length;
    const i = Math.floor(Math.random() * n);
    return list[i];
  }

  function drawSketch() {
    const colors = ["red", "blue", "green", "purple", "#ff33cc"];
    const fills = [
      "hachure",
      "zigzag",
      "cross-hatch",
      "dots",
      "sunburst",
      "dashed",
      "zigzag-line",
    ];
    rc.ctx.clearRect(0, 0, dimW, dimH);
    rc.rectangle(10, 10, dimW - 20, dimH - 20, {
      roughness: 1.8,
      fill: choice(colors),
      fillStyle: choice(fills),
      roughness: 2.5,
    });
  }

  function displayMath(markup) {
    let html = MathJax.tex2svg(markup, { display: true });
    let text = html.outerHTML;
    return text;
  }

  async function getQuestion() {
    const res = await fetch(questionUrl, { mode: "cors" });
    const text = await res.text();
    if (res.ok) {
      questionObject = JSON.parse(text);
      guess = "";
      inputRef.focus();
      drawSketch();
      return questionObject;
    } else {
      throw new Error(text);
    }
  }

  async function sendGuess() {
    if (guess === " ") return clickQuestion();
    if (isNaN(guess) || !guess.length) return;

    const res = await fetch(
      `http://phi:3000/attempt/${questionObject.drill_id}/${guess}`,
      { mode: "cors", method: "put" }
    );
    const text = await res.text();
    if (res.ok) {
      let attemptResponse = JSON.parse(text);
      if (attemptResponse.status) clickQuestion();
    } else {
      throw new Error(text);
    }
  }

  function typingAnswer() {
    sendGuess();
  }

  function clickQuestion() {
    promiseQuestion = getQuestion();
  }
</script>

<style>
  .question {
    color: #ff33cc;
    font-size: 55px;
  }
  #guess {
    font-size: 40px;
    position: relative;
    top: -80px;
    background: rgba(255, 255, 255, 0.3);
    width: 250px;
    font-family: monospace;
    color: #353535;
  }
</style>

<div>
  <canvas id="draw" width={dimW} height={dimH} />
  <div />
  <input
    id="guess"
    bind:value={guess}
    on:input={typingAnswer}
    bind:this={inputRef} />

  {#await promiseQuestion}
    <p>...waiting</p>
  {:then question}
    {#if question}
      <div class="question">
        {@html displayMath(question.question)}
      </div>
    {/if}
  {:catch error}
    <p>{error.message}</p>
  {/await}
</div>
