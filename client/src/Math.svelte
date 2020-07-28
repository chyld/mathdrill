<script>
    let promise;

	function displayMath(markup){
		let html = MathJax.tex2svg(markup, {display: true});
		let text = html.outerHTML;
		return text;
	}

    async function getQuestion() {
		const res = await fetch(`http://phi:3000/basic/1`, {mode: 'cors'});
		const text = await res.text();
		if (res.ok) {
			return JSON.parse(text);
		} else {
			throw new Error(text);
		}
	}

    function clickGetQuestion(){
        promise = getQuestion();
    }
</script>

<div>
    <button on:click={clickGetQuestion}>Next Question</button>

    {#await promise}
	    <p>...waiting</p>
	{:then response}
		{#if response}
			<div class='question'>
				{@html displayMath(response.question)}
			</div>
		{/if}
    {:catch error}
	    <p>{error.message}</p>
    {/await}
</div>

<style>
	.question{
		color: #ff33cc;
		font-size: 55px;
	}
</style>
