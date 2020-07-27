<script>
    let request;
    let answer;

    async function getBasic() {
		const res = await fetch(`http://phi:3000/basic/1`, {mode: 'cors'});
		const text = await res.text();
		if (res.ok) {
			return text;
		} else {
			throw new Error(text);
		}
	}

    async function sendAnswer() {
		const res = await fetch(`http://phi:3000/answer/${answer}`, {mode: 'cors'});
		const text = await res.text();
		if (res.ok) {
			return text;
		} else {
			throw new Error(text);
		}
	}

    function handleClick(){
        request = getBasic();
    }

    function handleAnswer(){
        console.log('the answer is:', answer);
        let x = sendAnswer();
    }
</script>

<div>
    <p>this is math</p>
    <button on:click={handleClick}>get question</button>
    <input bind:value={answer} on:input={handleAnswer}>

    {#await request}
	    <p>...waiting</p>
    {:then number}
	    <p>The number is {number}</p>
    {:catch error}
	    <p style="color: red">more {error.message}</p>
    {/await}
</div>

<style>
</style>
