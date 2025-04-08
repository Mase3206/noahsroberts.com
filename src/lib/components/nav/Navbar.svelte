<!-- Header.svelte -->

<script>
	let { children } = $props();
</script>

<header class="flex mx-8 p-0">
	{@render children?.()}
</header>