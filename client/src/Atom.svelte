<script>
  import { beforeUpdate } from "svelte";

  beforeUpdate(() => {
    clickQuestion();
  });

  export let questionUrl;
  let promiseQuestion;
  let promiseAnswer;
  let answer;
  let currentQuestion;

  function displayMath(markup) {
    let html = MathJax.tex2svg(markup, { display: true });
    let text = html.outerHTML;
    return text;
  }

  async function getQuestion() {
    console.log("getting a question");
    const res = await fetch(questionUrl, { mode: "cors" });
    const text = await res.text();
    if (res.ok) {
      currentQuestion = JSON.parse(text);
      return currentQuestion;
    } else {
      throw new Error(text);
    }
  }

  async function sendAnswer() {
    let attemptResponse;
    const res = await fetch(
      `http://phi:3000/attempt/${currentQuestion.drill_id}/${answer}`,
      { mode: "cors", method: "put" }
    );
    const text = await res.text();
    if (res.ok) {
      attemptResponse = JSON.parse(text);
      if (attemptResponse.status) {
        console.log("good attempt");
        clickGetQuestion();
      } else {
        console.log("bad attempt");
      }
    } else {
      throw new Error(text);
    }
  }

  function inputAnswer() {
    promiseAnswer = sendAnswer();
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
  <input bind:value={answer} on:input={inputAnswer} />

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
