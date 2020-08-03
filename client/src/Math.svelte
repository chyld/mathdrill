<script>
  import Atom from "./Atom.svelte";

  let component;
  let props;
  let selected;

  function clickButton(option) {
    selected = option;
    component = Atom;
    props = {
      questionUrl: `http://phi:3000/basic/${option}`,
      title: `Basic ${option}`,
    };
  }

  clickButton(1);
</script>

<style>
  .active {
    background-color: coral;
    color: cornsilk;
  }
</style>

<div>
  <button class:active={selected == 1} on:click={() => clickButton(1)}>
    Basic 1
  </button>
  <button class:active={selected == 2} on:click={() => clickButton(2)}>
    Basic 2
  </button>
  <button class:active={selected == 3} on:click={() => clickButton(3)}>
    Basic 3
  </button>
  <button class:active={selected == 4} on:click={() => clickButton(4)}>
    Basic 4
  </button>

  <svelte:component this={component} {...props} />
</div>
