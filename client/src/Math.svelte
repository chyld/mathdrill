<script>
  import Atom from "./Atom.svelte";

  let component;
  let props;

  function clickButton(option) {
    component = Atom;
    props = {
      questionUrl: `http://phi:3000/basic/${option}`,
      title: `Basic ${option}`,
    };
  }

  clickButton(1);
</script>

<div>
  <button on:click={() => clickButton(1)}>Basic 1</button>
  <button on:click={() => clickButton(2)}>Basic 2</button>
  <button on:click={() => clickButton(3)}>Basic 3</button>

  <svelte:component this={component} {...props} />
</div>
