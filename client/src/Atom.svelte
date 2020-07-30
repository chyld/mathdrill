<script>
  export let questionUrl;
  export let title;

  let promiseQuestion;
  let guess;
  let answer;
  let inputRef;

  $: {
    // runs when title changes
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
      let response = JSON.parse(text);
      answer = response.answer;
      guess = "";
      inputRef.focus();
      return response;
    } else {
      throw new Error(text);
    }
  }

  function checkGuess() {
    if (guess === " " || guess == answer) return clickQuestion();
  }

  function clickQuestion() {
    promiseQuestion = getQuestion();
  }
</script>

<style>
  #question {
    color: #ff33cc;
    font-size: 55px;
  }
  #guessdiv {
    text-align: center;
    position: relative;
    top: 50px;
  }
  #guessinput {
    color: #454545;
    font-family: monospace;
    font-size: 40px;
    width: 350px;
  }
</style>

<div>
  <div id="guessdiv">
    <input
      id="guessinput"
      bind:value={guess}
      on:input={checkGuess}
      bind:this={inputRef} />
  </div>

  {#await promiseQuestion then response}
    {#if response}
      <div id="question">
        {@html displayMath(response.question)}
      </div>
    {/if}
  {:catch error}
    <p>{error.message}</p>
  {/await}
</div>
