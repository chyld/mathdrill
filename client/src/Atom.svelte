<script>
  export let questionUrl;
  export let title;
  let promiseQuestion;
  let guess;
  let questionObject;
  let inputRef;

  $: {
    console.log("Loading:", title);
    clickQuestion();
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
</style>

<div>
  <h1>{title}</h1>
  <input bind:value={guess} on:input={typingAnswer} bind:this={inputRef} />

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
