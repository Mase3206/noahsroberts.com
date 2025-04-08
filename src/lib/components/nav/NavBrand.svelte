<script>
	let { children } = $props();
</script>

<a href="/" class="no-underline hover:underline text-xl">
	{@render children()}
</a>